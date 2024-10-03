---
layout: container
name:  "quay.io/biocontainers/bioconductor-pickgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pickgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pickgene/container.yaml"
updated_at: "2024-10-03 02:56:32.116316"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pickgene"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pickgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pickgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pickgene", "latest": {"1.74.0--r43hdfd78af_0": "sha256:b06149d7f3756be55689811124de2f32c87d24ae64688fb5e0b07ca55a7a7e01"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:200ab601e7bbe83d6f36e1534e1d9b8e7645950383919baed374d60e7261e47c", "1.70.0--r42hdfd78af_0": "sha256:12f3a0534b80890245743485e8ebec391ab35d0a27ed7974eb72222716d784e1", "1.72.0--r43hdfd78af_0": "sha256:c92c335b8ad504bbca48b8e20abf943560bddb16a41c6be7ea5a2ddfc8328b67", "1.74.0--r43hdfd78af_0": "sha256:b06149d7f3756be55689811124de2f32c87d24ae64688fb5e0b07ca55a7a7e01"}, "docker": "quay.io/biocontainers/bioconductor-pickgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pickgene.
shpc-registry automated BioContainers addition for bioconductor-pickgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pickgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pickgene:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pickgene/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pickgene/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pickgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pickgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pickgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pickgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pickgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pickgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pickgene

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