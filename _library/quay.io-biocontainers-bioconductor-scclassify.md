---
layout: container
name:  "quay.io/biocontainers/bioconductor-scclassify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scclassify/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scclassify/container.yaml"
updated_at: "2025-03-08 02:44:10.352523"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scclassify"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scclassify"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scclassify", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scclassify", "latest": {"1.18.0--r44hdfd78af_0": "sha256:62844e001ecec7b9a4b64709c36e7a76a936eafa501efb00acdca1ad6f488337"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:c67631194638007f8f3da8c485d0b3948a581d97aa8fdf6400a9f83d1e3b1591", "1.10.0--r42hdfd78af_0": "sha256:b3f4b05800f9151a74f5d74ccedcbaacb6baad78062113564467634ba688c0b7", "1.12.0--r43hdfd78af_0": "sha256:43ed0ad9c7797b1a08c89793798b3d44c8864be5ae6a0c2a05680b26da860ef0", "1.18.0--r44hdfd78af_0": "sha256:62844e001ecec7b9a4b64709c36e7a76a936eafa501efb00acdca1ad6f488337"}, "docker": "quay.io/biocontainers/bioconductor-scclassify"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scclassify.
shpc-registry automated BioContainers addition for bioconductor-scclassify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scclassify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scclassify:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scclassify/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scclassify/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scclassify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scclassify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scclassify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scclassify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scclassify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scclassify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scclassify

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