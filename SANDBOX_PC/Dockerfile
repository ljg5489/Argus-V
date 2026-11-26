# The everyday "computer" sandbox: the locked sandbox image (SANDBOX/Dockerfile, built as local/generic-sandbox:python:
# python 3.11, bash, coreutils, curl, git, procps, tar, user 10001) with a display, a small desktop, the tools a
# person reaches for and the Python libraries a first game needs. Built by `python3.11 SANDBOX_PC/sandbox.py build`.
ARG BASE_IMAGE=local/generic-sandbox:python
FROM ${BASE_IMAGE}
ARG LLM_PACKAGES=0
USER root
# - the display: an X server that draws into memory (Xvfb), a window manager, a bar, a terminal, a file manager, a
#   text editor; OpenGL drawn by the CPU (Mesa llvmpipe: no graphics card is given to the sandbox);
# - Korean text on the screen (fonts-nanum);
# - the tools.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        xvfb x11-xserver-utils x11-utils x11-xkb-utils dbus-x11 \
        openbox tint2 lxterminal pcmanfm l3afpad lxde-icon-theme \
        libgl1 libgl1-mesa-dri libglx-mesa0 libegl1 libglu1-mesa mesa-utils libopenal1 \
        fonts-nanum fonts-dejavu-core \
        tree vim nano less htop zip unzip file wget jq bc rsync sqlite3 \
    && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --no-cache-dir panda3d pygame numpy pillow python-xlib matplotlib requests \
    && python -m pip freeze > /opt/sandbox/environment.lock
COPY desktop/ /opt/desktop/
RUN chmod -R a+rX /opt/desktop && chmod 0555 /opt/desktop/start.sh /opt/desktop/stop.sh && fc-cache -f
USER 10001:10001
WORKDIR /workspace
ENV LANG=C.UTF-8 LIBGL_ALWAYS_SOFTWARE=1 GALLIUM_DRIVER=llvmpipe LP_NUM_THREADS=2 SDL_AUDIODRIVER=dummy
