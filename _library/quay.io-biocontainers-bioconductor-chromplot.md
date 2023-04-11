---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromplot/container.yaml"
updated_at: "2023-04-11 02:34:46.266975"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromplot"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromplot"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromplot", "latest": {"1.26.0--r42hdfd78af_0": "sha256:858749f900bef1ac68c5c4e68d7b54c0f037d5fce0f09986744b45c87ac1bbcb"}, "tags": {"1.8.0--r351_0": "sha256:6a45a9c1f22e44af3a4b8823872fe4f35f4cf3b80153cd4afce0543a8da7f81e", "1.26.0--r42hdfd78af_0": "sha256:858749f900bef1ac68c5c4e68d7b54c0f037d5fce0f09986744b45c87ac1bbcb", "1.22.0--r41hdfd78af_0": "sha256:5653d5e3795fc79d4f4ccd0d4674b6009899298bc213a654621d3008d6583edd", "1.20.0--r41hdfd78af_0": "sha256:40d0a5344275616fb5ee5df0e9043e367a55fb0d2b24d27ea75f06e418325bf5", "1.18.0--r40hdfd78af_1": "sha256:2463930872c644e01faa0b9039256c7cd326779936de8fdfe1526331b51d59bc", "1.16.0--r40_0": "sha256:48ae97416f2a6960662a862b40cd6e107c1b71e1aa5f7844ef97799945c22f74"}, "docker": "quay.io/biocontainers/bioconductor-chromplot", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromplot.
shpc-registry automated BioContainers addition for bioconductor-chromplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromplot:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromplot/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chromplot/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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