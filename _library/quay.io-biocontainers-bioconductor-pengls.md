---
layout: container
name:  "quay.io/biocontainers/bioconductor-pengls"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pengls/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pengls/container.yaml"
updated_at: "2025-08-23 03:40:13.472616"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pengls"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pengls"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pengls", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pengls", "latest": {"1.12.0--r44hdfd78af_0": "sha256:a5b600624ad50188fa3b5b775fb71d8bbc2a27ac0ead2c03ed92d8da806013a1"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:9e60990bc6a502901b608fac051aeea0597da4a61b39b9c63ba826f14a026271", "1.4.0--r42hdfd78af_0": "sha256:da736272cdc0ca5d6ffc4176e80505999e4ebd924dc38b118b0ea6fd545ac274", "1.6.0--r43hdfd78af_0": "sha256:f7be7df8f09fe46b239d8df97f5fe9fa720627807cab4049a93e144ca8d033a2", "1.8.0--r43hdfd78af_0": "sha256:1bd260643380f1adf7ed434e4fc7a177991a680981751826448aeb3235c9f67f", "1.12.0--r44hdfd78af_0": "sha256:a5b600624ad50188fa3b5b775fb71d8bbc2a27ac0ead2c03ed92d8da806013a1"}, "docker": "quay.io/biocontainers/bioconductor-pengls"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pengls.
shpc-registry automated BioContainers addition for bioconductor-pengls
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pengls
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pengls:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pengls/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pengls/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pengls-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pengls-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pengls-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pengls-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pengls-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pengls-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pengls

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