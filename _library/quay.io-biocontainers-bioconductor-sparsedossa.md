---
layout: container
name:  "quay.io/biocontainers/bioconductor-sparsedossa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sparsedossa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sparsedossa/container.yaml"
updated_at: "2025-05-13 03:13:40.543221"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sparsedossa"
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
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sparsedossa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sparsedossa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sparsedossa", "latest": {"1.24.0--r43hdfd78af_0": "sha256:dd6adbd05622a5778c79676b8d8b7e200b174d36b8cc44cc22befff98705d549"}, "tags": {"1.8.0--r36_1": "sha256:87d997889e1efbc83b5fe0c460fc78ddf83fe3fde0bfa0afa6e10736514a0b46", "1.22.0--r42hdfd78af_0": "sha256:7fc27d9aa77930f5b55a66755284bfe1b37b055181ade209a83463a7961cb121", "1.18.0--r41hdfd78af_0": "sha256:5552da8df6a2ce6d21f099fe09679a7744ec58fce72483d025d19db3cd31ae2e", "1.16.0--r41hdfd78af_0": "sha256:d5b85e00a523b00b66dbecdc82307ecab76d5fce864dc7918a913a1f3100a1a7", "1.14.0--r40hdfd78af_1": "sha256:57a41485916338504da9b1297f4b3330c54d24878bc2514b07bbe6592180ea34", "1.12.0--r40_0": "sha256:5e3fd5d92a7e2a17fe848202facddace183904a8b7a04197b175537548310db2", "1.24.0--r43hdfd78af_0": "sha256:dd6adbd05622a5778c79676b8d8b7e200b174d36b8cc44cc22befff98705d549"}, "docker": "quay.io/biocontainers/bioconductor-sparsedossa", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sparsedossa.
shpc-registry automated BioContainers addition for bioconductor-sparsedossa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsedossa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsedossa:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sparsedossa/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sparsedossa/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sparsedossa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsedossa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsedossa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sparsedossa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sparsedossa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sparsedossa-inspect-deffile:

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