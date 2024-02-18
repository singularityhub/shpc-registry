---
layout: container
name:  "quay.io/biocontainers/bioconductor-hom.hs.inp.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hom.hs.inp.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hom.hs.inp.db/container.yaml"
updated_at: "2024-02-18 02:31:55.643671"
latest: "3.1.3--r40hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-hom.hs.inp.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.1.3--r40hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-hom.hs.inp.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hom.hs.inp.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hom.hs.inp.db", "latest": {"3.1.3--r40hdfd78af_2": "sha256:ffc3e6306156017c03f1ee1fbe835c3744f401a2fb76855eff3efc3774267883"}, "tags": {"3.1.3--r40hdfd78af_2": "sha256:ffc3e6306156017c03f1ee1fbe835c3744f401a2fb76855eff3efc3774267883"}, "docker": "quay.io/biocontainers/bioconductor-hom.hs.inp.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hom.hs.inp.db.
shpc-registry automated BioContainers addition for bioconductor-hom.hs.inp.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hom.hs.inp.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hom.hs.inp.db:3.1.3--r40hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hom.hs.inp.db/3.1.3--r40hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-hom.hs.inp.db/3.1.3--r40hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hom.hs.inp.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hom.hs.inp.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hom.hs.inp.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hom.hs.inp.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hom.hs.inp.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hom.hs.inp.db-inspect-deffile:

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