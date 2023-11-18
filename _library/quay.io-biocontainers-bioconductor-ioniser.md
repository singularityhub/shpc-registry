---
layout: container
name:  "quay.io/biocontainers/bioconductor-ioniser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ioniser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ioniser/container.yaml"
updated_at: "2023-11-18 03:03:27.836391"
latest: "2.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ioniser"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.22.0--r42hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.0--r40_0"
 - "2.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ioniser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ioniser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ioniser", "latest": {"2.24.0--r43hdfd78af_0": "sha256:c0c9d4da2ed1b7e7bbcf8bb70a0068bceeb9d609e83c481987eba10bd71b569f"}, "tags": {"2.8.0--r36_1": "sha256:08e6f60502cea1b5e09e21dee7314d2d8cb6a2c6fc3c62e9338e1c01d4d5dd7d", "2.22.0--r42hdfd78af_0": "sha256:17ffafaa3f254353d23ba3b97da0a95d589774742c0931e5b57bc29a4ea8214b", "2.18.0--r41hdfd78af_0": "sha256:f60b68d29ebd9a1c3da2eb6488a81252939f28c5241a0dfdbac9e6ac631123c2", "2.16.0--r41hdfd78af_0": "sha256:370670041d29532cf107f2e2ce20472a21945d0fabe72329d5efa3576835827c", "2.14.0--r40hdfd78af_1": "sha256:d3280b8780a29f5b4e6e3af3eb88f54d886d6523501bf82c5944346cf8f851ce", "2.12.0--r40_0": "sha256:093b50e5ce9e34c4340235bfd90ea0bc86dbac0d690d8db30b56ba3576f684fb", "2.24.0--r43hdfd78af_0": "sha256:c0c9d4da2ed1b7e7bbcf8bb70a0068bceeb9d609e83c481987eba10bd71b569f"}, "docker": "quay.io/biocontainers/bioconductor-ioniser", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ioniser.
shpc-registry automated BioContainers addition for bioconductor-ioniser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ioniser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ioniser:2.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ioniser/2.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ioniser/2.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ioniser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ioniser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ioniser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ioniser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ioniser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ioniser-inspect-deffile:

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