---
layout: container
name:  "quay.io/biocontainers/bioconductor-motifbreakr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-motifbreakr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-motifbreakr/container.yaml"
updated_at: "2023-05-07 03:12:13.656202"
latest: "2.12.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-motifbreakr"

versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.12.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-motifbreakr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-motifbreakr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-motifbreakr", "latest": {"2.12.0--r42hdfd78af_0": "sha256:f78e11632dd2a8879daf2135e0ccb4dab1754ce02d928c727e0ee676c197bf25"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:9077d4d6af8a4e5ed478361d845a49160576f11bc0497393ae06400df86a6552", "2.12.0--r42hdfd78af_0": "sha256:f78e11632dd2a8879daf2135e0ccb4dab1754ce02d928c727e0ee676c197bf25"}, "docker": "quay.io/biocontainers/bioconductor-motifbreakr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-motifbreakr.
shpc-registry automated BioContainers addition for bioconductor-motifbreakr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-motifbreakr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-motifbreakr:2.12.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-motifbreakr/2.12.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-motifbreakr/2.12.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-motifbreakr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifbreakr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifbreakr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-motifbreakr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-motifbreakr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-motifbreakr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-motifbreakr

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