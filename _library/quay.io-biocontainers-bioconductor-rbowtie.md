---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbowtie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbowtie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbowtie/container.yaml"
updated_at: "2025-08-30 03:13:49.414052"
latest: "1.46.0--r44h77050f0_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rbowtie"

versions:
 - "1.34.0--r41hc247a5b_2"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hf17093f_2"
 - "1.40.0--r43hf17093f_0"
 - "1.42.0--r43hf17093f_0"
 - "1.46.0--r44h77050f0_0"
 - "1.46.0--r44h77050f0_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rbowtie"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbowtie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbowtie", "latest": {"1.46.0--r44h77050f0_1": "sha256:e666ffc103addd8b8d2c87b1497bb24ac2b46b356dd2ebf7e7da13fcb095cd4e"}, "tags": {"1.34.0--r41hc247a5b_2": "sha256:a469cf2c0dec56cee3d3af3ff11472b92335fd8a15d9f0290e571bc66c4794e6", "1.38.0--r42hc247a5b_0": "sha256:49f957bbdde1fc9aad2cc37cbca44d1ebf102e42c6a6388126276672c01c3973", "1.38.0--r42hf17093f_2": "sha256:e677addbe774d99e8b762cc68c099d8e4a7f1043de3365ea8609ca15052564f4", "1.40.0--r43hf17093f_0": "sha256:558e5e8f8f7a4e683ac214e6fde35635c84ab02715c55676647c5c7ad5a5c061", "1.42.0--r43hf17093f_0": "sha256:a4d2c213630c99299a2dbf970c2b6fcc4f2755077c6eee3e679524e0c60b9783", "1.46.0--r44h77050f0_0": "sha256:00d2e070559c639bb6b43457a73c78d5b3fbc26a63ff11ab253a9b61d18b9209", "1.46.0--r44h77050f0_1": "sha256:e666ffc103addd8b8d2c87b1497bb24ac2b46b356dd2ebf7e7da13fcb095cd4e"}, "docker": "quay.io/biocontainers/bioconductor-rbowtie"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbowtie.
shpc-registry automated BioContainers addition for bioconductor-rbowtie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbowtie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbowtie:1.46.0--r44h77050f0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbowtie/1.46.0--r44h77050f0_1
$ module help quay.io/biocontainers/bioconductor-rbowtie/1.46.0--r44h77050f0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbowtie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbowtie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbowtie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbowtie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbowtie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbowtie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbowtie

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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