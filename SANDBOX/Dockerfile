ARG BASE_IMAGE=python:3.11-slim-bookworm
FROM ${BASE_IMAGE}
ARG LLM_PACKAGES=0
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash ca-certificates coreutils curl git procps tar \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements-llm.txt /opt/sandbox/
RUN python -m pip install --no-cache-dir -r /opt/sandbox/requirements.txt \
    && if [ "$LLM_PACKAGES" = "1" ]; then python -m pip install --no-cache-dir -r /opt/sandbox/requirements-llm.txt; fi \
    && python -m pip freeze > /opt/sandbox/environment.lock
RUN groupadd --gid 10001 sandbox && useradd --uid 10001 --gid 10001 --no-create-home sandbox \
    && mkdir -p /workspace /models /opt/sandbox \
    && chown 10001:10001 /workspace
COPY entrypoint.sh proxy.py /opt/sandbox/
RUN chmod 0555 /opt/sandbox/entrypoint.sh && chmod 0444 /opt/sandbox/proxy.py
USER 10001:10001
WORKDIR /workspace
ENV HOME=/workspace/.home PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 \
    XDG_CACHE_HOME=/workspace/.cache PIP_CACHE_DIR=/workspace/.cache/pip \
    HF_HOME=/workspace/.cache/huggingface HF_HUB_OFFLINE=1 \
    TORCHINDUCTOR_CACHE_DIR=/workspace/.cache/torchinductor TRITON_CACHE_DIR=/workspace/.cache/triton
ENTRYPOINT ["/opt/sandbox/entrypoint.sh"]
CMD ["sleep", "infinity"]
