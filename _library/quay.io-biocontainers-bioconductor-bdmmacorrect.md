---
layout: container
name:  "quay.io/biocontainers/bioconductor-bdmmacorrect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bdmmacorrect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bdmmacorrect/container.yaml"
updated_at: "2025-11-08 03:48:43.063047"
latest: "1.18.1--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-bdmmacorrect"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40h399db7b_1"
 - "1.16.0--r42hc247a5b_0"
 - "1.12.0--r41hc247a5b_2"
 - "1.10.0--r41h399db7b_0"
 - "1.16.0--r42hf17093f_1"
 - "1.18.1--r43hf17093f_0"
 - "1.18.1--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-bdmmacorrect"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bdmmacorrect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bdmmacorrect", "latest": {"1.18.1--r43hf17093f_1": "sha256:91446bb9f729022de514ab6c7ca83e429f56f7e3644fe431f93b45f79e536f4a"}, "tags": {"1.8.0--r40h399db7b_1": "sha256:03f55ba4e0cbb221f901e7067dbb960c11c38920ce32a1f67ff4587f225ec3ca", "1.16.0--r42hc247a5b_0": "sha256:038e0f19b28ecc3d33a789a697d2f13e80021469ae7dce869d89099ae02ee614", "1.12.0--r41hc247a5b_2": "sha256:d9b26cd09e02d4200d1c98709b042d8a61388fc581cd4cf39a3b9cf381587687", "1.10.0--r41h399db7b_0": "sha256:92b688812e1d5543792874dcf2fb33e772c746624573294303e6afbc48ce0ef9", "1.16.0--r42hf17093f_1": "sha256:02f32d2589825d4c1481d3a408fe672b47eaf9c03cb1391f45ebbc0c65f66e01", "1.18.1--r43hf17093f_0": "sha256:32abebf74c1a95c236590a9792dd5e5b4b2baaa7ffac3761c97e3a78de5a1ba4", "1.18.1--r43hf17093f_1": "sha256:91446bb9f729022de514ab6c7ca83e429f56f7e3644fe431f93b45f79e536f4a"}, "docker": "quay.io/biocontainers/bioconductor-bdmmacorrect", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bdmmacorrect.
shpc-registry automated BioContainers addition for bioconductor-bdmmacorrect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bdmmacorrect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bdmmacorrect:1.18.1--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bdmmacorrect/1.18.1--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-bdmmacorrect/1.18.1--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bdmmacorrect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bdmmacorrect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bdmmacorrect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bdmmacorrect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bdmmacorrect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bdmmacorrect-inspect-deffile:

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