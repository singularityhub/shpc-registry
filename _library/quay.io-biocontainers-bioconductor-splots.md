---
layout: container
name:  "quay.io/biocontainers/bioconductor-splots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splots/container.yaml"
updated_at: "2025-09-21 03:33:35.590822"
latest: "1.72.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splots"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.64.0--r42hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.72.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splots"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splots", "latest": {"1.72.0--r44hdfd78af_0": "sha256:3e4359278de0a79c7b960581ed20640c24d8e4b4af0a3610474a961fcb4813ae"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:569a33cf9201ef27bc6f6853ab70b862f9d61eca635f8917d59f670abfea382d", "1.64.0--r42hdfd78af_0": "sha256:be3b3d3512e80da781cc498afe8c66127046424713c8319ef73234af37236e2b", "1.66.0--r43hdfd78af_0": "sha256:18115d1098817ec5030b91909c17ad3f6535dd68a9ddc7cd8988ca2ff4b7210f", "1.68.0--r43hdfd78af_0": "sha256:e4cc495405f518c0c22ae0ab2ec67f56834b2259020c3ddd111ce8d8e3ff1252", "1.72.0--r44hdfd78af_0": "sha256:3e4359278de0a79c7b960581ed20640c24d8e4b4af0a3610474a961fcb4813ae"}, "docker": "quay.io/biocontainers/bioconductor-splots"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splots.
shpc-registry automated BioContainers addition for bioconductor-splots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splots:1.72.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splots/1.72.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-splots/1.72.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-splots

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