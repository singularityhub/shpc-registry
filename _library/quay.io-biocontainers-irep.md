---
layout: container
name:  "quay.io/biocontainers/irep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/irep/container.yaml"
updated_at: "2023-08-21 02:35:38.906315"
latest: "1.1.7--pyh24bf2e0_1"
container_url: "https://biocontainers.pro/tools/irep"
aliases:
 - "bPTR"
 - "gc_skew"
 - "iRep"
 - "iRep_filter.py"
 - "qhelpconverter"
 - "pylupdate5"
 - "pyrcc5"
 - "pyuic5"
 - "sip"
 - "qdoc"
 - "gst-device-monitor-1.0"
 - "gst-discoverer-1.0"
 - "gst-play-1.0"
 - "fixqt4headers.pl"
versions:
 - "1.1.7--pyh24bf2e0_1"
description: "shpc-registry automated BioContainers addition for irep"
config: {"url": "https://biocontainers.pro/tools/irep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irep", "latest": {"1.1.7--pyh24bf2e0_1": "sha256:b77c59abfb6b36891d609147246b17639b750ceddbadc54913f868e4dd524f59"}, "tags": {"1.1.7--pyh24bf2e0_1": "sha256:b77c59abfb6b36891d609147246b17639b750ceddbadc54913f868e4dd524f59"}, "docker": "quay.io/biocontainers/irep", "aliases": {"bPTR": "/usr/local/bin/bPTR", "gc_skew": "/usr/local/bin/gc_skew", "iRep": "/usr/local/bin/iRep", "iRep_filter.py": "/usr/local/bin/iRep_filter.py", "qhelpconverter": "/usr/local/bin/qhelpconverter", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5", "pyuic5": "/usr/local/bin/pyuic5", "sip": "/usr/local/bin/sip", "qdoc": "/usr/local/bin/qdoc", "gst-device-monitor-1.0": "/usr/local/bin/gst-device-monitor-1.0", "gst-discoverer-1.0": "/usr/local/bin/gst-discoverer-1.0", "gst-play-1.0": "/usr/local/bin/gst-play-1.0", "fixqt4headers.pl": "/usr/local/bin/fixqt4headers.pl"}}
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


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylupdate5

```bash
$ singularity exec <container> /usr/local/bin/pylupdate5
$ podman run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrcc5

```bash
$ singularity exec <container> /usr/local/bin/pyrcc5
$ podman run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyuic5

```bash
$ singularity exec <container> /usr/local/bin/pyuic5
$ podman run --it --rm --entrypoint /usr/local/bin/pyuic5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyuic5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip

```bash
$ singularity exec <container> /usr/local/bin/sip
$ podman run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdoc

```bash
$ singularity exec <container> /usr/local/bin/qdoc
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-device-monitor-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-device-monitor-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-discoverer-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-discoverer-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-play-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-play-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fixqt4headers.pl

```bash
$ singularity exec <container> /usr/local/bin/fixqt4headers.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fixqt4headers.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixqt4headers.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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