---
layout: container
name:  "quay.io/biocontainers/strip_it"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strip_it/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strip_it/container.yaml"
updated_at: "2023-03-14 03:33:11.635928"
latest: "1.0.2--h7d875b9_6"
container_url: "https://biocontainers.pro/tools/strip_it"
aliases:
 - "babel"
 - "obchiral"
 - "strip-it"
 - "obabel"
 - "obconformer"
 - "obdistgen"
 - "obenergy"
 - "obfit"
 - "obgen"
 - "obgrep"
 - "obminimize"
 - "obprobe"
 - "obprop"
versions:
 - "1.0.2--h7d875b9_6"
description: "shpc-registry automated BioContainers addition for strip_it"
config: {"url": "https://biocontainers.pro/tools/strip_it", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strip_it", "latest": {"1.0.2--h7d875b9_6": "sha256:13b913ecec336a08d465a3c52c50c0d05fae824cef0f4f5b06af8f6e2d8570f4"}, "tags": {"1.0.2--h7d875b9_6": "sha256:13b913ecec336a08d465a3c52c50c0d05fae824cef0f4f5b06af8f6e2d8570f4"}, "docker": "quay.io/biocontainers/strip_it", "aliases": {"babel": "/usr/local/bin/babel", "obchiral": "/usr/local/bin/obchiral", "strip-it": "/usr/local/bin/strip-it", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strip_it.
shpc-registry automated BioContainers addition for strip_it
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strip_it
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strip_it:1.0.2--h7d875b9_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strip_it/1.0.2--h7d875b9_6
$ module help quay.io/biocontainers/strip_it/1.0.2--h7d875b9_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strip_it-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strip_it-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strip_it-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strip_it-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strip_it-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strip_it-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### babel

```bash
$ singularity exec <container> /usr/local/bin/babel
$ podman run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obchiral

```bash
$ singularity exec <container> /usr/local/bin/obchiral
$ podman run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip-it

```bash
$ singularity exec <container> /usr/local/bin/strip-it
$ podman run --it --rm --entrypoint /usr/local/bin/strip-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obabel

```bash
$ singularity exec <container> /usr/local/bin/obabel
$ podman run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obconformer

```bash
$ singularity exec <container> /usr/local/bin/obconformer
$ podman run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obdistgen

```bash
$ singularity exec <container> /usr/local/bin/obdistgen
$ podman run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obenergy

```bash
$ singularity exec <container> /usr/local/bin/obenergy
$ podman run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfit

```bash
$ singularity exec <container> /usr/local/bin/obfit
$ podman run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgen

```bash
$ singularity exec <container> /usr/local/bin/obgen
$ podman run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgrep

```bash
$ singularity exec <container> /usr/local/bin/obgrep
$ podman run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obminimize

```bash
$ singularity exec <container> /usr/local/bin/obminimize
$ podman run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprobe

```bash
$ singularity exec <container> /usr/local/bin/obprobe
$ podman run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprop

```bash
$ singularity exec <container> /usr/local/bin/obprop
$ podman run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
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