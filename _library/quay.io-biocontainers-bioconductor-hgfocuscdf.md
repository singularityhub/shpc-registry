---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgfocuscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgfocuscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgfocuscdf/container.yaml"
updated_at: "2025-05-24 11:43:53.054259"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgfocuscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgfocuscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgfocuscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgfocuscdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:f52b7777839f28e4d73ca3cedae311a659ec1b50a8a9550df4aa975ac7eb7529"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:3d739305f69203437bd59fae897fd396403ab6b1a069709c691cfccc46cb708f", "2.18.0--r42hdfd78af_10": "sha256:41a2d360893e276b945483e7b9e12c3b675b024612e6e1953d185cd6302038b7", "2.18.0--r43hdfd78af_11": "sha256:97ce0019cb4e2626cd323a45adcfd7f6ef5036d0f36ab041bfa0529bd91bf1de", "2.18.0--r43hdfd78af_12": "sha256:51badb93ba7aa6e81437acab0d94ac2a4f65a212529e85ca0946d812054f136d", "2.18.0--r44hdfd78af_13": "sha256:f52b7777839f28e4d73ca3cedae311a659ec1b50a8a9550df4aa975ac7eb7529"}, "docker": "quay.io/biocontainers/bioconductor-hgfocuscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgfocuscdf.
shpc-registry automated BioContainers addition for bioconductor-hgfocuscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgfocuscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgfocuscdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgfocuscdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgfocuscdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgfocuscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgfocuscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgfocuscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgfocuscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgfocuscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgfocuscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgfocuscdf

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