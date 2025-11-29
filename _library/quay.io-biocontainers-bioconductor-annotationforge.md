---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationforge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationforge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationforge/container.yaml"
updated_at: "2025-11-29 02:58:45.798464"
latest: "1.48.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotationforge"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.2--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.48.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationforge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationforge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationforge", "latest": {"1.48.0--r44hdfd78af_0": "sha256:296d1387dcb84f77a90dcd0d244ce5a91e67da8c8ff03a056e195f4561e6829c"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:e75c5fed340242f3096f61b9e9760f9a8e1c1334ff902d0a6336ce4cf07ccb63", "1.40.0--r42hdfd78af_0": "sha256:6084b2a6b10bc6a6bc5c199cff146188c159595f85186df946dd51f585655a99", "1.42.2--r43hdfd78af_0": "sha256:ba76ebcfc77ab8729d5423c648fbb8da16372ce09b511be2723d097daf0cc4df", "1.44.0--r43hdfd78af_0": "sha256:899a5e3e26f2b433938305acd08acabf7bbe3df8a9806e597d9144be453bd3e8", "1.48.0--r44hdfd78af_0": "sha256:296d1387dcb84f77a90dcd0d244ce5a91e67da8c8ff03a056e195f4561e6829c"}, "docker": "quay.io/biocontainers/bioconductor-annotationforge"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationforge.
shpc-registry automated BioContainers addition for bioconductor-annotationforge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationforge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationforge:1.48.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationforge/1.48.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationforge/1.48.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotationforge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationforge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationforge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotationforge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotationforge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotationforge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-annotationforge

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