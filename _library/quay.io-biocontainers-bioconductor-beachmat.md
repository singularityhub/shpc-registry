---
layout: container
name:  "quay.io/biocontainers/bioconductor-beachmat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beachmat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beachmat/container.yaml"
updated_at: "2025-11-17 04:53:28.135199"
latest: "2.22.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-beachmat"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41h399db7b_0"
 - "2.14.0--r42hc247a5b_0"
 - "2.10.0--r41hc247a5b_2"
 - "2.14.0--r42hf17093f_1"
 - "2.16.0--r43hf17093f_0"
 - "2.18.0--r43hf17093f_0"
 - "2.18.0--r43hf17093f_1"
 - "2.22.0--r44he5774e6_0"
 - "2.22.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-beachmat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beachmat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beachmat", "latest": {"2.22.0--r44he5774e6_1": "sha256:b84de5a5479d0a1289e4c0ef7cfebfd28d39a71ab838b9db98a895d23033c5aa"}, "tags": {"2.8.0--r41h399db7b_0": "sha256:59f89eeaa0653e777d623574f908dd365141b2f4ca040d2df35f90fff9676927", "2.14.0--r42hc247a5b_0": "sha256:f24cbf0d202ad3a5091f8c0cb35440f57c83880ff5757d01ac52c9acf0bd75db", "2.10.0--r41hc247a5b_2": "sha256:f6aba1b4f086984b37b8502a4d6317db90cdc77c52716fa365ba8755cc8403ed", "2.14.0--r42hf17093f_1": "sha256:d0e05c216adc665cbca205b21cf1733e4f1e6358cb0a3941c9548215cbbe5117", "2.16.0--r43hf17093f_0": "sha256:38dbfce24fbdd86020d56172732703b192445dee3d4782160ef2a380454c06de", "2.18.0--r43hf17093f_0": "sha256:5d574ad397dd99f7a3c7e595c50ec852ae3461a04d89c74f79fd09a501e70a8f", "2.18.0--r43hf17093f_1": "sha256:cfdc4f1d75a4ff8090d4fe6b49bc295fea50d717b447f2609b285aac82700366", "2.22.0--r44he5774e6_0": "sha256:5e16ee0bb1329ed809f9209bbd96953f426851c4a7c16a9415921311a791bd83", "2.22.0--r44he5774e6_1": "sha256:b84de5a5479d0a1289e4c0ef7cfebfd28d39a71ab838b9db98a895d23033c5aa"}, "docker": "quay.io/biocontainers/bioconductor-beachmat", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beachmat.
shpc-registry automated BioContainers addition for bioconductor-beachmat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beachmat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beachmat:2.22.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beachmat/2.22.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-beachmat/2.22.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beachmat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beachmat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beachmat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beachmat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beachmat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beachmat-inspect-deffile:

```bash
$ singularity inspect -d <container>
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