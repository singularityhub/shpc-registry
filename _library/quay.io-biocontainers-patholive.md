---
layout: container
name:  "quay.io/biocontainers/patholive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/patholive/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/patholive/container.yaml"
updated_at: "2022-10-29 05:53:47.350567"
latest: "1.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/patholive"
aliases:
 - "PathoLive.py"
 - "hilive"
 - "hilive-build"
 - "hilive-out"
 - "patholive"
 - "2to3-3.6"
 - "assistant"
 - "canbusutil"
 - "certutil"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
 - "dbus-send"
versions:
 - "1.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for patholive"
config: {"url": "https://biocontainers.pro/tools/patholive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for patholive", "latest": {"1.0--hdfd78af_1": "sha256:f7527475a1b1b7c3b792096fbd8d322fe111e28b6d99eb1aff3fe0497062efb2"}, "tags": {"1.0--hdfd78af_1": "sha256:f7527475a1b1b7c3b792096fbd8d322fe111e28b6d99eb1aff3fe0497062efb2"}, "docker": "quay.io/biocontainers/patholive", "aliases": {"PathoLive.py": "/usr/local/bin/PathoLive.py", "hilive": "/usr/local/bin/hilive", "hilive-build": "/usr/local/bin/hilive-build", "hilive-out": "/usr/local/bin/hilive-out", "patholive": "/usr/local/bin/patholive", "2to3-3.6": "/usr/local/bin/2to3-3.6", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/patholive.
shpc-registry automated BioContainers addition for patholive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/patholive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/patholive:1.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/patholive/1.0--hdfd78af_1
$ module help quay.io/biocontainers/patholive/1.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### patholive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### patholive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### patholive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### patholive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### patholive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### patholive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PathoLive.py

```bash
$ singularity exec <container> /usr/local/bin/PathoLive.py
$ podman run --it --rm --entrypoint /usr/local/bin/PathoLive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PathoLive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hilive

```bash
$ singularity exec <container> /usr/local/bin/hilive
$ podman run --it --rm --entrypoint /usr/local/bin/hilive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hilive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hilive-build

```bash
$ singularity exec <container> /usr/local/bin/hilive-build
$ podman run --it --rm --entrypoint /usr/local/bin/hilive-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hilive-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hilive-out

```bash
$ singularity exec <container> /usr/local/bin/hilive-out
$ podman run --it --rm --entrypoint /usr/local/bin/hilive-out   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hilive-out   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### patholive

```bash
$ singularity exec <container> /usr/local/bin/patholive
$ podman run --it --rm --entrypoint /usr/local/bin/patholive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/patholive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dbus-send

```bash
$ singularity exec <container> /usr/local/bin/dbus-send
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-send   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-send   -v ${PWD} -w ${PWD} <container> -c " $@"
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