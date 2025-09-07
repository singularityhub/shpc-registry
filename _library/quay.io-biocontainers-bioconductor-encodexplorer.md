---
layout: container
name:  "quay.io/biocontainers/bioconductor-encodexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-encodexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-encodexplorer/container.yaml"
updated_at: "2025-09-07 03:09:19.639266"
latest: "2.16.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-encodexplorer"
aliases:
 - "c89"
 - "c99"
versions:
 - "2.8.0--r351_0"
 - "2.16.0--r40hdfd78af_1"
 - "2.14.0--r40_0"
 - "2.12.0--r36_0"
 - "2.10.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-encodexplorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-encodexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-encodexplorer", "latest": {"2.16.0--r40hdfd78af_1": "sha256:eeb03e7f3e9f8370bd7bfd81b98509b557a2930e8ea8253eef74470bf5ea736f"}, "tags": {"2.8.0--r351_0": "sha256:2cb2f00b796e5f6fa213642af17719f8169ddeb38213625e90b27353d9de7955", "2.16.0--r40hdfd78af_1": "sha256:eeb03e7f3e9f8370bd7bfd81b98509b557a2930e8ea8253eef74470bf5ea736f", "2.14.0--r40_0": "sha256:419ae8419420d1ec51de08d5ab6af2761e79b373029c4d9eebe9764d1e8384bd", "2.12.0--r36_0": "sha256:08baf908dbc004e2c830d1c830ce3d23e6465cd9668d3ace34f42d4bf60c6b95", "2.10.0--r36_1": "sha256:f814f98776ac2d4f447ed0803a0140be7ef71e5a68502d1e1a0916e07d2aee17"}, "docker": "quay.io/biocontainers/bioconductor-encodexplorer", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-encodexplorer.
shpc-registry automated BioContainers addition for bioconductor-encodexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-encodexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-encodexplorer:2.16.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-encodexplorer/2.16.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-encodexplorer/2.16.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-encodexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-encodexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-encodexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-encodexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-encodexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-encodexplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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