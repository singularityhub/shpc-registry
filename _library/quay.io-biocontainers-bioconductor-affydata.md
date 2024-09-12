---
layout: container
name:  "quay.io/biocontainers/bioconductor-affydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affydata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affydata/container.yaml"
updated_at: "2024-09-12 17:10:32.320620"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affydata"

versions:
 - "1.42.0--r41hdfd78af_1"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.48.1--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affydata", "latest": {"1.50.0--r43hdfd78af_0": "sha256:df418017cfea7a9ab8d78195f98a48f12c123cd3810a8a21ce20bfd4276fe996"}, "tags": {"1.42.0--r41hdfd78af_1": "sha256:8d220eb8a24a7a943bb27e30c66b18f6c5e566b32cc4b32960272a4c86789b37", "1.46.0--r42hdfd78af_0": "sha256:79f1df927469bb141b518735b9ee2fb44fb5dfe16b1ae4a67370b1dc5d2cd7bc", "1.48.0--r43hdfd78af_0": "sha256:34b1f1a3d66ecfbf972fe3a4464c88584e5942ae717253bebf000c1279ac47e2", "1.48.1--r43hdfd78af_0": "sha256:e48e398b22f40468e551c10b50b7274ddab75d12f50a6a0484834b6db1ef2c10", "1.50.0--r43hdfd78af_0": "sha256:df418017cfea7a9ab8d78195f98a48f12c123cd3810a8a21ce20bfd4276fe996"}, "docker": "quay.io/biocontainers/bioconductor-affydata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affydata.
shpc-registry automated BioContainers addition for bioconductor-affydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affydata:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affydata/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affydata/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affydata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affydata

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