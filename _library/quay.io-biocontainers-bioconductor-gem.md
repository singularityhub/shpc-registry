---
layout: container
name:  "quay.io/biocontainers/bioconductor-gem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gem/container.yaml"
updated_at: "2023-05-17 03:31:52.255885"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gem"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gem", "latest": {"1.24.0--r42hdfd78af_0": "sha256:99957cdc77198254aabe6c77e7a35fa276377d5b90aed03da8310c0421e7b475"}, "tags": {"1.8.0--r351_0": "sha256:f04340f70500905d5c67fa4b8c7d8434b9130d65fc7e0d0d9fdaa3de0b796c02", "1.24.0--r42hdfd78af_0": "sha256:99957cdc77198254aabe6c77e7a35fa276377d5b90aed03da8310c0421e7b475", "1.20.0--r41hdfd78af_0": "sha256:b12cc92ecf8f3e02e398dbb77d845950d2cd73a60956d41df3744271c3666625", "1.18.0--r41hdfd78af_0": "sha256:dfccac9e7a7e1c7fc916ae352fcc6871eba62be9da436274ee1c64624b056a63", "1.16.0--r40hdfd78af_1": "sha256:78d67122908f66a566a097deedc792c1978e4cb3b353ce92bf4a26d948325aa9", "1.14.0--r40_0": "sha256:40170d422558a4098991fd948fdfb9d038cbe16a7ec5a5b85e1eca853f5a4550"}, "docker": "quay.io/biocontainers/bioconductor-gem", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gem.
shpc-registry automated BioContainers addition for bioconductor-gem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gem:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gem/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gem/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gem-inspect-deffile:

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