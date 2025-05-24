---
layout: container
name:  "quay.io/biocontainers/bioconductor-sparsearray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sparsearray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sparsearray/container.yaml"
updated_at: "2025-05-24 03:25:07.013196"
latest: "1.6.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-sparsearray"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.10--r43ha9d7317_0"
 - "1.2.2--r43ha9d7317_1"
 - "1.2.2--r43ha9d7317_2"
 - "1.6.0--r44h3df3fcb_0"
 - "1.6.0--r44h3df3fcb_1"
description: "singularity registry hpc automated addition for bioconductor-sparsearray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sparsearray", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-sparsearray", "latest": {"1.6.0--r44h3df3fcb_1": "sha256:5cbf258bd5c7cbbf69e61ef315300ff4e494a3c3012475db4ef4c604bc8c9960"}, "tags": {"1.0.10--r43ha9d7317_0": "sha256:2bfed3b1dcb0a1d98535a806914c632d5693c1cb775daffcebdab60ed84c44dd", "1.2.2--r43ha9d7317_1": "sha256:666f4d9c0a8ce586796e63571cabdc8a8ae90691886288b9462cbbfded87ef24", "1.2.2--r43ha9d7317_2": "sha256:def2daef1d4aca02960a91cc39c2b4837539a0c4ac25caca822714c41bb036d4", "1.6.0--r44h3df3fcb_0": "sha256:187268387a15f99fc6b73bf02ef0882e24f7c48b1f3f3b7b2535e0962b74eb40", "1.6.0--r44h3df3fcb_1": "sha256:5cbf258bd5c7cbbf69e61ef315300ff4e494a3c3012475db4ef4c604bc8c9960"}, "docker": "quay.io/biocontainers/bioconductor-sparsearray", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sparsearray.
singularity registry hpc automated addition for bioconductor-sparsearray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsearray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsearray:1.6.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sparsearray/1.6.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-sparsearray/1.6.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sparsearray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsearray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsearray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sparsearray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sparsearray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sparsearray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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