---
layout: container
name:  "quay.io/biocontainers/bioconductor-nucpos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nucpos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nucpos/container.yaml"
updated_at: "2024-02-08 02:40:36.973246"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nucpos"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hacda110_1"
 - "1.12.0--r41hefde4a7_2"
 - "1.10.0--r41hacda110_0"
 - "1.16.0--r42hefde4a7_0"
 - "1.16.0--r42h9913872_1"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nucpos"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nucpos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nucpos", "latest": {"1.20.0--r43hdfd78af_0": "sha256:23dad30f7f5d1006e2ca341de63d75b73df422521a86f3c7a82a113ae750e4a8"}, "tags": {"1.8.0--r40hacda110_1": "sha256:f55553a618f780793b4bb5aa0e74a1f98f348508f8e899fdfc277613ff44f562", "1.12.0--r41hefde4a7_2": "sha256:f321ee951faf449d88f7eda042cbc1315611a9d81fe62a2885c7e8fa52a9f0fb", "1.10.0--r41hacda110_0": "sha256:82922799f259227eee3600d4cdcc074e059ca4286e0b88ea63412128d829616f", "1.16.0--r42hefde4a7_0": "sha256:922a2425d0f7dfb62c82ae41121354e3b6a3196575975fd4be39a32f93f82015", "1.16.0--r42h9913872_1": "sha256:de3c31e6e15f85f09d8e4765d83671f8fbb1e1c3887dd3642b07430d019ca248", "1.18.0--r43hdfd78af_0": "sha256:5bbdd95dcb3f74df7b26996a6bb78c3e24afd8d17e56b66590fecb61f4b54c0d", "1.20.0--r43hdfd78af_0": "sha256:23dad30f7f5d1006e2ca341de63d75b73df422521a86f3c7a82a113ae750e4a8"}, "docker": "quay.io/biocontainers/bioconductor-nucpos", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nucpos.
shpc-registry automated BioContainers addition for bioconductor-nucpos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nucpos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nucpos:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nucpos/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nucpos/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nucpos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nucpos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nucpos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nucpos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nucpos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nucpos-inspect-deffile:

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