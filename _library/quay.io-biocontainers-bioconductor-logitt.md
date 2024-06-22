---
layout: container
name:  "quay.io/biocontainers/bioconductor-logitt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-logitt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-logitt/container.yaml"
updated_at: "2024-06-22 02:46:28.626595"
latest: "1.58.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-logitt"

versions:
 - "1.52.0--r41hc0cfd56_2"
 - "1.56.0--r42hc0cfd56_0"
 - "1.56.0--r42ha9d7317_1"
 - "1.58.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-logitt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-logitt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-logitt", "latest": {"1.58.0--r43ha9d7317_0": "sha256:7bd0ebc4f066ce4d4b86e3dc39346f81214c179baab72c97341070575772dccd"}, "tags": {"1.52.0--r41hc0cfd56_2": "sha256:c31b2ca44009ad9a48eb79cc8ebfb58d507e595a0ba4c4e2f6f15a1a0d3858bc", "1.56.0--r42hc0cfd56_0": "sha256:ea4841395c939a3fab78b2ca5610064622b7b1136094a64b4cc6b0e8b1082d11", "1.56.0--r42ha9d7317_1": "sha256:8baf4856e3c4427db258d77fd7e72998d636c2c525035eac1c209b035964836c", "1.58.0--r43ha9d7317_0": "sha256:7bd0ebc4f066ce4d4b86e3dc39346f81214c179baab72c97341070575772dccd"}, "docker": "quay.io/biocontainers/bioconductor-logitt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-logitt.
shpc-registry automated BioContainers addition for bioconductor-logitt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-logitt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-logitt:1.58.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-logitt/1.58.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-logitt/1.58.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-logitt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-logitt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-logitt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-logitt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-logitt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-logitt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-logitt

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