---
layout: container
name:  "quay.io/biocontainers/bioconductor-human660quadv1acrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human660quadv1acrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human660quadv1acrlmm/container.yaml"
updated_at: "2024-02-01 02:38:37.267421"
latest: "1.0.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-human660quadv1acrlmm"

versions:
 - "1.0.3--r41hdfd78af_9"
 - "1.0.3--r42hdfd78af_10"
 - "1.0.3--r43hdfd78af_11"
 - "1.0.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-human660quadv1acrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human660quadv1acrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human660quadv1acrlmm", "latest": {"1.0.3--r43hdfd78af_12": "sha256:de5f5ab1c688fb52450905a74cda92bbbbb19fcd517d9261cd469575fe286697"}, "tags": {"1.0.3--r41hdfd78af_9": "sha256:235c3baf6ac80d9434800137b51d94d29762dfd91c5b110a4c1ef40a5a77a892", "1.0.3--r42hdfd78af_10": "sha256:7bdb3b87f6364100a392394580e0b80c4ab78313ca881ff69a8e9d9db4325d8c", "1.0.3--r43hdfd78af_11": "sha256:36af57ec6f7a64a88ace3183a0391967a97ccebff380cb24a0323a6bc17d2d7b", "1.0.3--r43hdfd78af_12": "sha256:de5f5ab1c688fb52450905a74cda92bbbbb19fcd517d9261cd469575fe286697"}, "docker": "quay.io/biocontainers/bioconductor-human660quadv1acrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human660quadv1acrlmm.
shpc-registry automated BioContainers addition for bioconductor-human660quadv1acrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human660quadv1acrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human660quadv1acrlmm:1.0.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human660quadv1acrlmm/1.0.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-human660quadv1acrlmm/1.0.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human660quadv1acrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human660quadv1acrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human660quadv1acrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human660quadv1acrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human660quadv1acrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human660quadv1acrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human660quadv1acrlmm

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