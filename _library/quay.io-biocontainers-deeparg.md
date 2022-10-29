---
layout: container
name:  "quay.io/biocontainers/deeparg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeparg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deeparg/container.yaml"
updated_at: "2022-10-29 05:49:04.212996"
latest: "1.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/deeparg"
aliases:
 - "deeparg"
 - "theano-test"
 - "assistant"
 - "canbusutil"
 - "chardetect"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
 - "dbus-send"
 - "dbus-test-tool"
versions:
 - "1.0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for deeparg"
config: {"url": "https://biocontainers.pro/tools/deeparg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deeparg", "latest": {"1.0.2--pyhdfd78af_1": "sha256:e832b2c8217b058b9fba5bd61be0c87f03721464bfb7bc7025ed100414b974bf"}, "tags": {"1.0.2--pyhdfd78af_1": "sha256:e832b2c8217b058b9fba5bd61be0c87f03721464bfb7bc7025ed100414b974bf"}, "docker": "quay.io/biocontainers/deeparg", "aliases": {"deeparg": "/usr/local/bin/deeparg", "theano-test": "/usr/local/bin/theano-test", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "chardetect": "/usr/local/bin/chardetect", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send", "dbus-test-tool": "/usr/local/bin/dbus-test-tool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeparg.
shpc-registry automated BioContainers addition for deeparg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeparg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeparg:1.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeparg/1.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/deeparg/1.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deeparg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deeparg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deeparg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deeparg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deeparg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deeparg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deeparg

```bash
$ singularity exec <container> /usr/local/bin/deeparg
$ podman run --it --rm --entrypoint /usr/local/bin/deeparg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deeparg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-test

```bash
$ singularity exec <container> /usr/local/bin/theano-test
$ podman run --it --rm --entrypoint /usr/local/bin/theano-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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