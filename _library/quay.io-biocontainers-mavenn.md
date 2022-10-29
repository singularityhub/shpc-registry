---
layout: container
name:  "quay.io/biocontainers/mavenn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mavenn/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mavenn/container.yaml"
updated_at: "2022-10-29 05:48:59.866496"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mavenn"
aliases:
 - "2to3-3.9"
 - "aserver"
 - "assistant"
 - "brotli"
 - "canbusutil"
 - "certutil"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
versions:
 - "1.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mavenn"
config: {"url": "https://biocontainers.pro/tools/mavenn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mavenn", "latest": {"1.0.0--pyhdfd78af_0": "sha256:1a6c4096483e08490985db1aadeec22d4041688f76a9a4ad86a4585f7465785a"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:1a6c4096483e08490985db1aadeec22d4041688f76a9a4ad86a4585f7465785a"}, "docker": "quay.io/biocontainers/mavenn", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "aserver": "/usr/local/bin/aserver", "assistant": "/usr/local/bin/assistant", "brotli": "/usr/local/bin/brotli", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mavenn.
shpc-registry automated BioContainers addition for mavenn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mavenn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mavenn:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mavenn/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/mavenn/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mavenn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mavenn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mavenn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mavenn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mavenn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mavenn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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