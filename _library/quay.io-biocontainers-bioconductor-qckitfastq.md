---
layout: container
name:  "quay.io/biocontainers/bioconductor-qckitfastq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qckitfastq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qckitfastq/container.yaml"
updated_at: "2023-09-27 03:25:11.464405"
latest: "1.16.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qckitfastq"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qckitfastq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qckitfastq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qckitfastq", "latest": {"1.16.0--r43hf17093f_0": "sha256:e0e72377b737620924a5c4bbc23237793aac077be555889b539c428ce55dec21"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:a596621359b12ac8814adfa65c1bb8efb10f5e29f0c1753e9e2dc357846ddd68", "1.14.0--r42hc247a5b_0": "sha256:7f41209e8eb968276c2466331187ff5770491ca2d192080aa51f1f3c4bef3a11", "1.10.0--r41hc247a5b_2": "sha256:073cd586fe698d091f8d9f7c4c14d2f71ff70910947bc8e05a7f2af2e09d4564", "1.14.0--r42hf17093f_1": "sha256:a471a67757ae6ba694d246646294c04abd8a361e91ca1bcbb9a481aafb1e6fe6", "1.16.0--r43hf17093f_0": "sha256:e0e72377b737620924a5c4bbc23237793aac077be555889b539c428ce55dec21"}, "docker": "quay.io/biocontainers/bioconductor-qckitfastq", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qckitfastq.
shpc-registry automated BioContainers addition for bioconductor-qckitfastq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qckitfastq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qckitfastq:1.16.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qckitfastq/1.16.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-qckitfastq/1.16.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qckitfastq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qckitfastq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qckitfastq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qckitfastq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qckitfastq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qckitfastq-inspect-deffile:

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