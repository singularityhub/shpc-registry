---
layout: container
name:  "quay.io/biocontainers/xpclr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xpclr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xpclr/container.yaml"
updated_at: "2023-09-15 03:04:36.255828"
latest: "1.1.2--py_0"
container_url: "https://biocontainers.pro/tools/xpclr"
aliases:
 - "xpclr"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "compile-et.pl"
 - "prerr.properties"
 - "bokeh"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
versions:
 - "1.1.2--py_0"
description: "shpc-registry automated BioContainers addition for xpclr"
config: {"url": "https://biocontainers.pro/tools/xpclr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xpclr", "latest": {"1.1.2--py_0": "sha256:0ba23d9d38f456697410db133663d7e20a09a5dd2aea805d8afc389611dcde99"}, "tags": {"1.1.2--py_0": "sha256:0ba23d9d38f456697410db133663d7e20a09a5dd2aea805d8afc389611dcde99"}, "docker": "quay.io/biocontainers/xpclr", "aliases": {"xpclr": "/usr/local/bin/xpclr", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "compile-et.pl": "/usr/local/bin/compile-et.pl", "prerr.properties": "/usr/local/bin/prerr.properties", "bokeh": "/usr/local/bin/bokeh", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xpclr.
shpc-registry automated BioContainers addition for xpclr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xpclr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xpclr:1.1.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xpclr/1.1.2--py_0
$ module help quay.io/biocontainers/xpclr/1.1.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xpclr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xpclr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xpclr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xpclr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xpclr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xpclr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xpclr

```bash
$ singularity exec <container> /usr/local/bin/xpclr
$ podman run --it --rm --entrypoint /usr/local/bin/xpclr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xpclr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerr.properties

```bash
$ singularity exec <container> /usr/local/bin/prerr.properties
$ podman run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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