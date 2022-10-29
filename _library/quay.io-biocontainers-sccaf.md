---
layout: container
name:  "quay.io/biocontainers/sccaf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sccaf/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sccaf/container.yaml"
updated_at: "2022-10-29 05:52:37.681496"
latest: "0.0.9--py_0"
container_url: "https://biocontainers.pro/tools/sccaf"
aliases:
 - "sccaf"
 - "sccaf-assess"
 - "sccaf-assess-merger"
 - "sccaf-regress-out"
 - "2to3-3.7"
 - "assistant"
 - "canbusutil"
 - "certutil"
 - "compile-et.pl"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
versions:
 - "0.0.9--py_0"
description: "shpc-registry automated BioContainers addition for sccaf"
config: {"url": "https://biocontainers.pro/tools/sccaf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sccaf", "latest": {"0.0.9--py_0": "sha256:a414e19efb731079c3d3e1b671a941b57ebe58f21179fc3a54b1acf9abc33d56"}, "tags": {"0.0.9--py_0": "sha256:a414e19efb731079c3d3e1b671a941b57ebe58f21179fc3a54b1acf9abc33d56"}, "docker": "quay.io/biocontainers/sccaf", "aliases": {"sccaf": "/usr/local/bin/sccaf", "sccaf-assess": "/usr/local/bin/sccaf-assess", "sccaf-assess-merger": "/usr/local/bin/sccaf-assess-merger", "sccaf-regress-out": "/usr/local/bin/sccaf-regress-out", "2to3-3.7": "/usr/local/bin/2to3-3.7", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "compile-et.pl": "/usr/local/bin/compile-et.pl", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sccaf.
shpc-registry automated BioContainers addition for sccaf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sccaf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sccaf:0.0.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sccaf/0.0.9--py_0
$ module help quay.io/biocontainers/sccaf/0.0.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sccaf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sccaf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sccaf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sccaf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sccaf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sccaf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sccaf

```bash
$ singularity exec <container> /usr/local/bin/sccaf
$ podman run --it --rm --entrypoint /usr/local/bin/sccaf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sccaf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sccaf-assess

```bash
$ singularity exec <container> /usr/local/bin/sccaf-assess
$ podman run --it --rm --entrypoint /usr/local/bin/sccaf-assess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sccaf-assess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sccaf-assess-merger

```bash
$ singularity exec <container> /usr/local/bin/sccaf-assess-merger
$ podman run --it --rm --entrypoint /usr/local/bin/sccaf-assess-merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sccaf-assess-merger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sccaf-regress-out

```bash
$ singularity exec <container> /usr/local/bin/sccaf-regress-out
$ podman run --it --rm --entrypoint /usr/local/bin/sccaf-regress-out   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sccaf-regress-out   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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