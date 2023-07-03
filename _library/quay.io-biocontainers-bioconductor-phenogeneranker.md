---
layout: container
name:  "quay.io/biocontainers/bioconductor-phenogeneranker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phenogeneranker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phenogeneranker/container.yaml"
updated_at: "2023-07-03 03:42:32.598963"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phenogeneranker"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phenogeneranker"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phenogeneranker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phenogeneranker", "latest": {"1.6.0--r42hdfd78af_0": "sha256:f51f415590cbe67fff177ce01519c7b3a354ff0aff61f131a5ee8f9c5a2cd6ff"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:a468b8970a17f2d0415a6ff0e959911ee1453f4e571d463d7b4b4226477dc59e", "1.6.0--r42hdfd78af_0": "sha256:f51f415590cbe67fff177ce01519c7b3a354ff0aff61f131a5ee8f9c5a2cd6ff"}, "docker": "quay.io/biocontainers/bioconductor-phenogeneranker"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phenogeneranker.
shpc-registry automated BioContainers addition for bioconductor-phenogeneranker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phenogeneranker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phenogeneranker:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phenogeneranker/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phenogeneranker/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phenogeneranker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenogeneranker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenogeneranker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phenogeneranker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phenogeneranker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phenogeneranker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phenogeneranker

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