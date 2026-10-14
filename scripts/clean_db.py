#!/usr/bin/env python3
"""Delete all rows from the Argus-V dashboard SQLite database, preserving its schema."""

import argparse
import sqlite3
import sys
from pathlib import Path


DEFAULT_DB = Path(__file__).resolve().parents[1] / "Research" / "hook_research.sqlite3"


def quote_identifier(value: str) -> str:
    """Quote a SQLite identifier obtained from sqlite_master."""
    return '"' + value.replace('"', '""') + '"'


def clean_database(path: Path, *, vacuum: bool = False) -> dict[str, int]:
    """Remove all rows in one transaction; return deleted row counts by table."""
    if not path.is_file():
        raise FileNotFoundError(f"SQLite database does not exist: {path}")

    connection = sqlite3.connect(path, timeout=30)
    try:
        connection.execute("PRAGMA busy_timeout=30000")
        connection.execute("PRAGMA foreign_keys=OFF")
        tables = [row[0] for row in connection.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        )]
        counts = {
            table: connection.execute(f"SELECT COUNT(*) FROM {quote_identifier(table)}").fetchone()[0]
            for table in tables
        }

        connection.execute("BEGIN IMMEDIATE")
        try:
            for table in tables:
                connection.execute(f"DELETE FROM {quote_identifier(table)}")
            if connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND name='sqlite_sequence'"
            ).fetchone():
                connection.execute("DELETE FROM sqlite_sequence")
            connection.commit()
        except Exception:
            connection.rollback()
            raise

        # Checkpoint the WAL so deleted pages are consolidated into the database file.
        connection.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        if vacuum:
            connection.execute("VACUUM")
        return counts
    finally:
        connection.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Clear rows from the dashboard SQLite database while preserving tables and indexes."
    )
    parser.add_argument("--db", type=Path, default=DEFAULT_DB,
                        help=f"database path (default: {DEFAULT_DB})")
    parser.add_argument("--vacuum", action="store_true",
                        help="rebuild the database file after clearing rows to reclaim disk space")
    parser.add_argument("--yes", action="store_true", help="skip the interactive confirmation")
    args = parser.parse_args(argv)
    db_path = args.db.expanduser().resolve()

    if not db_path.is_file():
        print(f"SQLite 데이터베이스 파일이 없습니다: {db_path}", file=sys.stderr)
        return 1

    # Show the exact target and row counts before making any change.
    try:
        with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=10) as connection:
            tables = [row[0] for row in connection.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )]
            counts = {
                table: connection.execute(f"SELECT COUNT(*) FROM {quote_identifier(table)}").fetchone()[0]
                for table in tables
            }
    except sqlite3.Error as error:
        print(f"데이터베이스를 읽을 수 없습니다: {error}", file=sys.stderr)
        return 1

    print(f"대상 DB: {db_path}")
    if not counts:
        print("삭제할 테이블이 없습니다.")
        return 0
    for table, count in counts.items():
        print(f"  {table}: {count:,} rows")
    print("테이블 구조와 인덱스는 유지하고, 위 테이블의 모든 행을 삭제합니다.")

    if not args.yes:
        try:
            answer = input("계속하려면 DELETE를 입력하세요: ")
        except EOFError:
            answer = ""
        if answer != "DELETE":
            print("취소했습니다.")
            return 1

    try:
        deleted = clean_database(db_path, vacuum=args.vacuum)
    except (OSError, sqlite3.Error) as error:
        print(f"DB 초기화에 실패했습니다: {error}", file=sys.stderr)
        return 1

    total = sum(deleted.values())
    print(f"완료: {total:,}개 행을 삭제했습니다.")
    if args.vacuum:
        print("VACUUM을 완료해 DB 파일의 미사용 공간을 회수했습니다.")
    else:
        print("디스크 공간까지 회수하려면 --vacuum 옵션을 추가하세요.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
