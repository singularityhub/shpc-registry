---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene/container.yaml"
updated_at: "2024-04-07 02:29:12.080227"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg38.refgene"

versions:
 - "3.13.0--r41hdfd78af_2"
 - "3.15.0--r42hdfd78af_0"
 - "3.15.0--r43hdfd78af_1"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg38.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg38.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg38.refgene", "latest": {"3.18.0--r43hdfd78af_0": "sha256:e0e8043dc1c60b87b828578bb428ff8c24c71168c0b2ff8b77d781120b1e7da8"}, "tags": {"3.13.0--r41hdfd78af_2": "sha256:861e89ef1667c30f1a64d9c880b12fa09cb2bca78a08d22f26d351327154a71b", "3.15.0--r42hdfd78af_0": "sha256:b79dbbce19bce717dc33403f65aec07122d964117bde424e21cd7a3a75a365bc", "3.15.0--r43hdfd78af_1": "sha256:8c4c38b584f05b161f3a970c576b34db1e20ab55a72cfb93e57b4fe80e7201bb", "3.18.0--r43hdfd78af_0": "sha256:e0e8043dc1c60b87b828578bb428ff8c24c71168c0b2ff8b77d781120b1e7da8"}, "docker": "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg38.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.refgene/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.hsapiens.ucsc.hg38.refgene

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