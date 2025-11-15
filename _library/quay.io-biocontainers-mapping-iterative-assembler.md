---
layout: container
name:  "quay.io/biocontainers/mapping-iterative-assembler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mapping-iterative-assembler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mapping-iterative-assembler/container.yaml"
updated_at: "2025-11-15 03:55:25.905486"
latest: "1.0--h503566f_7"
container_url: "https://biocontainers.pro/tools/mapping-iterative-assembler"
aliases:
 - "ccheck"
 - "ma"
 - "mia"
versions:
 - "1.0--h87f3376_3"
 - "1.0--hdbdd923_5"
 - "1.0--h503566f_6"
 - "1.0--h503566f_7"
description: "shpc-registry automated BioContainers addition for mapping-iterative-assembler"
config: {"url": "https://biocontainers.pro/tools/mapping-iterative-assembler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mapping-iterative-assembler", "latest": {"1.0--h503566f_7": "sha256:f85176bc4651be204d26cb119d1a734279999f3a83fb02b06771706abcff3eda"}, "tags": {"1.0--h87f3376_3": "sha256:6651ca06c2ca4c2e5edcbffc92080608f263013205e713f0fd5b0b49ea42edc6", "1.0--hdbdd923_5": "sha256:81c1dce388e8fd29641cd5a45f2ee13f1faec8f25f589257a260571323e4c1b1", "1.0--h503566f_6": "sha256:8df7c133f75997da9db108d21ae2a7039de5e8674e0d7b9110fad9d7b9b6dc18", "1.0--h503566f_7": "sha256:f85176bc4651be204d26cb119d1a734279999f3a83fb02b06771706abcff3eda"}, "docker": "quay.io/biocontainers/mapping-iterative-assembler", "aliases": {"ccheck": "/usr/local/bin/ccheck", "ma": "/usr/local/bin/ma", "mia": "/usr/local/bin/mia"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mapping-iterative-assembler.
shpc-registry automated BioContainers addition for mapping-iterative-assembler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mapping-iterative-assembler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mapping-iterative-assembler:1.0--h503566f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mapping-iterative-assembler/1.0--h503566f_7
$ module help quay.io/biocontainers/mapping-iterative-assembler/1.0--h503566f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mapping-iterative-assembler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mapping-iterative-assembler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mapping-iterative-assembler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mapping-iterative-assembler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mapping-iterative-assembler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mapping-iterative-assembler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccheck

```bash
$ singularity exec <container> /usr/local/bin/ccheck
$ podman run --it --rm --entrypoint /usr/local/bin/ccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ma

```bash
$ singularity exec <container> /usr/local/bin/ma
$ podman run --it --rm --entrypoint /usr/local/bin/ma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mia

```bash
$ singularity exec <container> /usr/local/bin/mia
$ podman run --it --rm --entrypoint /usr/local/bin/mia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mia   -v ${PWD} -w ${PWD} <container> -c " $@"
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