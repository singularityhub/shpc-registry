---
layout: container
name:  "quay.io/biocontainers/bioconductor-derfinderplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-derfinderplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-derfinderplot/container.yaml"
updated_at: "2025-05-24 03:29:59.922742"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-derfinderplot"

versions:
 - "1.27.1--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-derfinderplot"
config: {"url": "https://biocontainers.pro/tools/bioconductor-derfinderplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-derfinderplot", "latest": {"1.40.0--r44hdfd78af_0": "sha256:32767080fff1b0a86d1721565375f21de2cdf5358cb108a6dd1d32dee91bfcac"}, "tags": {"1.27.1--r41hdfd78af_0": "sha256:718f141dc7b23f6e1fca5620b0557bf2d7bd736f2bddf85e5a65c250322f5bde", "1.32.0--r42hdfd78af_0": "sha256:e65346a109d1a133336b39e24ba97a670ddd3d6177d5c0d6b1cd8e3250de35a5", "1.34.0--r43hdfd78af_0": "sha256:b332c84bc60d760eb46279a139c03b64aaa4f060472c53f28a2de84ec0ee9a64", "1.36.0--r43hdfd78af_0": "sha256:5bec74d9cf4bf5a56fa86c357307ffba5323fd86370def2e0f5bddcb2c840259", "1.40.0--r44hdfd78af_0": "sha256:32767080fff1b0a86d1721565375f21de2cdf5358cb108a6dd1d32dee91bfcac"}, "docker": "quay.io/biocontainers/bioconductor-derfinderplot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-derfinderplot.
shpc-registry automated BioContainers addition for bioconductor-derfinderplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-derfinderplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-derfinderplot:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-derfinderplot/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-derfinderplot/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-derfinderplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-derfinderplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-derfinderplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-derfinderplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-derfinderplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-derfinderplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-derfinderplot

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