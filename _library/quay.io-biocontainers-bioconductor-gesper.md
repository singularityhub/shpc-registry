---
layout: container
name:  "quay.io/biocontainers/bioconductor-gesper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gesper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gesper/container.yaml"
updated_at: "2024-06-25 02:47:48.188906"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gesper"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.31.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gesper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gesper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gesper", "latest": {"1.34.0--r43hdfd78af_0": "sha256:ec6a5bcccf164e5ee7a6ae4d7aaabfab5ce5a18856ed85700b9777b96b9964dc"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:dae89c09e791c32763813f5f6834aa8344ead1cdb40dc0acc99620dac5a5616d", "1.30.0--r42hdfd78af_0": "sha256:45d2f7bda3eb3a1bdf79e0805bdcd7a9e3da6a453fc9502f89eb459895d434ed", "1.31.0--r43hdfd78af_0": "sha256:07e2de3f68c061a2433aedaf8ada5b5b1c10a8bde4daa0d58730f8602d035635", "1.34.0--r43hdfd78af_0": "sha256:ec6a5bcccf164e5ee7a6ae4d7aaabfab5ce5a18856ed85700b9777b96b9964dc"}, "docker": "quay.io/biocontainers/bioconductor-gesper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gesper.
shpc-registry automated BioContainers addition for bioconductor-gesper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gesper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gesper:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gesper/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gesper/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gesper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gesper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gesper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gesper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gesper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gesper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gesper

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