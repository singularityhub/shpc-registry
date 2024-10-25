---
layout: container
name:  "quay.io/biocontainers/bioconductor-mina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mina/container.yaml"
updated_at: "2024-10-25 03:32:10.792679"
latest: "1.10.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mina"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mina"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mina", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mina", "latest": {"1.10.0--r43hf17093f_1": "sha256:dd8e714bac9d19ffb4d7a3e039c4294e61f8a5a5667a54f8ea125ba2008d9588"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:a1f5d5bc1d4201740e3f73aa86767f1e81e11ae5afec1f0cd528a8981fd72ff8", "1.6.0--r42hc247a5b_0": "sha256:f9bd85c2ade4ad1c2f5883528e31898053194fad1f91c7d12f0d6e0a4b8deb3c", "1.6.0--r42hf17093f_1": "sha256:56c0818baa7f4fe0588fe87472ddc56e52d5a629f3d6b598bbec6daef86e41d2", "1.8.0--r43hf17093f_0": "sha256:71185796c945ee911735830cac2b9705c55bfc99326ff874e0ad928131222d2d", "1.10.0--r43hf17093f_1": "sha256:dd8e714bac9d19ffb4d7a3e039c4294e61f8a5a5667a54f8ea125ba2008d9588"}, "docker": "quay.io/biocontainers/bioconductor-mina"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mina.
shpc-registry automated BioContainers addition for bioconductor-mina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mina:1.10.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mina/1.10.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-mina/1.10.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mina-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mina

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