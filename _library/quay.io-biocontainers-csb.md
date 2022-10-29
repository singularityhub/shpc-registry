---
layout: container
name:  "quay.io/biocontainers/csb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/csb/container.yaml"
updated_at: "2022-10-29 05:55:30.419416"
latest: "1.2.5--pyh24bf2e0_2"
container_url: "https://biocontainers.pro/tools/csb"
aliases:
 - "csb-bfit"
 - "csb-bfite"
 - "csb-buildhmm"
 - "csb-csfrag"
 - "csb-embd"
 - "csb-hhfrag"
 - "csb-hhsearch"
 - "csb-precision"
 - "csb-promix"
 - "csb-test"
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
 - "1.2.5--pyh24bf2e0_2"
description: "shpc-registry automated BioContainers addition for csb"
config: {"url": "https://biocontainers.pro/tools/csb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for csb", "latest": {"1.2.5--pyh24bf2e0_2": "sha256:78eb0352517ed26a0055570aa2e1f900b7086084b42e92b13ad76c2774101f5e"}, "tags": {"1.2.5--pyh24bf2e0_2": "sha256:78eb0352517ed26a0055570aa2e1f900b7086084b42e92b13ad76c2774101f5e"}, "docker": "quay.io/biocontainers/csb", "aliases": {"csb-bfit": "/usr/local/bin/csb-bfit", "csb-bfite": "/usr/local/bin/csb-bfite", "csb-buildhmm": "/usr/local/bin/csb-buildhmm", "csb-csfrag": "/usr/local/bin/csb-csfrag", "csb-embd": "/usr/local/bin/csb-embd", "csb-hhfrag": "/usr/local/bin/csb-hhfrag", "csb-hhsearch": "/usr/local/bin/csb-hhsearch", "csb-precision": "/usr/local/bin/csb-precision", "csb-promix": "/usr/local/bin/csb-promix", "csb-test": "/usr/local/bin/csb-test", "2to3-3.6": "/usr/local/bin/2to3-3.6", "assistant": "/usr/local/bin/assistant", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send", "dbus-test-tool": "/usr/local/bin/dbus-test-tool", "dbus-update-activation-environment": "/usr/local/bin/dbus-update-activation-environment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csb.
shpc-registry automated BioContainers addition for csb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csb:1.2.5--pyh24bf2e0_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csb/1.2.5--pyh24bf2e0_2
$ module help quay.io/biocontainers/csb/1.2.5--pyh24bf2e0_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csb-bfit

```bash
$ singularity exec <container> /usr/local/bin/csb-bfit
$ podman run --it --rm --entrypoint /usr/local/bin/csb-bfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-bfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-bfite

```bash
$ singularity exec <container> /usr/local/bin/csb-bfite
$ podman run --it --rm --entrypoint /usr/local/bin/csb-bfite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-bfite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-buildhmm

```bash
$ singularity exec <container> /usr/local/bin/csb-buildhmm
$ podman run --it --rm --entrypoint /usr/local/bin/csb-buildhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-buildhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-csfrag

```bash
$ singularity exec <container> /usr/local/bin/csb-csfrag
$ podman run --it --rm --entrypoint /usr/local/bin/csb-csfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-csfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-embd

```bash
$ singularity exec <container> /usr/local/bin/csb-embd
$ podman run --it --rm --entrypoint /usr/local/bin/csb-embd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-embd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-hhfrag

```bash
$ singularity exec <container> /usr/local/bin/csb-hhfrag
$ podman run --it --rm --entrypoint /usr/local/bin/csb-hhfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-hhfrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-hhsearch

```bash
$ singularity exec <container> /usr/local/bin/csb-hhsearch
$ podman run --it --rm --entrypoint /usr/local/bin/csb-hhsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-hhsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-precision

```bash
$ singularity exec <container> /usr/local/bin/csb-precision
$ podman run --it --rm --entrypoint /usr/local/bin/csb-precision   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-precision   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-promix

```bash
$ singularity exec <container> /usr/local/bin/csb-promix
$ podman run --it --rm --entrypoint /usr/local/bin/csb-promix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-promix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csb-test

```bash
$ singularity exec <container> /usr/local/bin/csb-test
$ podman run --it --rm --entrypoint /usr/local/bin/csb-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csb-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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