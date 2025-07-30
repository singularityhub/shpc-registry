---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgu34bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgu34bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgu34bprobe/container.yaml"
updated_at: "2025-07-30 04:26:26.085217"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rgu34bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rgu34bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgu34bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgu34bprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:b6d7928628791ec71f00fc08c99f931d861cfe60837ce30d4cfb62799c003cd7"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5f80fd9af1e61755d6e2f53b2bfe3acb48fad30666212a1988054a2008ea4b3d", "2.18.0--r42hdfd78af_10": "sha256:b66d74193d1087b06ab5a9714ed1a73d963d9eb42835ddedca796783670b08d1", "2.18.0--r43hdfd78af_11": "sha256:8ff7dc52049eafa20aeddeebb7faa8797b2cf1b6c554ee755fcf6cddfaf594c3", "2.18.0--r43hdfd78af_12": "sha256:efcfe285b6718b63ffba01d80c264f1c917ddd2a84152f04b1e8998b490bbb68", "2.18.0--r44hdfd78af_13": "sha256:b6d7928628791ec71f00fc08c99f931d861cfe60837ce30d4cfb62799c003cd7"}, "docker": "quay.io/biocontainers/bioconductor-rgu34bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgu34bprobe.
shpc-registry automated BioContainers addition for bioconductor-rgu34bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34bprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgu34bprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rgu34bprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgu34bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgu34bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgu34bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgu34bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgu34bprobe

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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