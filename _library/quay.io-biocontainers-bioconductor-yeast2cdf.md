---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeast2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeast2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeast2cdf/container.yaml"
updated_at: "2024-03-19 02:29:20.386821"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-yeast2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-yeast2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeast2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeast2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:53dd8bf12d04b54118a0eb08db7c1bc64b14c98775e54c2a80c9d956f2851f21"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:3892ce137d3ffcd977f9f955336726c8fe2256f9f35c54b992077f23c7dcb4b3", "2.18.0--r42hdfd78af_10": "sha256:33a69035f307617dad5838bec7b63e9289570da2d091caecd7216c241b45789a", "2.18.0--r43hdfd78af_11": "sha256:8f5766d17486af8cf151ccc0ce3bd6c5d0341a18ba4de1ee895657f0260f32f8", "2.18.0--r43hdfd78af_12": "sha256:53dd8bf12d04b54118a0eb08db7c1bc64b14c98775e54c2a80c9d956f2851f21"}, "docker": "quay.io/biocontainers/bioconductor-yeast2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeast2cdf.
shpc-registry automated BioContainers addition for bioconductor-yeast2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeast2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeast2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeast2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-yeast2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeast2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeast2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeast2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeast2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeast2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeast2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-yeast2cdf

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