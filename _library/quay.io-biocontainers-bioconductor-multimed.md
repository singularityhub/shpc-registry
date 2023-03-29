---
layout: container
name:  "quay.io/biocontainers/bioconductor-multimed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multimed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multimed/container.yaml"
updated_at: "2023-03-29 00:14:01.519984"
latest: "2.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multimed"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_0"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_1"
 - "2.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multimed"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multimed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multimed", "latest": {"2.20.0--r42hdfd78af_0": "sha256:8cb1a63a710003b1fced10d8fe8b5d7a8885b86967b5dc0fc7b6ddc6c3706e4a"}, "tags": {"2.8.0--r36_0": "sha256:fa672979f418ca1ec9801d612977b8c4b8c6e6d78db996c1fb3d10ab46ad3805", "2.20.0--r42hdfd78af_0": "sha256:8cb1a63a710003b1fced10d8fe8b5d7a8885b86967b5dc0fc7b6ddc6c3706e4a", "2.16.0--r41hdfd78af_0": "sha256:f72103a8fbf3857913dbf3750e09d730cd8a7d17b2b25063910bee9d6b7bc436", "2.14.0--r41hdfd78af_0": "sha256:3baf040798c19031a0026d26f3b8f8da79e5fbd393cf1cf81b82548c20b2e1c9", "2.12.0--r40hdfd78af_1": "sha256:9315df5b02012bd9cc873b9a6aeb33b61b98f88f6f8cfc8c653c1ac4a0c3a1cb", "2.10.0--r40_0": "sha256:5e66f77d17365899d1af9c1a09e36b23c376ec3097eeb30758b7e1949a399a01"}, "docker": "quay.io/biocontainers/bioconductor-multimed", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multimed.
shpc-registry automated BioContainers addition for bioconductor-multimed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multimed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multimed:2.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multimed/2.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multimed/2.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multimed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multimed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multimed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multimed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multimed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multimed-inspect-deffile:

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