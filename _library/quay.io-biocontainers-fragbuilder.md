---
layout: container
name:  "quay.io/biocontainers/fragbuilder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fragbuilder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fragbuilder/container.yaml"
updated_at: "2024-08-10 03:12:28.467829"
latest: "1.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/fragbuilder"
aliases:
 - "babel"
 - "obchiral"
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
 - "1.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for fragbuilder"
config: {"url": "https://biocontainers.pro/tools/fragbuilder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fragbuilder", "latest": {"1.0.1--hdfd78af_1": "sha256:08abce9d04d2fc67fc65a80013cbd702fd7d06284d6af53381158dc9c7a59390"}, "tags": {"1.0.1--hdfd78af_1": "sha256:08abce9d04d2fc67fc65a80013cbd702fd7d06284d6af53381158dc9c7a59390"}, "docker": "quay.io/biocontainers/fragbuilder", "aliases": {"babel": "/usr/local/bin/babel", "obchiral": "/usr/local/bin/obchiral", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fragbuilder.
shpc-registry automated BioContainers addition for fragbuilder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fragbuilder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fragbuilder:1.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fragbuilder/1.0.1--hdfd78af_1
$ module help quay.io/biocontainers/fragbuilder/1.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fragbuilder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fragbuilder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fragbuilder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fragbuilder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fragbuilder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fragbuilder-inspect-deffile:

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