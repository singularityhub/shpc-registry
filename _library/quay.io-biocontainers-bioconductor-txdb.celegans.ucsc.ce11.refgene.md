---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene/container.yaml"
updated_at: "2025-11-26 03:51:17.859925"
latest: "3.4.6--r44hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.celegans.ucsc.ce11.refgene"

versions:
 - "3.4.6--r41hdfd78af_8"
 - "3.4.6--r42hdfd78af_9"
 - "3.4.6--r43hdfd78af_10"
 - "3.4.6--r43hdfd78af_11"
 - "3.4.6--r44hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce11.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.celegans.ucsc.ce11.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce11.refgene", "latest": {"3.4.6--r44hdfd78af_12": "sha256:d54e46aa46c76d8955d53622172e53c47de86d5458d01c4c754f7090ea8e94d5"}, "tags": {"3.4.6--r41hdfd78af_8": "sha256:7cf1187a5abff7dda1ad19db3a7f4b7df751c2774a4b3998c77b21f499d19a63", "3.4.6--r42hdfd78af_9": "sha256:09cd8744ff4b9669723cc1e87a64e8867d101b7e553e772cbc31f77632c4a383", "3.4.6--r43hdfd78af_10": "sha256:4f20821d25d1e36e44b5644a9105ad80fd7213f70924bc40c48e5c4820e47efc", "3.4.6--r43hdfd78af_11": "sha256:e8da9e869e94626c169f2d243d41f6d65e38bd07283df79c592579dea05eed65", "3.4.6--r44hdfd78af_12": "sha256:d54e46aa46c76d8955d53622172e53c47de86d5458d01c4c754f7090ea8e94d5"}, "docker": "quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce11.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene:3.4.6--r44hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene/3.4.6--r44hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.refgene/3.4.6--r44hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.celegans.ucsc.ce11.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.celegans.ucsc.ce11.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.celegans.ucsc.ce11.refgene

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