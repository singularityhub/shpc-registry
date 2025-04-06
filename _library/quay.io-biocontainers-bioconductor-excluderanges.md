---
layout: container
name:  "quay.io/biocontainers/bioconductor-excluderanges"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-excluderanges/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-excluderanges/container.yaml"
updated_at: "2025-04-06 03:22:02.951241"
latest: "0.99.8--r44hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-excluderanges"

versions:
 - "0.99.6--r41hdfd78af_1"
 - "0.99.6--r42hdfd78af_2"
 - "0.99.8--r43hdfd78af_0"
 - "0.99.8--r43hdfd78af_1"
 - "0.99.8--r44hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-excluderanges"
config: {"url": "https://biocontainers.pro/tools/bioconductor-excluderanges", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-excluderanges", "latest": {"0.99.8--r44hdfd78af_2": "sha256:f66cb7247a6f6a369258225f8f908ac818685d428e1ec2bfdff0439dd7d8d4ae"}, "tags": {"0.99.6--r41hdfd78af_1": "sha256:370db92af5f30ed99b4b6fb9912af0021d636efe48956d8860ce3d1b86646909", "0.99.6--r42hdfd78af_2": "sha256:d8665a88f8c5082659fa7c7bc7b4abcbb2399490cb1f96bd7193a0184217d36d", "0.99.8--r43hdfd78af_0": "sha256:cfb7061045db11828da8271e93d20d78d856916a6402114d4702d8c85480a3ea", "0.99.8--r43hdfd78af_1": "sha256:18942a18f88a2dd218f5e7b1ee5d5e7f21038db8045d8b0572c4b8eb23c8da75", "0.99.8--r44hdfd78af_2": "sha256:f66cb7247a6f6a369258225f8f908ac818685d428e1ec2bfdff0439dd7d8d4ae"}, "docker": "quay.io/biocontainers/bioconductor-excluderanges"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-excluderanges.
shpc-registry automated BioContainers addition for bioconductor-excluderanges
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-excluderanges
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-excluderanges:0.99.8--r44hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-excluderanges/0.99.8--r44hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-excluderanges/0.99.8--r44hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-excluderanges-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-excluderanges-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-excluderanges-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-excluderanges-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-excluderanges-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-excluderanges-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-excluderanges

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