---
layout: container
name:  "quay.io/biocontainers/irep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irep/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/irep/container.yaml"
updated_at: "2022-10-29 05:38:51.140912"
latest: "1.1.7--pyh24bf2e0_1"
container_url: "https://biocontainers.pro/tools/irep"
aliases:
 - "bPTR"
 - "gc_skew"
 - "iRep"
 - "iRep_filter.py"
 - "2to3-3.6"
 - "assistant"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
 - "dbus-send"
 - "dbus-test-tool"
 - "dbus-update-activation-environment"
versions:
 - "1.1.7--pyh24bf2e0_1"
description: "shpc-registry automated BioContainers addition for irep"
config: {"url": "https://biocontainers.pro/tools/irep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irep", "latest": {"1.1.7--pyh24bf2e0_1": "sha256:b77c59abfb6b36891d609147246b17639b750ceddbadc54913f868e4dd524f59"}, "tags": {"1.1.7--pyh24bf2e0_1": "sha256:b77c59abfb6b36891d609147246b17639b750ceddbadc54913f868e4dd524f59"}, "docker": "quay.io/biocontainers/irep", "aliases": {"bPTR": "/usr/local/bin/bPTR", "gc_skew": "/usr/local/bin/gc_skew", "iRep": "/usr/local/bin/iRep", "iRep_filter.py": "/usr/local/bin/iRep_filter.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "assistant": "/usr/local/bin/assistant", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send", "dbus-test-tool": "/usr/local/bin/dbus-test-tool", "dbus-update-activation-environment": "/usr/local/bin/dbus-update-activation-environment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/irep.
shpc-registry automated BioContainers addition for irep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/irep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/irep:1.1.7--pyh24bf2e0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/irep/1.1.7--pyh24bf2e0_1
$ module help quay.io/biocontainers/irep/1.1.7--pyh24bf2e0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### irep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### irep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### irep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### irep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### irep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### irep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bPTR

```bash
$ singularity exec <container> /usr/local/bin/bPTR
$ podman run --it --rm --entrypoint /usr/local/bin/bPTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bPTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc_skew

```bash
$ singularity exec <container> /usr/local/bin/gc_skew
$ podman run --it --rm --entrypoint /usr/local/bin/gc_skew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc_skew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iRep

```bash
$ singularity exec <container> /usr/local/bin/iRep
$ podman run --it --rm --entrypoint /usr/local/bin/iRep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iRep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iRep_filter.py

```bash
$ singularity exec <container> /usr/local/bin/iRep_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/iRep_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iRep_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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