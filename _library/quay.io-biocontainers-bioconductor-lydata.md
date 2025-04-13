---
layout: container
name:  "quay.io/biocontainers/bioconductor-lydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lydata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lydata/container.yaml"
updated_at: "2025-04-13 04:34:08.590258"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lydata"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.23.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.15.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lydata", "latest": {"1.32.0--r44hdfd78af_0": "sha256:86849edfed11fdf2601143182e58ceb01f0edc0d03cbc2d339af5fdf43e35e4e"}, "tags": {"1.8.0--r351_0": "sha256:930a880caf30c3523505db3633be0b8d99cfe91de272eb1244a97c82416b5db0", "1.23.0--r42hdfd78af_0": "sha256:16bf04321c08e20859e15b34703cceed7ccc529a48f23a64b2ff1546b3d7da79", "1.20.0--r41hdfd78af_1": "sha256:bde2c29b791b1d9aba6fb5552602249336501eadd0de2d570355c64b130c006b", "1.18.0--r41hdfd78af_0": "sha256:9e867d6475fdc57b23f660e61f79bc300470a2d795e36df49bcc9dd61433a602", "1.16.0--r40hdfd78af_1": "sha256:2366bcfde1d2e4d4d579d4603d6c30bcdff125aed2875376e56efed0e6ccacb7", "1.15.0--r40_0": "sha256:7c666bf6c981793b42e681e4a27ab6535ca55fe8f44b1d0c8a86ec60e322b197", "1.26.0--r43hdfd78af_0": "sha256:e3a0f88f6fdb1e71998a953b9193191eb63c7769278a60edcbcf31c84d12876e", "1.28.0--r43hdfd78af_0": "sha256:15ea43d51b8543c5d2ddb56c42bcd8571b9e8b5d8c4f1dbd6a494d121a8d8c68", "1.32.0--r44hdfd78af_0": "sha256:86849edfed11fdf2601143182e58ceb01f0edc0d03cbc2d339af5fdf43e35e4e"}, "docker": "quay.io/biocontainers/bioconductor-lydata", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lydata.
shpc-registry automated BioContainers addition for bioconductor-lydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lydata:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lydata/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lydata/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lydata-inspect-deffile:

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