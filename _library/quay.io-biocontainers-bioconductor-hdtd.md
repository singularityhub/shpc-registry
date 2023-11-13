---
layout: container
name:  "quay.io/biocontainers/bioconductor-hdtd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hdtd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hdtd/container.yaml"
updated_at: "2023-11-13 02:31:59.359650"
latest: "1.34.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hdtd"

versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hdtd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hdtd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hdtd", "latest": {"1.34.1--r43hf17093f_0": "sha256:d0edf3936390cac49c5e92677aa6597d6c855295767d1a44217f71a003e4bd1d"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:ac44a5366106295c7e0a27e655a7c96cc62213290f9c493d41dd9169490787e2", "1.32.0--r42hc247a5b_0": "sha256:8e6990e0bbbcfcd895d3bba246233cd03068a40e4f44988a382b193772fe98d4", "1.32.0--r42hf17093f_1": "sha256:933125b046df7d6d74e09a67ce3e37d0d15daf5448bc76028ea69040206b0d4c", "1.34.1--r43hf17093f_0": "sha256:d0edf3936390cac49c5e92677aa6597d6c855295767d1a44217f71a003e4bd1d"}, "docker": "quay.io/biocontainers/bioconductor-hdtd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hdtd.
shpc-registry automated BioContainers addition for bioconductor-hdtd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hdtd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hdtd:1.34.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hdtd/1.34.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-hdtd/1.34.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hdtd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hdtd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hdtd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hdtd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hdtd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hdtd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hdtd

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