---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytolib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytolib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytolib/container.yaml"
updated_at: "2024-02-07 02:29:28.963796"
latest: "2.14.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytolib"

versions:
 - "2.6.2--r41hc247a5b_1"
 - "2.10.0--r42hc247a5b_0"
 - "2.12.0--r43hf17093f_0"
 - "2.14.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cytolib"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytolib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cytolib", "latest": {"2.14.0--r43hf17093f_0": "sha256:dce8ad4fd89b626fb86df31a7bff2214b0b3d7b97ec1297a2a9edff2a68cd624"}, "tags": {"2.6.2--r41hc247a5b_1": "sha256:114a7cd157a77272b8c1d9d14f3aa07b99ef62c566b2b8c52253d1010e547ca9", "2.10.0--r42hc247a5b_0": "sha256:1d2e606cdd702baa7302c607273cfd8a75e02c2afd680d92bb3b02625e22e537", "2.12.0--r43hf17093f_0": "sha256:232979c2cc49ed474b172e8af5f9b1246bf29ee008d807c2a205ede8b3d11960", "2.14.0--r43hf17093f_0": "sha256:dce8ad4fd89b626fb86df31a7bff2214b0b3d7b97ec1297a2a9edff2a68cd624"}, "docker": "quay.io/biocontainers/bioconductor-cytolib"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytolib.
shpc-registry automated BioContainers addition for bioconductor-cytolib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytolib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytolib:2.14.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytolib/2.14.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cytolib/2.14.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytolib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytolib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytolib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytolib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytolib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytolib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cytolib

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