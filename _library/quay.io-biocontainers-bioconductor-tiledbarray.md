---
layout: container
name:  "quay.io/biocontainers/bioconductor-tiledbarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tiledbarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tiledbarray/container.yaml"
updated_at: "2024-03-14 02:44:12.839613"
latest: "1.12.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tiledbarray"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.0--r43hf17093f_0"
 - "1.12.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tiledbarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tiledbarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tiledbarray", "latest": {"1.12.0--r43hf17093f_0": "sha256:d3fd603123f7dcee971b807924aff7335730ef06fd55415d2f4ac411d7db983c"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:5a7cbb1f90694692d64a10f12cf77762a619dbdda3b385c5ad91d9e3c2aed411", "1.8.0--r42hc247a5b_0": "sha256:141df3ec85aafeefb4d5424a55eb1b357f0774da9825d393eb41d9adf0fb84ce", "1.8.0--r42hf17093f_1": "sha256:83557add720beccc17449460405ec1d5edf426924505b7a664af9c420c1f4a2d", "1.10.0--r43hf17093f_0": "sha256:4045f094603c67f0dcc67e1b6cd436a20282c1fd4f89cc84ab1dab5767b9c05d", "1.12.0--r43hf17093f_0": "sha256:d3fd603123f7dcee971b807924aff7335730ef06fd55415d2f4ac411d7db983c"}, "docker": "quay.io/biocontainers/bioconductor-tiledbarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tiledbarray.
shpc-registry automated BioContainers addition for bioconductor-tiledbarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tiledbarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tiledbarray:1.12.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tiledbarray/1.12.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-tiledbarray/1.12.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tiledbarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tiledbarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tiledbarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tiledbarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tiledbarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tiledbarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tiledbarray

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