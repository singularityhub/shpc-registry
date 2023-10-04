---
layout: container
name:  "quay.io/biocontainers/bioconductor-synergyfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-synergyfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-synergyfinder/container.yaml"
updated_at: "2023-10-04 04:36:52.329537"
latest: "3.8.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-synergyfinder"
aliases:
 - "pandoc"
versions:
 - "3.2.2--r41hdfd78af_0"
 - "3.6.0--r42hdfd78af_0"
 - "3.8.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-synergyfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-synergyfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-synergyfinder", "latest": {"3.8.2--r43hdfd78af_0": "sha256:899bfae152d3e7df8f95759988c1d404e1b727ffd8051dcae135ff888a0aeb0b"}, "tags": {"3.2.2--r41hdfd78af_0": "sha256:438e38e7a30725aae92b1600d0f4685c6f5a6e8a91b20a83a761d7a8495d69ad", "3.6.0--r42hdfd78af_0": "sha256:aeb5efc8ab61be3ec06d34ecbab9e4b05f2c4afb3f260ad020cc9be65efc2380", "3.8.2--r43hdfd78af_0": "sha256:899bfae152d3e7df8f95759988c1d404e1b727ffd8051dcae135ff888a0aeb0b"}, "docker": "quay.io/biocontainers/bioconductor-synergyfinder", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-synergyfinder.
shpc-registry automated BioContainers addition for bioconductor-synergyfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-synergyfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-synergyfinder:3.8.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-synergyfinder/3.8.2--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-synergyfinder/3.8.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-synergyfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synergyfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synergyfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-synergyfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-synergyfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-synergyfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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