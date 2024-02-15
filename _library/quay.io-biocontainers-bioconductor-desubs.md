---
layout: container
name:  "quay.io/biocontainers/bioconductor-desubs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-desubs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-desubs/container.yaml"
updated_at: "2024-02-15 03:00:33.971013"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-desubs"
aliases:
 - "idn2"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_1"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-desubs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-desubs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-desubs", "latest": {"1.28.0--r43hdfd78af_0": "sha256:77f39a41337c7c4a962575504372ae1da07ea0d65a737760a4b18115756e48f6"}, "tags": {"1.8.1--r351_1": "sha256:21ea4c0cc09f7b33b149d2ff2627a63513a7618c6b75ac74ddb4be29337c8d4d", "1.24.0--r42hdfd78af_0": "sha256:0f3d725f7c5ac0e67bf677246ae9cda591a725dd95b9a1b82a9551e31de013c9", "1.20.0--r41hdfd78af_0": "sha256:a661500bb9b5be68c9aa7df2e6d66261333940a91c3bd3059da0957a7f23f9c6", "1.18.0--r41hdfd78af_0": "sha256:e9fa1041962e4b8f7a70b1d5f9d248dc8346c154c021c151918d3ac66ce50358", "1.14.0--r40_0": "sha256:8abb2979519e1f49739600680a7463afb1ba91caa36ebe59230711c0fae53110", "1.12.0--r36_0": "sha256:2f1d3bd3f2b639b1932bb8630a5bddbea06e92452eeba1ce60f45f3068898ffb", "1.26.0--r43hdfd78af_0": "sha256:a9424cc420d0f830ca07a51f0eb1701faa027c6ccc20e6ed0258f18e61eb0c30", "1.28.0--r43hdfd78af_0": "sha256:77f39a41337c7c4a962575504372ae1da07ea0d65a737760a4b18115756e48f6"}, "docker": "quay.io/biocontainers/bioconductor-desubs", "aliases": {"idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-desubs.
shpc-registry automated BioContainers addition for bioconductor-desubs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-desubs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-desubs:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-desubs/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-desubs/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-desubs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-desubs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-desubs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-desubs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-desubs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-desubs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
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