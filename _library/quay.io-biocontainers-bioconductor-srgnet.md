---
layout: container
name:  "quay.io/biocontainers/bioconductor-srgnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-srgnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-srgnet/container.yaml"
updated_at: "2025-08-07 04:37:29.857928"
latest: "1.16.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-srgnet"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.10.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-srgnet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-srgnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-srgnet", "latest": {"1.16.0--r40hdfd78af_1": "sha256:4a3e6044d85e814ac9141dd98fb11897f26f63da9c87b0160396fe77dc05d46e"}, "tags": {"1.8.0--r351_0": "sha256:ddbfd94b4471b4c164cb57342c570214a450bc86de12951cf3b5890d30ad8710", "1.16.0--r40hdfd78af_1": "sha256:4a3e6044d85e814ac9141dd98fb11897f26f63da9c87b0160396fe77dc05d46e", "1.14.0--r40_0": "sha256:1e1acc812f89ba0219a6d1e38c215a7fe9a85741e124af5e5d5715266b31d77d", "1.12.0--r36_0": "sha256:9301194960a22268baa8738d3766ed6085c786c04817e6b9e2660d2539fb0d7e", "1.10.0--r36_1": "sha256:f5b480bb365085316e701a9442a0f3c5cf6343bf2b24401dc94695a14ed43370"}, "docker": "quay.io/biocontainers/bioconductor-srgnet", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-srgnet.
shpc-registry automated BioContainers addition for bioconductor-srgnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-srgnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-srgnet:1.16.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-srgnet/1.16.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-srgnet/1.16.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-srgnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-srgnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-srgnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-srgnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-srgnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-srgnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
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