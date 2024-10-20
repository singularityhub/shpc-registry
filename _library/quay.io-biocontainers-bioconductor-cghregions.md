---
layout: container
name:  "quay.io/biocontainers/bioconductor-cghregions"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cghregions/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cghregions/container.yaml"
updated_at: "2024-10-20 03:23:24.268900"
latest: "1.60.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cghregions"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cghregions"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cghregions", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cghregions", "latest": {"1.60.0--r43hdfd78af_0": "sha256:fa9221b9c95a0f7c8187da20a40518821d0fab62e6870e2652c9d15ed228eb9e"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:202164e59b7ee2d82de821cbad01cfee377a4f818f4142781b450f115aadc443", "1.56.0--r42hdfd78af_0": "sha256:dbd1e15a73658cedd55d2713d20a6118c36c8c854242b78b78456b659e2f8a7f", "1.58.0--r43hdfd78af_0": "sha256:7df4f801d9a8c8556de5cfa4f4cd000544c95c1271ff71903ac08dfb8e210383", "1.60.0--r43hdfd78af_0": "sha256:fa9221b9c95a0f7c8187da20a40518821d0fab62e6870e2652c9d15ed228eb9e"}, "docker": "quay.io/biocontainers/bioconductor-cghregions"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cghregions.
shpc-registry automated BioContainers addition for bioconductor-cghregions
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cghregions
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cghregions:1.60.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cghregions/1.60.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cghregions/1.60.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cghregions-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghregions-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghregions-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cghregions-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cghregions-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cghregions-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cghregions

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