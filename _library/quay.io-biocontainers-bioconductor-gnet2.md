---
layout: container
name:  "quay.io/biocontainers/bioconductor-gnet2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gnet2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gnet2/container.yaml"
updated_at: "2023-12-02 03:02:08.449761"
latest: "1.16.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gnet2"
aliases:
 - "xgboost"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hc247a5b_0"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gnet2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gnet2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gnet2", "latest": {"1.16.0--r43hf17093f_0": "sha256:01bb8eefbccacfbc3f2beacec5c158cfbf1d04cfb588a21796d2fbd5951c3c57"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:cea6a8005017e23d09c1fdddaaae3bb2621e709062668e1220b47a6787fa6e12", "1.10.0--r41hc247a5b_2": "sha256:c8aad01c8605f1910592f7de8544411befa6267f777c4aaccf22657fcf86f3bf", "1.14.0--r42hc247a5b_0": "sha256:8d043f7e2c8e38d35e82d0e4fc1c8c7fbdb5b95eba62c5faf8413ae912afdcfd", "1.14.0--r42hf17093f_1": "sha256:b604ea4643b82a5a066db208025fa75aa0997fafe4f961e6adf9edfb76ffcc33", "1.16.0--r43hf17093f_0": "sha256:01bb8eefbccacfbc3f2beacec5c158cfbf1d04cfb588a21796d2fbd5951c3c57"}, "docker": "quay.io/biocontainers/bioconductor-gnet2", "aliases": {"xgboost": "/usr/local/bin/xgboost", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gnet2.
shpc-registry automated BioContainers addition for bioconductor-gnet2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gnet2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gnet2:1.16.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gnet2/1.16.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-gnet2/1.16.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gnet2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gnet2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gnet2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gnet2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gnet2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gnet2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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