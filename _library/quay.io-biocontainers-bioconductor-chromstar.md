---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromstar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromstar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromstar/container.yaml"
updated_at: "2023-10-12 02:42:57.536383"
latest: "1.26.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromstar"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.2--r41hc247a5b_1"
 - "1.19.0--r41h399db7b_0"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_2"
 - "1.24.0--r42hf17093f_1"
 - "1.26.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromstar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromstar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromstar", "latest": {"1.26.0--r43hf17093f_0": "sha256:e7cd560cf1d1ff8a205794df836daa50e8d494e4b48cec78a8c1f5e7b0ee1c39"}, "tags": {"1.8.1--r351hf484d3e_0": "sha256:3a3a684038fd108122b90779b87c072b00e695b54e59c223c3d94060a9c51b28", "1.24.0--r42hc247a5b_0": "sha256:c0c724a214ea5bbff726ac96005901f5d32eb629b943a7f959eebdd3061ee9c2", "1.20.2--r41hc247a5b_1": "sha256:6c381071541ffc4e6c7c93dec6688babe80d5ea600881670da1a4cbeadb198e9", "1.19.0--r41h399db7b_0": "sha256:429887da7213b9f9d931bc18fba60af3f88ddbca4c7f3cabe2ef0d4e41427be2", "1.18.0--r41h399db7b_0": "sha256:7cadf36ec61289b34389db5c3fffe8741c34ae30794b9f4879afa78cf64fc7b7", "1.16.0--r40h399db7b_2": "sha256:8006127695f14eb2b043c7d153e02cc1e357dadc7937505d111a9ba52b8047e1", "1.24.0--r42hf17093f_1": "sha256:7565294f0ac4d3769a26831d63a91318c409f6191ef2aa12f67354eef96d0569", "1.26.0--r43hf17093f_0": "sha256:e7cd560cf1d1ff8a205794df836daa50e8d494e4b48cec78a8c1f5e7b0ee1c39"}, "docker": "quay.io/biocontainers/bioconductor-chromstar", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromstar.
shpc-registry automated BioContainers addition for bioconductor-chromstar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromstar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromstar:1.26.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromstar/1.26.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-chromstar/1.26.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromstar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromstar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromstar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromstar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromstar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromstar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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