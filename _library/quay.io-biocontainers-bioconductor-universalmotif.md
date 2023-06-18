---
layout: container
name:  "quay.io/biocontainers/bioconductor-universalmotif"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-universalmotif/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-universalmotif/container.yaml"
updated_at: "2023-06-18 02:58:48.270132"
latest: "1.16.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-universalmotif"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.3--r40h399db7b_0"
 - "1.16.0--r42hc247a5b_0"
 - "1.12.4--r41hc247a5b_0"
 - "1.10.1--r41h399db7b_0"
 - "1.16.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-universalmotif"
config: {"url": "https://biocontainers.pro/tools/bioconductor-universalmotif", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-universalmotif", "latest": {"1.16.0--r42hf17093f_1": "sha256:18c991a2917e7fcfddf197eda08835f017760da3b6e070224ea78a1392b8242d"}, "tags": {"1.8.3--r40h399db7b_0": "sha256:e67048bda7783467b120c6d37b18c6bb5aecd6fe27c1ae77fc458b2801f2d8aa", "1.16.0--r42hc247a5b_0": "sha256:0f36d763035a923c86edc7d4d6d8b8aa0a05a84b0b15744087c38c78e7976cee", "1.12.4--r41hc247a5b_0": "sha256:7c5949aef3c01553085419316a020e90e2f6eb7589cfe34c8fdd3b2d3da01fc5", "1.10.1--r41h399db7b_0": "sha256:0b9714f615654ccded1de0f546f77117644a116ac240742c8b84c498675bd19e", "1.16.0--r42hf17093f_1": "sha256:18c991a2917e7fcfddf197eda08835f017760da3b6e070224ea78a1392b8242d"}, "docker": "quay.io/biocontainers/bioconductor-universalmotif", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-universalmotif.
shpc-registry automated BioContainers addition for bioconductor-universalmotif
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-universalmotif
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-universalmotif:1.16.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-universalmotif/1.16.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-universalmotif/1.16.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-universalmotif-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-universalmotif-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-universalmotif-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-universalmotif-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-universalmotif-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-universalmotif-inspect-deffile:

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