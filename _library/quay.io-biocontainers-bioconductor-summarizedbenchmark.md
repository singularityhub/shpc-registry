---
layout: container
name:  "quay.io/biocontainers/bioconductor-summarizedbenchmark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-summarizedbenchmark/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-summarizedbenchmark/container.yaml"
updated_at: "2025-12-24 03:44:57.541982"
latest: "2.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-summarizedbenchmark"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r40hdfd78af_1"
 - "2.16.0--r42hdfd78af_0"
 - "2.12.0--r41hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
 - "2.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-summarizedbenchmark"
config: {"url": "https://biocontainers.pro/tools/bioconductor-summarizedbenchmark", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-summarizedbenchmark", "latest": {"2.20.0--r43hdfd78af_0": "sha256:2bed0fdddde36097e3f567ef98d820e1edeb6425f293f37e47bc40e4ab6ea809"}, "tags": {"2.8.0--r40hdfd78af_1": "sha256:69f700a491d99333ce544c111bce419abe884c7a9c1f678d1fd690255b7b57ce", "2.16.0--r42hdfd78af_0": "sha256:4da200743a53f16596d99524ab9fe4d9f699b7aca9062e3cdc13dc0753bbb6b6", "2.12.0--r41hdfd78af_0": "sha256:b01a27d8d5c406cab46d15f237918bd251e73d7a8e77931b03bda3e815a17618", "2.10.0--r41hdfd78af_0": "sha256:7526bff9b525b4c76568f3f2d98e096b62a8af72fa1f81e28acabfcff5e31969", "2.18.0--r43hdfd78af_0": "sha256:eb5373c170cba5fff1a28d0f61aef7cf3bc399c499edade58d8173b0b3a7887d", "2.20.0--r43hdfd78af_0": "sha256:2bed0fdddde36097e3f567ef98d820e1edeb6425f293f37e47bc40e4ab6ea809"}, "docker": "quay.io/biocontainers/bioconductor-summarizedbenchmark", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-summarizedbenchmark.
shpc-registry automated BioContainers addition for bioconductor-summarizedbenchmark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-summarizedbenchmark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-summarizedbenchmark:2.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-summarizedbenchmark/2.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-summarizedbenchmark/2.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-summarizedbenchmark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-summarizedbenchmark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-summarizedbenchmark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-summarizedbenchmark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-summarizedbenchmark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-summarizedbenchmark-inspect-deffile:

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