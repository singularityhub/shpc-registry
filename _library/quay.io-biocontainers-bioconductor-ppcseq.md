---
layout: container
name:  "quay.io/biocontainers/bioconductor-ppcseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ppcseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ppcseq/container.yaml"
updated_at: "2025-09-24 03:06:50.606146"
latest: "1.14.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ppcseq"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
 - "1.14.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ppcseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ppcseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ppcseq", "latest": {"1.14.0--r44he5774e6_0": "sha256:2b5268aa501f35ecf05930c22c91d378d46769628092569a4b6eb360752e43e9"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:74db7d393db5d859e082d93f1ab8d4e9d6064aec959aaeb6d48fd1f9b15fe446", "1.6.0--r42hc247a5b_0": "sha256:ef62a844c6f8d9ba0c51b23cd38ef1d7df43a3cfd0ecf231c1605289ec8b4ce3", "1.6.0--r42hf17093f_1": "sha256:e041cd267704e5ad4b5eaefba8475fdd8c51713ca59f272148c8e333bed99245", "1.8.0--r43hf17093f_0": "sha256:4c2ba95cccee2260108c69317e9b07dec306792e05a14d561f9b17910530e618", "1.10.0--r43hf17093f_0": "sha256:10db55cedffe200c2f19638330958193605472ec78ebd511dc082991b340eaad", "1.14.0--r44he5774e6_0": "sha256:2b5268aa501f35ecf05930c22c91d378d46769628092569a4b6eb360752e43e9"}, "docker": "quay.io/biocontainers/bioconductor-ppcseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ppcseq.
shpc-registry automated BioContainers addition for bioconductor-ppcseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ppcseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ppcseq:1.14.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ppcseq/1.14.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-ppcseq/1.14.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ppcseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ppcseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ppcseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ppcseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ppcseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ppcseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ppcseq

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