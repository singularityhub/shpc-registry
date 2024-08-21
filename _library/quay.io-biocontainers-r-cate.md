---
layout: container
name:  "quay.io/biocontainers/r-cate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cate/container.yaml"
updated_at: "2024-08-21 03:23:02.192580"
latest: "1.1.1--r41h3342da4_3"
container_url: "https://biocontainers.pro/tools/r-cate"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1.1--r41h3342da4_3"
 - "1.1--r40h6115d3f_1"
 - "1.1.1--r43h3342da4_5"
description: "shpc-registry automated BioContainers addition for r-cate"
config: {"url": "https://biocontainers.pro/tools/r-cate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-cate", "latest": {"1.1.1--r41h3342da4_3": "sha256:85adde4ce4e292eafb328227c941ba645de88de684178d97c5db96e1a923d9ab"}, "tags": {"1.1.1--r41h3342da4_3": "sha256:85adde4ce4e292eafb328227c941ba645de88de684178d97c5db96e1a923d9ab", "1.1--r40h6115d3f_1": "sha256:a0707b843ee0991c2b112246e94095f9f26ea182b8cda91360b3d7d2aa649f88", "1.1.1--r43h3342da4_5": "sha256:46f87c11c1cc16f8787eeb8a8fec1c2a2064d9a77f6a4bc6ae8861ae1a97f0b4"}, "docker": "quay.io/biocontainers/r-cate", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cate.
shpc-registry automated BioContainers addition for r-cate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cate:1.1.1--r41h3342da4_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cate/1.1.1--r41h3342da4_3
$ module help quay.io/biocontainers/r-cate/1.1.1--r41h3342da4_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cate-inspect-deffile:

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