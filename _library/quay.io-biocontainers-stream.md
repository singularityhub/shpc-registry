---
layout: container
name:  "quay.io/biocontainers/stream"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stream/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stream/container.yaml"
updated_at: "2022-10-29 05:56:22.077886"
latest: "0.4.0--py37r36hc99cbb1_0"
container_url: "https://biocontainers.pro/tools/stream"
aliases:
 - "gunicorn"
 - "slugify"
 - "stream_run_test"
 - "2to3-3.7"
 - "assistant"
 - "c89"
 - "c99"
 - "canbusutil"
 - "curve_keygen"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
versions:
 - "0.4.0--py37r36hc99cbb1_0"
description: "shpc-registry automated BioContainers addition for stream"
config: {"url": "https://biocontainers.pro/tools/stream", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stream", "latest": {"0.4.0--py37r36hc99cbb1_0": "sha256:59ebb094505a21d0fe38825be15c968aeda821dc94bc924080cf799e3a420f0a"}, "tags": {"0.4.0--py37r36hc99cbb1_0": "sha256:59ebb094505a21d0fe38825be15c968aeda821dc94bc924080cf799e3a420f0a"}, "docker": "quay.io/biocontainers/stream", "aliases": {"gunicorn": "/usr/local/bin/gunicorn", "slugify": "/usr/local/bin/slugify", "stream_run_test": "/usr/local/bin/stream_run_test", "2to3-3.7": "/usr/local/bin/2to3-3.7", "assistant": "/usr/local/bin/assistant", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99", "canbusutil": "/usr/local/bin/canbusutil", "curve_keygen": "/usr/local/bin/curve_keygen", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stream.
shpc-registry automated BioContainers addition for stream
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stream
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stream:0.4.0--py37r36hc99cbb1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stream/0.4.0--py37r36hc99cbb1_0
$ module help quay.io/biocontainers/stream/0.4.0--py37r36hc99cbb1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stream-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stream-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stream-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stream-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stream-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stream-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gunicorn

```bash
$ singularity exec <container> /usr/local/bin/gunicorn
$ podman run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stream_run_test

```bash
$ singularity exec <container> /usr/local/bin/stream_run_test
$ podman run --it --rm --entrypoint /usr/local/bin/stream_run_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stream_run_test   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
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