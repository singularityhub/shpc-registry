---
layout: container
name:  "quay.io/biocontainers/bioconductor-beadsorted.saliva.epic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beadsorted.saliva.epic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beadsorted.saliva.epic/container.yaml"
updated_at: "2023-11-16 02:50:38.686810"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beadsorted.saliva.epic"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beadsorted.saliva.epic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beadsorted.saliva.epic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beadsorted.saliva.epic", "latest": {"1.8.0--r43hdfd78af_0": "sha256:e198ce2d4029bb79fe8c7ab6a38e59e7038642e9803fe7dafca2675537fa98f0"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:9f6aad366630fc278c4956415799ca5bf4e60d8692a9cb81e5de3ada88e49f0a", "1.6.0--r42hdfd78af_0": "sha256:13c1edb6e71aedf4b43b6656785de1a455a2e0398ca8622ee9b5f1e8f4ca9f26", "1.8.0--r43hdfd78af_0": "sha256:e198ce2d4029bb79fe8c7ab6a38e59e7038642e9803fe7dafca2675537fa98f0"}, "docker": "quay.io/biocontainers/bioconductor-beadsorted.saliva.epic"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beadsorted.saliva.epic.
shpc-registry automated BioContainers addition for bioconductor-beadsorted.saliva.epic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beadsorted.saliva.epic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beadsorted.saliva.epic:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beadsorted.saliva.epic/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-beadsorted.saliva.epic/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beadsorted.saliva.epic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadsorted.saliva.epic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadsorted.saliva.epic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beadsorted.saliva.epic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beadsorted.saliva.epic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beadsorted.saliva.epic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beadsorted.saliva.epic

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