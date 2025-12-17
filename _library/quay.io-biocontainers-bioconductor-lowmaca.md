---
layout: container
name:  "quay.io/biocontainers/bioconductor-lowmaca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lowmaca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lowmaca/container.yaml"
updated_at: "2025-12-17 16:19:49.533039"
latest: "1.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lowmaca"
aliases:
 - "clustalo"
versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lowmaca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lowmaca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lowmaca", "latest": {"1.28.0--r42hdfd78af_0": "sha256:ce4b7ebe4db24362313468bdedaedc3a51c4c5252454ff3e522bcef16cccbb40"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:a69f079b23fa0fa63775c6f4c9d9cb2ff8637c0394d2919d22f9e9853d2a69e2", "1.28.0--r42hdfd78af_0": "sha256:ce4b7ebe4db24362313468bdedaedc3a51c4c5252454ff3e522bcef16cccbb40"}, "docker": "quay.io/biocontainers/bioconductor-lowmaca", "aliases": {"clustalo": "/usr/local/bin/clustalo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lowmaca.
shpc-registry automated BioContainers addition for bioconductor-lowmaca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lowmaca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lowmaca:1.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lowmaca/1.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lowmaca/1.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lowmaca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lowmaca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lowmaca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lowmaca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lowmaca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lowmaca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
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