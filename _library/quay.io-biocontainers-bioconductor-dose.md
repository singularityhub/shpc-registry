---
layout: container
name:  "quay.io/biocontainers/bioconductor-dose"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dose/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dose/container.yaml"
updated_at: "2023-02-07 03:15:01.226639"
latest: "3.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dose"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "3.8.0--r351_0"
 - "3.24.0--r42hdfd78af_0"
 - "3.20.0--r41hdfd78af_0"
 - "3.18.0--r41hdfd78af_0"
 - "3.16.0--r40hdfd78af_1"
 - "3.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dose"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dose", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dose", "latest": {"3.24.0--r42hdfd78af_0": "sha256:e9e5938d4b07e207c2918ad5d4bcad3917aa71324f9b24c0a96000c0ee9e1d51"}, "tags": {"3.8.0--r351_0": "sha256:5b96c05496622543184833e2b7e0b0926540abd17893c4e437aa1f8453ad4e73", "3.24.0--r42hdfd78af_0": "sha256:e9e5938d4b07e207c2918ad5d4bcad3917aa71324f9b24c0a96000c0ee9e1d51", "3.20.0--r41hdfd78af_0": "sha256:8b90b33fe28ad723ae00c286df15f1c4a58be2359427bcaaae0cd1f43739376f", "3.18.0--r41hdfd78af_0": "sha256:d17b7495e2cf4d24b21da3d1bf3a03d4cfc61cc1cef2837b6d2ef2357bcab5ea", "3.16.0--r40hdfd78af_1": "sha256:5968fd056b3b5f068fdf90309cc5ba90bd1f198677b3c129899a0d23cd38042d", "3.14.0--r40_0": "sha256:d928171af9086438a7011bb7f4e167139b0186ff706ac5adcf35a0a457668bd1"}, "docker": "quay.io/biocontainers/bioconductor-dose", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dose.
shpc-registry automated BioContainers addition for bioconductor-dose
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dose
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dose:3.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dose/3.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dose/3.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dose-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dose-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dose-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dose-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dose-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dose-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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