---
layout: container
name:  "quay.io/biocontainers/bioconductor-ag.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ag.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ag.db/container.yaml"
updated_at: "2025-05-01 03:27:11.367720"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-ag.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_8"
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-ag.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ag.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ag.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:5d62d8ca078773755f3a3bf9362f0b54332b19fd26e65e0e9e7477c0cfa33d98"}, "tags": {"3.2.3--r41hdfd78af_8": "sha256:12ebf86065b97cab40d1eeb1a0676343e9d74d1a3040564b8b681ccd2bf270da", "3.13.0--r41hdfd78af_1": "sha256:f7efee704a28d7bd79199028b3f75d4ed307b9d9a1170b7338574f7a77d61f51", "3.13.0--r42hdfd78af_2": "sha256:b18345045b887e3f646db3732cfdea3d6c19fbfbffb0b4b246ee8b669490fdfb", "3.13.0--r43hdfd78af_3": "sha256:5532a7ccbbb91a136023ef799c8f5d5933e2bde16f4a6893aa1e695d21b45010", "3.13.0--r43hdfd78af_4": "sha256:32a8f5125efe01fbe75560f41768d2895c6f889c866065cfc61711d650a4beef", "3.13.0--r44hdfd78af_5": "sha256:5d62d8ca078773755f3a3bf9362f0b54332b19fd26e65e0e9e7477c0cfa33d98"}, "docker": "quay.io/biocontainers/bioconductor-ag.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ag.db.
shpc-registry automated BioContainers addition for bioconductor-ag.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ag.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ag.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ag.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-ag.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ag.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ag.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ag.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ag.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ag.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ag.db-inspect-deffile:

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