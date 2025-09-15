---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene/container.yaml"
updated_at: "2025-09-15 03:58:20.609841"
latest: "3.4.6--r44hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.drerio.ucsc.danrer11.refgene"

versions:
 - "3.4.6--r41hdfd78af_8"
 - "3.4.6--r42hdfd78af_9"
 - "3.4.6--r43hdfd78af_10"
 - "3.4.6--r43hdfd78af_11"
 - "3.4.6--r44hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.drerio.ucsc.danrer11.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.drerio.ucsc.danrer11.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.drerio.ucsc.danrer11.refgene", "latest": {"3.4.6--r44hdfd78af_12": "sha256:676f94b8103eaf83949af82bb0303e5040d757fe3485087d74c5ffe77515a2f3"}, "tags": {"3.4.6--r41hdfd78af_8": "sha256:8cfe1b1a0dc4132e79ec2066dbdb56502cda06e252b2fbb85022b4c109e0cc6d", "3.4.6--r42hdfd78af_9": "sha256:b5f15c962cfc4fd96d9c93a21027f5a34f442b7831d1d74558dcd768c0e89247", "3.4.6--r43hdfd78af_10": "sha256:0519f427a6479b1b41e758c424eaba9322c00bbb0378ac66a354c98e5438c606", "3.4.6--r43hdfd78af_11": "sha256:906d344c0af6f46ba05a37e5d8141a7e40ef33234b171c46274cef1322810ba5", "3.4.6--r44hdfd78af_12": "sha256:676f94b8103eaf83949af82bb0303e5040d757fe3485087d74c5ffe77515a2f3"}, "docker": "quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.drerio.ucsc.danrer11.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene:3.4.6--r44hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene/3.4.6--r44hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-txdb.drerio.ucsc.danrer11.refgene/3.4.6--r44hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.drerio.ucsc.danrer11.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.drerio.ucsc.danrer11.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.drerio.ucsc.danrer11.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.drerio.ucsc.danrer11.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.drerio.ucsc.danrer11.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.drerio.ucsc.danrer11.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.drerio.ucsc.danrer11.refgene

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