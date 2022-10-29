---
layout: container
name:  "quay.io/biocontainers/cogent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cogent/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cogent/container.yaml"
updated_at: "2022-10-29 05:39:26.005280"
latest: "1.9--py27h9801fc8_4"
container_url: "https://biocontainers.pro/tools/cogent"
aliases:
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
 - "1.9--py27h9801fc8_4"
description: "shpc-registry automated BioContainers addition for cogent"
config: {"url": "https://biocontainers.pro/tools/cogent", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cogent", "latest": {"1.9--py27h9801fc8_4": "sha256:679dd3174a77952fa28dce4bfe36a957b81f37b69638df82fef702bd14b89839"}, "tags": {"1.9--py27h9801fc8_4": "sha256:679dd3174a77952fa28dce4bfe36a957b81f37b69638df82fef702bd14b89839"}, "docker": "quay.io/biocontainers/cogent", "aliases": {"assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send", "dbus-test-tool": "/usr/local/bin/dbus-test-tool", "dbus-update-activation-environment": "/usr/local/bin/dbus-update-activation-environment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cogent.
shpc-registry automated BioContainers addition for cogent
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cogent
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cogent:1.9--py27h9801fc8_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cogent/1.9--py27h9801fc8_4
$ module help quay.io/biocontainers/cogent/1.9--py27h9801fc8_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cogent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cogent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cogent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cogent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cogent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cogent-inspect-deffile:

```bash
$ singularity inspect -d <container>
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