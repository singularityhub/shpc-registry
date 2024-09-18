---
layout: container
name:  "quay.io/biocontainers/bioconductor-cn.farms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cn.farms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cn.farms/container.yaml"
updated_at: "2024-09-18 02:45:19.457672"
latest: "1.50.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cn.farms"

versions:
 - "1.42.0--r41hc247a5b_2"
 - "1.46.0--r42hc247a5b_0"
 - "1.46.0--r42hf17093f_1"
 - "1.48.0--r43hf17093f_0"
 - "1.50.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cn.farms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cn.farms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cn.farms", "latest": {"1.50.0--r43hf17093f_0": "sha256:15d6fa4464dbc1297707ddb65f735fb477028f48ee03d7ab4a88ca4bf45480a8"}, "tags": {"1.42.0--r41hc247a5b_2": "sha256:45cfce5f03d6c88a3d0a2adacaf32e0b48cef65d4c478a415f90c98925969e6e", "1.46.0--r42hc247a5b_0": "sha256:be7fd485081edf176edc64b66f63b910b7c25b41dd9d444addbaee4af2aa3945", "1.46.0--r42hf17093f_1": "sha256:a318346ac7bb9afab91eb95fb8278ab504febd3734cdbc6dfd4a016757ea99dc", "1.48.0--r43hf17093f_0": "sha256:95c1ac6091925e9325f8b459fa3ffff63fd4f5c40defbb44126dd56b6f48fc70", "1.50.0--r43hf17093f_0": "sha256:15d6fa4464dbc1297707ddb65f735fb477028f48ee03d7ab4a88ca4bf45480a8"}, "docker": "quay.io/biocontainers/bioconductor-cn.farms"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cn.farms.
shpc-registry automated BioContainers addition for bioconductor-cn.farms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cn.farms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cn.farms:1.50.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cn.farms/1.50.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cn.farms/1.50.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cn.farms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cn.farms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cn.farms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cn.farms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cn.farms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cn.farms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cn.farms

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