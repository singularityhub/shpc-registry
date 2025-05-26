---
layout: container
name:  "quay.io/biocontainers/bioconductor-clstutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clstutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clstutils/container.yaml"
updated_at: "2025-05-26 04:05:12.003941"
latest: "1.54.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clstutils"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.54.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clstutils"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clstutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clstutils", "latest": {"1.54.0--r44hdfd78af_0": "sha256:2aa9e872334c43724d123dae93fc01489e25beb5fd3c6ae2096a443eb706c72f"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:693918aa9d99325949cd11d0048d678ef3a2cea81a86ef87914b4a0eb156b81f", "1.46.0--r42hdfd78af_0": "sha256:775df1df442dc87badb27d88c1764bae76b40e8946a8373cea00e30221218a71", "1.48.0--r43hdfd78af_0": "sha256:a261fb04bc00f3e69db76d84da81c797f5066c23f9cd79e235fb901ed8c12cde", "1.50.0--r43hdfd78af_0": "sha256:76c0f8d963b8348b0bd6917e98c2a102613ed99d28d009c54164feb64991ee9e", "1.54.0--r44hdfd78af_0": "sha256:2aa9e872334c43724d123dae93fc01489e25beb5fd3c6ae2096a443eb706c72f"}, "docker": "quay.io/biocontainers/bioconductor-clstutils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clstutils.
shpc-registry automated BioContainers addition for bioconductor-clstutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clstutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clstutils:1.54.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clstutils/1.54.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clstutils/1.54.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clstutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clstutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clstutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clstutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clstutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clstutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clstutils

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