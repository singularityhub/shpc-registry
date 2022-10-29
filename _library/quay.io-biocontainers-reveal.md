---
layout: container
name:  "quay.io/biocontainers/reveal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reveal/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/reveal/container.yaml"
updated_at: "2022-10-29 05:58:19.344492"
latest: "0.1--py27h95a95ce_7"
container_url: "https://biocontainers.pro/tools/reveal"
aliases:
 - "reveal"
 - "assistant"
 - "canbusutil"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
 - "dbus-send"
 - "dbus-test-tool"
 - "dbus-update-activation-environment"
versions:
 - "0.1--py27h95a95ce_7"
description: "shpc-registry automated BioContainers addition for reveal"
config: {"url": "https://biocontainers.pro/tools/reveal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for reveal", "latest": {"0.1--py27h95a95ce_7": "sha256:74ad2313518ece943c42f939e27b5bb1da0ea636836f1cc7ed6cc25e39b409d9"}, "tags": {"0.1--py27h95a95ce_7": "sha256:74ad2313518ece943c42f939e27b5bb1da0ea636836f1cc7ed6cc25e39b409d9"}, "docker": "quay.io/biocontainers/reveal", "aliases": {"reveal": "/usr/local/bin/reveal", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send", "dbus-test-tool": "/usr/local/bin/dbus-test-tool", "dbus-update-activation-environment": "/usr/local/bin/dbus-update-activation-environment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reveal.
shpc-registry automated BioContainers addition for reveal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reveal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reveal:0.1--py27h95a95ce_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reveal/0.1--py27h95a95ce_7
$ module help quay.io/biocontainers/reveal/0.1--py27h95a95ce_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reveal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reveal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reveal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reveal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reveal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reveal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### reveal

```bash
$ singularity exec <container> /usr/local/bin/reveal
$ podman run --it --rm --entrypoint /usr/local/bin/reveal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reveal   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dbus-test-tool

```bash
$ singularity exec <container> /usr/local/bin/dbus-test-tool
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-test-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-test-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-update-activation-environment

```bash
$ singularity exec <container> /usr/local/bin/dbus-update-activation-environment
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-update-activation-environment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-update-activation-environment   -v ${PWD} -w ${PWD} <container> -c " $@"
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