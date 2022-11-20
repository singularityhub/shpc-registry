---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowspecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowspecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowspecs/container.yaml"
updated_at: "2022-11-20 00:47:19.766144"
latest: "1.12.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowspecs"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowspecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowspecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowspecs", "latest": {"1.12.0--r42hdfd78af_0": "sha256:d75a67dfd6f476840befb21c6e94e76fc94cf4cf38767c1b135df27bd2c76243"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:2435895856456952940ca2b305fd7635844b59b5f5f082285904c8d5a5187b64", "1.12.0--r42hdfd78af_0": "sha256:d75a67dfd6f476840befb21c6e94e76fc94cf4cf38767c1b135df27bd2c76243"}, "docker": "quay.io/biocontainers/bioconductor-flowspecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowspecs.
shpc-registry automated BioContainers addition for bioconductor-flowspecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowspecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowspecs:1.12.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowspecs/1.12.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowspecs/1.12.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowspecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowspecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowspecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowspecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowspecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowspecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowspecs

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