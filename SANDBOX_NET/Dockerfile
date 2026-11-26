# The "internet" sandbox: the computer sandbox's image (SANDBOX_PC/Dockerfile, built as local/argus-pc:desktop: a
# display, a desktop, tools, game libraries) with another proxy program. Built by `python3.11 SANDBOX_NET/sandbox.py build`.
#
# The sandbox itself stays on an internal network, as in every folder (the locked sandbox script checks it). What
# leaves goes through the proxy container the script starts beside it for network "allowlist", and that container
# runs /opt/sandbox/proxy.py of this image: here proxy_open.py, which lets HTTP and HTTPS through to any PUBLIC
# address when the allowlist names "open.internet" (settings.json), and to no private one.
ARG BASE_IMAGE=local/argus-pc:desktop
FROM ${BASE_IMAGE}
ARG LLM_PACKAGES=0
USER root
RUN cp /opt/sandbox/proxy.py /opt/sandbox/proxy_allowlist.py
COPY proxy_open.py /opt/sandbox/proxy.py
RUN chmod 0444 /opt/sandbox/proxy.py /opt/sandbox/proxy_allowlist.py

# What the agent reaches for and did not find (2026-11-23, its first turns here): tools/ as commands.
# - apply_patch: the "*** Begin Patch" format gpt-oss writes files with. Panda3D's wheel installs a program of the same
#   name (its own binary patches); that one is kept as panda3d-apply-patch.
# - websearch, webread, wiki: the web as text, a part at a time (a model that reads text cannot "look at" a page, and
#   a command's output is kept from its end: curl of a long page shows its footer).
# - gui-run: a window program started in the background, with a report of its window or of why it ended.
# - gui-look: the screen in words (flat color or which colors and where, moving or not): the agent reads text, and it
#   answered that a gray, empty window showed a blue scene with a cube.
# - sandbox-info: what is here, looked at now.
# In /usr/local/bin, which a login shell (`bash -lc`) keeps in its PATH; root's and read-only like the rest of the image.
COPY tools/ /opt/tools/
RUN set -eu; \
    if [ -e /usr/local/bin/apply_patch ] && [ ! -L /usr/local/bin/apply_patch ]; then \
        mv /usr/local/bin/apply_patch /usr/local/bin/panda3d-apply-patch; fi; \
    for tool in apply_patch websearch webread wiki gui-run gui-look sandbox-info; do \
        chmod 0555 "/opt/tools/$tool"; ln -sf "/opt/tools/$tool" "/usr/local/bin/$tool"; done; \
    chmod 0444 /opt/tools/argus_web.py /opt/tools/argus_screen.py /opt/tools/profile.sh; \
    install -m 0444 /opt/tools/profile.sh /etc/profile.d/zz-argus-path.sh; \
    install -m 0444 /opt/tools/asound.conf /etc/asound.conf; \
    python3 -I -m py_compile /opt/tools/argus_web.py /opt/tools/argus_screen.py; \
    for tool in apply_patch websearch webread wiki gui-run gui-look sandbox-info; do "$tool" --help >/dev/null; done
# (after the system's folders: a program of the image is never replaced by a file in /workspace)
ENV PATH="${PATH}:/workspace/.home/.local/bin"
# pip keeps what it downloads in /workspace/.cache/pip (the locked sandbox's setting), and sandbox.py copies /workspace
# before every command: one 53 MB wheel made every copy 52 MB (2.4 GB in an afternoon). Here pip keeps no downloads.
ENV PIP_NO_CACHE_DIR=1
USER 10001:10001
WORKDIR /workspace
