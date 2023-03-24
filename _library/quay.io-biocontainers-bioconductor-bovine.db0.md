---
layout: container
name:  "quay.io/biocontainers/bioconductor-bovine.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bovine.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bovine.db0/container.yaml"
updated_at: "2023-03-24 03:15:15.593761"
latest: "3.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bovine.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bovine.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bovine.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bovine.db0", "latest": {"3.16.0--r42hdfd78af_0": "sha256:9cfb38d8d9c45ef17f66c0ee6939144f42ee0651b5dfc7d5b5da62ad0b097c6b"}, "tags": {"3.8.2--r36_1": "sha256:a23f774e850f5b7c4e87b5553aafe4a040f4e0105ee7323eaf610dd12d31d2ff", "3.16.0--r42hdfd78af_0": "sha256:9cfb38d8d9c45ef17f66c0ee6939144f42ee0651b5dfc7d5b5da62ad0b097c6b", "3.14.0--r41hdfd78af_1": "sha256:413ab4f04e44d751c7de6b7eb143e9ef150ee10e16c790f37312cea7f18d59e3", "3.13.0--r41hdfd78af_0": "sha256:54470c367199dca5f07c6dfe3c62529e115132e905901b7c4aec9d7f26c00f99", "3.12.0--r40hdfd78af_1": "sha256:46d812849dc85977d64c7e2e9c3cc084673464f2a6d6bf36b9194832beb3e4d8", "3.11.2--r40_0": "sha256:fddce8a7c0692c9f95b234cb94b7c0eb83ce65253285f8b36b7515820cccab2d"}, "docker": "quay.io/biocontainers/bioconductor-bovine.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bovine.db0.
shpc-registry automated BioContainers addition for bioconductor-bovine.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bovine.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bovine.db0:3.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bovine.db0/3.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bovine.db0/3.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bovine.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bovine.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bovine.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bovine.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bovine.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bovine.db0-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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