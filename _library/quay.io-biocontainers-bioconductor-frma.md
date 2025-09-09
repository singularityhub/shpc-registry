---
layout: container
name:  "quay.io/biocontainers/bioconductor-frma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-frma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-frma/container.yaml"
updated_at: "2025-09-09 03:53:20.413192"
latest: "1.58.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-frma"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.58.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-frma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-frma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-frma", "latest": {"1.58.0--r44hdfd78af_0": "sha256:81fc094cb835c21ba8c17d800eb1b8389546fbe349d90bc9294afbfa01d5c8c3"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:309bda605a6f1a18516b20020ff14c1865e658dc221cf00c25902f0c0e52c340", "1.50.0--r42hdfd78af_0": "sha256:768ae34cb1658074ad783f27fd59c1496fd3fc9738755541762b839c0d87c79c", "1.52.0--r43hdfd78af_0": "sha256:8b8a783b2d0781957d020d78028379d3b216efa3d282eaf43c5d6c6b43308dc9", "1.54.0--r43hdfd78af_0": "sha256:74b05f70de915889d6871cb925c142c7a255743fe3ecce211d4ce9cf7cbae98f", "1.58.0--r44hdfd78af_0": "sha256:81fc094cb835c21ba8c17d800eb1b8389546fbe349d90bc9294afbfa01d5c8c3"}, "docker": "quay.io/biocontainers/bioconductor-frma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-frma.
shpc-registry automated BioContainers addition for bioconductor-frma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-frma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-frma:1.58.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-frma/1.58.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-frma/1.58.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-frma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-frma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-frma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-frma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-frma

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