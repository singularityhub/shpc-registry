---
layout: container
name:  "quay.io/biocontainers/bioconductor-baalchip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-baalchip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-baalchip/container.yaml"
updated_at: "2025-12-12 03:37:38.103393"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-baalchip"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-baalchip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-baalchip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-baalchip", "latest": {"1.32.0--r44hdfd78af_0": "sha256:262aebfdd3f95262d1521ddb953ec25668f40f8ac761c69a637d01f1afed9962"}, "tags": {"1.8.0--r351_0": "sha256:1d0ea4f58905f442928163b9150f025e02653f3dd4ed99323bbdcfc3d880b159", "1.24.0--r42hdfd78af_0": "sha256:1665558175595aa97932bb840655bfe8689cb89998022bbd8f3c8596b743ff8c", "1.20.0--r41hdfd78af_0": "sha256:71cbd8499c07304b65ec297ed3d79a5f016280b57999059a13474ef9b8996812", "1.18.0--r41hdfd78af_0": "sha256:5ccefdef11abd2182f530704fe359f1eb0001de55fa10c3d487de73e2bfaf03d", "1.16.0--r40hdfd78af_1": "sha256:24fcc99d7602120f2379987a2411933c1bb66729ecf9a50356a28cb5a6357c0c", "1.14.0--r40_0": "sha256:24832fcd312c4e786b6056d852d2dfe93d380450b58ae1cfcc325c84c9de7137", "1.26.0--r43hdfd78af_0": "sha256:ac8602df3f7dda16e222973b4ea95fb71985ce5eabbcbf8ffda81f975c40cd24", "1.28.0--r43hdfd78af_0": "sha256:8fc2dfae49d6023aeaae0041dc2af56f7533e2c0956ca9fa25f983a178b5969c", "1.32.0--r44hdfd78af_0": "sha256:262aebfdd3f95262d1521ddb953ec25668f40f8ac761c69a637d01f1afed9962"}, "docker": "quay.io/biocontainers/bioconductor-baalchip", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-baalchip.
shpc-registry automated BioContainers addition for bioconductor-baalchip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-baalchip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-baalchip:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-baalchip/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-baalchip/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-baalchip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-baalchip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-baalchip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-baalchip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-baalchip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-baalchip-inspect-deffile:

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