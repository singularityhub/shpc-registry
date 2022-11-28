---
layout: container
name:  "quay.io/biocontainers/bioconductor-htseqgenie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htseqgenie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htseqgenie/container.yaml"
updated_at: "2022-11-28 03:29:03.001081"
latest: "4.27.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-htseqgenie"

versions:
 - "4.24.0--r41hdfd78af_0"
 - "4.27.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-htseqgenie"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htseqgenie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htseqgenie", "latest": {"4.27.0--r42hdfd78af_0": "sha256:c9a6d83a0f0faaa547f85722811ffc47f33856f959e643d3e3dcd80dd15d1009"}, "tags": {"4.24.0--r41hdfd78af_0": "sha256:ed867da011fc173d46c793be4a6b0d6979d8409f1f1e115e8e86912f54c20ca1", "4.27.0--r42hdfd78af_0": "sha256:c9a6d83a0f0faaa547f85722811ffc47f33856f959e643d3e3dcd80dd15d1009"}, "docker": "quay.io/biocontainers/bioconductor-htseqgenie"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htseqgenie.
shpc-registry automated BioContainers addition for bioconductor-htseqgenie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htseqgenie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htseqgenie:4.27.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htseqgenie/4.27.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-htseqgenie/4.27.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htseqgenie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htseqgenie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htseqgenie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htseqgenie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htseqgenie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htseqgenie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htseqgenie

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