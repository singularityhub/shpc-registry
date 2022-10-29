---
layout: container
name:  "quay.io/biocontainers/cirtap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cirtap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cirtap/container.yaml"
updated_at: "2022-10-29 05:59:21.108613"
latest: "0.3.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/cirtap"
aliases:
 - "cirtap"
 - "2to3-3.10"
 - "aserver"
 - "assistant"
 - "canbusutil"
 - "certutil"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
versions:
 - "0.3.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for cirtap"
config: {"url": "https://biocontainers.pro/tools/cirtap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cirtap", "latest": {"0.3.1--pyh5e36f6f_0": "sha256:6e7579624bca8c95da6a0ce9ccb987d16fdd102d8f3340675725c0d7eb87d6c6"}, "tags": {"0.3.1--pyh5e36f6f_0": "sha256:6e7579624bca8c95da6a0ce9ccb987d16fdd102d8f3340675725c0d7eb87d6c6"}, "docker": "quay.io/biocontainers/cirtap", "aliases": {"cirtap": "/usr/local/bin/cirtap", "2to3-3.10": "/usr/local/bin/2to3-3.10", "aserver": "/usr/local/bin/aserver", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cirtap.
shpc-registry automated BioContainers addition for cirtap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cirtap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cirtap:0.3.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cirtap/0.3.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/cirtap/0.3.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cirtap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cirtap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cirtap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cirtap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cirtap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cirtap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cirtap

```bash
$ singularity exec <container> /usr/local/bin/cirtap
$ podman run --it --rm --entrypoint /usr/local/bin/cirtap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cirtap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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