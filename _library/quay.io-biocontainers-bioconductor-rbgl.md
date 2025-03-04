---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbgl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbgl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbgl/container.yaml"
updated_at: "2025-03-04 03:27:40.720671"
latest: "1.82.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rbgl"

versions:
 - "1.70.0--r41hc247a5b_2"
 - "1.74.0--r42hc247a5b_0"
 - "1.74.0--r42hf17093f_1"
 - "1.76.0--r43hf17093f_0"
 - "1.78.0--r43hf17093f_0"
 - "1.78.0--r43hf17093f_1"
 - "1.82.0--r44he5774e6_0"
 - "1.82.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rbgl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbgl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbgl", "latest": {"1.82.0--r44he5774e6_1": "sha256:2362a5eaaee2f0ad5ddd43a0830f18a0b7aa71a5df5ce9fdbeba8a48dc8c3103"}, "tags": {"1.70.0--r41hc247a5b_2": "sha256:16e02b3a444b6621bc8a66fefed19b12c3215b40f05f29ea51ed5c020c456a8b", "1.74.0--r42hc247a5b_0": "sha256:d68d68fcee8c0d6fe2d90feebe7c6b0247c90a747970ce4b2f7085bcd81d165c", "1.74.0--r42hf17093f_1": "sha256:29bea56fdb4620e82384ae734567582b2071623e6d948ec069f668ae57e42bb3", "1.76.0--r43hf17093f_0": "sha256:315a7a78fb701be2185d512f32ded772312e4fc9d051eeb2d99bc3526116b563", "1.78.0--r43hf17093f_0": "sha256:8d3a6227bcac0de18f975d9963d418c27e421d2e8a0978891700c0f61cf1cd92", "1.78.0--r43hf17093f_1": "sha256:1ee44df6937ef932d96fe96d804d2cdb95ae359cc29262d96a6c1c4e1eab416c", "1.82.0--r44he5774e6_0": "sha256:fb1047d6091f5dd35a1757a85f33809b1a2f1d0fd65e0f52914f0bc24d6fd7c5", "1.82.0--r44he5774e6_1": "sha256:2362a5eaaee2f0ad5ddd43a0830f18a0b7aa71a5df5ce9fdbeba8a48dc8c3103"}, "docker": "quay.io/biocontainers/bioconductor-rbgl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbgl.
shpc-registry automated BioContainers addition for bioconductor-rbgl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbgl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbgl:1.82.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbgl/1.82.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-rbgl/1.82.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbgl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbgl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbgl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbgl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbgl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbgl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbgl

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