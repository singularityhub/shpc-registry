---
layout: container
name:  "quay.io/biocontainers/bioconductor-iclusterplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iclusterplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iclusterplus/container.yaml"
updated_at: "2024-07-28 02:58:45.489109"
latest: "1.38.0--r43h9913872_2"
container_url: "https://biocontainers.pro/tools/bioconductor-iclusterplus"

versions:
 - "1.30.0--r41hefde4a7_2"
 - "1.34.0--r42hefde4a7_0"
 - "1.34.0--r42h9913872_1"
 - "1.36.1--r43h9913872_0"
 - "1.38.0--r43h9913872_0"
 - "1.38.0--r43h9913872_2"
description: "shpc-registry automated BioContainers addition for bioconductor-iclusterplus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iclusterplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iclusterplus", "latest": {"1.38.0--r43h9913872_2": "sha256:f19baefa7f83f21cf2bb8fd4343b61d2de215cb52d629b9c90a02d652e293114"}, "tags": {"1.30.0--r41hefde4a7_2": "sha256:86cc817102ee51e101abc5a61c7585e9516aa1b36eae3a4c85a9d6e8960d59f4", "1.34.0--r42hefde4a7_0": "sha256:4ad61718c3a05ec8992d4d438cda81d21ee451a839ca3312fa2b1a9fe73e8e26", "1.34.0--r42h9913872_1": "sha256:2780d5410cd08c21f91c76b13cb05f9c8d7f4ed1b760c12de5064fedfa61df8f", "1.36.1--r43h9913872_0": "sha256:0f19f962996342365d442e3c0834af85167e5df5b9680aa8e37764ef73b23074", "1.38.0--r43h9913872_0": "sha256:c5ceedc73c598b421285b193b0a0687325239254770b033cec3c4fec36abbf74", "1.38.0--r43h9913872_2": "sha256:f19baefa7f83f21cf2bb8fd4343b61d2de215cb52d629b9c90a02d652e293114"}, "docker": "quay.io/biocontainers/bioconductor-iclusterplus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iclusterplus.
shpc-registry automated BioContainers addition for bioconductor-iclusterplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iclusterplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iclusterplus:1.38.0--r43h9913872_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iclusterplus/1.38.0--r43h9913872_2
$ module help quay.io/biocontainers/bioconductor-iclusterplus/1.38.0--r43h9913872_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iclusterplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iclusterplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iclusterplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iclusterplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iclusterplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iclusterplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iclusterplus

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