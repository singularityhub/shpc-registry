---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74av2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74av2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74av2.db/container.yaml"
updated_at: "2024-08-24 03:24:13.492193"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74av2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74av2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74av2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74av2.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:b13f760f3b7c378894c4da33f11e2d25186d5be7f34c9b137557a51cc75c386f"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:7ea93c318b27c9c7efaf9c73665645339a90994cea2fafdc7688e2624a6ec854", "3.13.0--r42hdfd78af_2": "sha256:dde267eb6cae8c92082edb8811bb55b3bf31d58cab8b20fb4660cab9ff086233", "3.13.0--r43hdfd78af_3": "sha256:13ab9f6718f17ce33b522972b3d4980451c7e1bf402ef2e8cb7aaf4d0c3fa2e4", "3.13.0--r43hdfd78af_4": "sha256:b13f760f3b7c378894c4da33f11e2d25186d5be7f34c9b137557a51cc75c386f"}, "docker": "quay.io/biocontainers/bioconductor-mgu74av2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74av2.db.
shpc-registry automated BioContainers addition for bioconductor-mgu74av2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74av2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74av2.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74av2.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-mgu74av2.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74av2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74av2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74av2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74av2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74av2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74av2.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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