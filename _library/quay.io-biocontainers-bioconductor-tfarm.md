---
layout: container
name:  "quay.io/biocontainers/bioconductor-tfarm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tfarm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tfarm/container.yaml"
updated_at: "2024-01-10 08:44:00.984928"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tfarm"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.6.0--r36_1"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tfarm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tfarm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tfarm", "latest": {"1.24.0--r43hdfd78af_0": "sha256:a131a36c3f6580702ef6e4fdc70d67b7bf925d929b9cfbd4ab7d85603197eea0"}, "tags": {"1.6.0--r36_1": "sha256:55deb0fa415f67c4df6c8daba1bb9d33ccc0f3dfeb3be786bd3ce3486d7f3972", "1.20.0--r42hdfd78af_0": "sha256:b958b312a52fe193da1c9414ad78f840a500d4c51bc8d0613f054c6745620293", "1.16.0--r41hdfd78af_0": "sha256:fbfd72474e1115b580d81dda1c70772d15fb55956778fceb2fca415b07ad2bcf", "1.14.0--r41hdfd78af_0": "sha256:e36ef335e85a060fe182f0413d73d68c6f5324bbb87ac12029a32b91a4644315", "1.12.0--r40hdfd78af_1": "sha256:5ffc90db31a8be25cf8083da290e4b228a4f17162fcdbe8cb3095a7db7522ceb", "1.10.0--r40_0": "sha256:f63a5d8308c66fa5c038b71413745feafda8ea40fe15ddacaf1820cee23708f0", "1.22.0--r43hdfd78af_0": "sha256:e4ae87e1df8f0ff21342a6aeb59baa6bfdd1d38d7cebea2d0be7b6698c486281", "1.24.0--r43hdfd78af_0": "sha256:a131a36c3f6580702ef6e4fdc70d67b7bf925d929b9cfbd4ab7d85603197eea0"}, "docker": "quay.io/biocontainers/bioconductor-tfarm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tfarm.
shpc-registry automated BioContainers addition for bioconductor-tfarm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tfarm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tfarm:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tfarm/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tfarm/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tfarm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfarm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfarm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tfarm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tfarm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tfarm-inspect-deffile:

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