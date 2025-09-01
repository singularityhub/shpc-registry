---
layout: container
name:  "quay.io/biocontainers/bioconductor-citrusprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-citrusprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-citrusprobe/container.yaml"
updated_at: "2025-09-01 03:59:13.601415"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-citrusprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-citrusprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-citrusprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-citrusprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:0c17a87a6066a5a946d2cf410da77ee906841ae444a79edb0b29349f01dc215d"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:970a81dcce874b80d7c2d294110801fb3e897eb0e7b3ed051c9846b98d13ebb2", "2.18.0--r42hdfd78af_10": "sha256:c971cf1f2e8ad6f96b56b56ba2ddc521605fa47f57866fd6f366acdbc3e32319", "2.18.0--r43hdfd78af_11": "sha256:abfdbadcea10bad17106a1d2392bf31777db1f0f6b63bf93925e257176fc4046", "2.18.0--r43hdfd78af_12": "sha256:240af6bd31b808ca48a809a98ee714b7d962df172d36d2e66fa6813ac7d89e33", "2.18.0--r44hdfd78af_13": "sha256:0c17a87a6066a5a946d2cf410da77ee906841ae444a79edb0b29349f01dc215d"}, "docker": "quay.io/biocontainers/bioconductor-citrusprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-citrusprobe.
shpc-registry automated BioContainers addition for bioconductor-citrusprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-citrusprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-citrusprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-citrusprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-citrusprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-citrusprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-citrusprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-citrusprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-citrusprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-citrusprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-citrusprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-citrusprobe

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