---
layout: container
name:  "quay.io/biocontainers/genepop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genepop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genepop/container.yaml"
updated_at: "2024-06-27 03:32:35.139474"
latest: "4.6--0"
container_url: "https://biocontainers.pro/tools/genepop"
aliases:
 - "Genepop"
versions:
 - "4.6--0"
description: "shpc-registry automated BioContainers addition for genepop"
config: {"url": "https://biocontainers.pro/tools/genepop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genepop", "latest": {"4.6--0": "sha256:9dee578651fa195029ccff712e8fb63835bdfd20e3135dd3125e21b662082cb4"}, "tags": {"4.6--0": "sha256:9dee578651fa195029ccff712e8fb63835bdfd20e3135dd3125e21b662082cb4"}, "docker": "quay.io/biocontainers/genepop", "aliases": {"Genepop": "/usr/local/bin/Genepop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genepop.
shpc-registry automated BioContainers addition for genepop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genepop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genepop:4.6--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genepop/4.6--0
$ module help quay.io/biocontainers/genepop/4.6--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genepop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genepop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genepop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genepop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genepop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genepop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Genepop

```bash
$ singularity exec <container> /usr/local/bin/Genepop
$ podman run --it --rm --entrypoint /usr/local/bin/Genepop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Genepop   -v ${PWD} -w ${PWD} <container> -c " $@"
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