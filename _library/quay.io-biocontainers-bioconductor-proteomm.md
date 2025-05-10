---
layout: container
name:  "quay.io/biocontainers/bioconductor-proteomm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proteomm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proteomm/container.yaml"
updated_at: "2025-05-10 03:17:47.446488"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proteomm"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proteomm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proteomm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proteomm", "latest": {"1.24.0--r44hdfd78af_0": "sha256:130b6727dfa5acd500c1624199fb8e6d9586554a76269e7d565ed434f854d7f4"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:2eabcc21f2ada24c07de4edd32496a60db2729c13a0117505bd9bf227f479b1a", "1.12.0--r41hdfd78af_0": "sha256:fb434901857e46997ef511e95413dfb021e541f69d17eb596b42070e87fe6aae", "1.10.0--r41hdfd78af_0": "sha256:77bee2273bb778c9fdebdf771953745ae07ba832515ca18b2f20405b9a532cf2", "1.16.0--r42hdfd78af_0": "sha256:c8dc5d4d0dfacdb83edcb73756b27d247c4775cda30678a896986f1486975202", "1.18.0--r43hdfd78af_0": "sha256:cfabd9c5728a1e91effa8e35e601018041f31147c0360f554b4d9810a9db0004", "1.20.0--r43hdfd78af_0": "sha256:4ce4fb1fa4349cdb8130de57601f5eb19be8160deaf447b5a7c29226d45f956b", "1.24.0--r44hdfd78af_0": "sha256:130b6727dfa5acd500c1624199fb8e6d9586554a76269e7d565ed434f854d7f4"}, "docker": "quay.io/biocontainers/bioconductor-proteomm", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proteomm.
shpc-registry automated BioContainers addition for bioconductor-proteomm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proteomm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proteomm:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proteomm/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-proteomm/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proteomm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proteomm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proteomm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proteomm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proteomm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proteomm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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