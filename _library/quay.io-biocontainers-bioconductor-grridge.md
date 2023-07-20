---
layout: container
name:  "quay.io/biocontainers/bioconductor-grridge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-grridge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-grridge/container.yaml"
updated_at: "2023-07-20 03:17:04.821477"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-grridge"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-grridge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-grridge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-grridge", "latest": {"1.22.0--r42hdfd78af_0": "sha256:1269f4fdd9f81c222cbd69decc3a4389d9487918ed78689e3664a1d9c9b37920"}, "tags": {"1.8.0--r36_1": "sha256:b0af9194a9dbb239c9697ffc90529e5c3874f47145c80664c4b7a982cd35af28", "1.22.0--r42hdfd78af_0": "sha256:1269f4fdd9f81c222cbd69decc3a4389d9487918ed78689e3664a1d9c9b37920", "1.18.0--r41hdfd78af_0": "sha256:89d3cccf4363158030c628d954572a7961434133cb82f395f9969d1afbb5c4d1", "1.16.0--r41hdfd78af_0": "sha256:c1dfe813ea40c05980c3c2aaa018375561f762c82843714c0906c2d0195b7bfd", "1.14.0--r40hdfd78af_1": "sha256:896a4e55b08771c4ef47439adb4032d94bae616ee21c7e04670a4389415ab000", "1.12.0--r40_0": "sha256:6479ad4e2ac6b1918d94b81d3adda9bf51bf897a76fca37ef291afc807d44b3b"}, "docker": "quay.io/biocontainers/bioconductor-grridge", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-grridge.
shpc-registry automated BioContainers addition for bioconductor-grridge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-grridge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-grridge:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-grridge/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-grridge/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-grridge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grridge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grridge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-grridge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-grridge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-grridge-inspect-deffile:

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