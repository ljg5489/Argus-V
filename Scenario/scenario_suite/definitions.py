"""Small, declarative contracts for local-only business task mocks."""
from copy import deepcopy


def tool(kind, params=None, **config):
    properties, required = {}, []
    for name, descriptor in (params or {}).items():
        optional = descriptor.startswith("?") or descriptor.endswith("?")
        descriptor = descriptor.strip("?")
        if descriptor == "token":
            item = {"type": ["string", "null"], "maxLength": 512}
        elif descriptor == "strings":
            item = {"type": "array", "items": {"type": "string", "maxLength": 4096}, "maxItems": 32}
        else:
            item = {"type": {"str": "string", "int": "integer", "number": "number", "bool": "boolean"}[descriptor]}
            if descriptor == "str":
                item["maxLength"] = 32768
        properties[name] = item
        if not optional:
            required.append(name)
    return {"kind": kind, "schema": {"type": "object", "properties": properties,
            "required": required, "additionalProperties": False}, **deepcopy(config)}


def profile(identifier, **values):
    return {"id": identifier, **deepcopy(values)}
