---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq/container.yaml"
updated_at: "2024-06-27 03:08:36.666096"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnamodr.alkanilineseq"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnamodr.alkanilineseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnamodr.alkanilineseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnamodr.alkanilineseq", "latest": {"1.16.0--r43hdfd78af_0": "sha256:5a46a193660949012d4141af658ce76686df62fd8047dc6211eb159b44a64dab"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:35be0dd65c38b2c2f3e8cf20563d44a9b450dc00a5b1325b7063e31800aa7365", "1.12.0--r42hdfd78af_0": "sha256:ddb6dbee8ef70074e083953047c1b99adbcd4fcfb3a2520fbff756e4e521cb6f", "1.14.0--r43hdfd78af_0": "sha256:0a1478a9960538805b8f30c7d65b766c81e60c4702327019ed43fd3380156893", "1.16.0--r43hdfd78af_0": "sha256:5a46a193660949012d4141af658ce76686df62fd8047dc6211eb159b44a64dab"}, "docker": "quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq.
shpc-registry automated BioContainers addition for bioconductor-rnamodr.alkanilineseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnamodr.alkanilineseq/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnamodr.alkanilineseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.alkanilineseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.alkanilineseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnamodr.alkanilineseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnamodr.alkanilineseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnamodr.alkanilineseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnamodr.alkanilineseq

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