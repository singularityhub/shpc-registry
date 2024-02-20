---
layout: container
name:  "quay.io/biocontainers/bioconductor-atsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-atsnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-atsnp/container.yaml"
updated_at: "2024-02-20 02:49:38.072708"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-atsnp"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-atsnp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-atsnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-atsnp", "latest": {"1.18.0--r43hf17093f_0": "sha256:f9856dcfe2f063b5dbbe9e6d40c3de69ab0afad0f9bca01a3fc6205d747323de"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:40e1ab4feb8dfae9dbef31172293dfb3153eec7992d3d9f09e708caa33d6af2b", "1.14.0--r42hc247a5b_0": "sha256:e851e4286e6427a3e0a7139d3c1f405a3daba89cef097df653989973f8ec58d1", "1.10.0--r41hc247a5b_2": "sha256:2711465010c3adfbc15d96b1bf75944cdc61886b74a3b4199dcb11448335e8ea", "1.14.0--r42hf17093f_1": "sha256:c8193076416a074ebc94d17457047244f02530f83e28bfa13287c0b87deb4ec9", "1.16.0--r43hf17093f_0": "sha256:f1ea553e15c603b9373071bbc2f296351cc9091fbfdeb765c967f41e6d3cd5db", "1.18.0--r43hf17093f_0": "sha256:f9856dcfe2f063b5dbbe9e6d40c3de69ab0afad0f9bca01a3fc6205d747323de"}, "docker": "quay.io/biocontainers/bioconductor-atsnp", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-atsnp.
shpc-registry automated BioContainers addition for bioconductor-atsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-atsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-atsnp:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-atsnp/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-atsnp/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-atsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-atsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-atsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-atsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-atsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-atsnp-inspect-deffile:

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