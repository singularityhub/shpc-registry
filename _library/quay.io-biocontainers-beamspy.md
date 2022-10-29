---
layout: container
name:  "quay.io/biocontainers/beamspy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beamspy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/beamspy/container.yaml"
updated_at: "2022-10-29 05:50:23.804193"
latest: "1.1.0--py_0"
container_url: "https://biocontainers.pro/tools/beamspy"
aliases:
 - "beamspy"
 - "pyside2-lupdate"
 - "pyside2-rcc"
 - "pyside2-uic"
 - "pyside_tool.py"
 - "shiboken2"
 - "shiboken_tool.py"
 - "2to3-3.8"
 - "assistant"
 - "canbusutil"
 - "certutil"
 - "chardetect"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
versions:
 - "1.1.0--py_0"
description: "shpc-registry automated BioContainers addition for beamspy"
config: {"url": "https://biocontainers.pro/tools/beamspy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for beamspy", "latest": {"1.1.0--py_0": "sha256:7fdf5784946dba81f2b58fe2750b8925cfe4dcf1201ff00bd7f600a47777374a"}, "tags": {"1.1.0--py_0": "sha256:7fdf5784946dba81f2b58fe2750b8925cfe4dcf1201ff00bd7f600a47777374a"}, "docker": "quay.io/biocontainers/beamspy", "aliases": {"beamspy": "/usr/local/bin/beamspy", "pyside2-lupdate": "/usr/local/bin/pyside2-lupdate", "pyside2-rcc": "/usr/local/bin/pyside2-rcc", "pyside2-uic": "/usr/local/bin/pyside2-uic", "pyside_tool.py": "/usr/local/bin/pyside_tool.py", "shiboken2": "/usr/local/bin/shiboken2", "shiboken_tool.py": "/usr/local/bin/shiboken_tool.py", "2to3-3.8": "/usr/local/bin/2to3-3.8", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "chardetect": "/usr/local/bin/chardetect", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/beamspy.
shpc-registry automated BioContainers addition for beamspy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beamspy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beamspy:1.1.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beamspy/1.1.0--py_0
$ module help quay.io/biocontainers/beamspy/1.1.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beamspy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beamspy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beamspy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beamspy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beamspy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beamspy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beamspy

```bash
$ singularity exec <container> /usr/local/bin/beamspy
$ podman run --it --rm --entrypoint /usr/local/bin/beamspy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beamspy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside2-lupdate

```bash
$ singularity exec <container> /usr/local/bin/pyside2-lupdate
$ podman run --it --rm --entrypoint /usr/local/bin/pyside2-lupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside2-lupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside2-rcc

```bash
$ singularity exec <container> /usr/local/bin/pyside2-rcc
$ podman run --it --rm --entrypoint /usr/local/bin/pyside2-rcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside2-rcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside2-uic

```bash
$ singularity exec <container> /usr/local/bin/pyside2-uic
$ podman run --it --rm --entrypoint /usr/local/bin/pyside2-uic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside2-uic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside_tool.py

```bash
$ singularity exec <container> /usr/local/bin/pyside_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyside_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiboken2

```bash
$ singularity exec <container> /usr/local/bin/shiboken2
$ podman run --it --rm --entrypoint /usr/local/bin/shiboken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiboken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiboken_tool.py

```bash
$ singularity exec <container> /usr/local/bin/shiboken_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/shiboken_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiboken_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-cleanup-sockets

```bash
$ singularity exec <container> /usr/local/bin/dbus-cleanup-sockets
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-daemon

```bash
$ singularity exec <container> /usr/local/bin/dbus-daemon
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-launch

```bash
$ singularity exec <container> /usr/local/bin/dbus-launch
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-monitor

```bash
$ singularity exec <container> /usr/local/bin/dbus-monitor
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-run-session

```bash
$ singularity exec <container> /usr/local/bin/dbus-run-session
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-run-session   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-run-session   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)