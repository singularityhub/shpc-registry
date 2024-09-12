---
layout: container
name:  "quay.io/biocontainers/bioconductor-cfdnapro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cfdnapro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cfdnapro/container.yaml"
updated_at: "2024-09-12 02:59:23.762764"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cfdnapro"

versions:
 - "1.0.0--r41hdfd78af_3"
 - "1.4.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cfdnapro"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cfdnapro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cfdnapro", "latest": {"1.8.0--r43hdfd78af_0": "sha256:e727e196458c7269ad29c4ea7e434d339f73795a44723e21e0cb087d3380717a"}, "tags": {"1.0.0--r41hdfd78af_3": "sha256:64e9cdaa55b85d713ea239cfecda0dc609b9e59b1760658ce6c2ca74569b5c84", "1.4.0--r42hdfd78af_0": "sha256:6a424e91b59347080983f53ad56f968f19229cb90a33803eb105bc4d6b53e8b5", "1.8.0--r43hdfd78af_0": "sha256:e727e196458c7269ad29c4ea7e434d339f73795a44723e21e0cb087d3380717a"}, "docker": "quay.io/biocontainers/bioconductor-cfdnapro"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cfdnapro.
shpc-registry automated BioContainers addition for bioconductor-cfdnapro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cfdnapro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cfdnapro:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cfdnapro/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cfdnapro/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cfdnapro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cfdnapro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cfdnapro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cfdnapro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cfdnapro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cfdnapro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cfdnapro

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