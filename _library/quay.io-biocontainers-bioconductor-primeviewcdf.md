---
layout: container
name:  "quay.io/biocontainers/bioconductor-primeviewcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-primeviewcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-primeviewcdf/container.yaml"
updated_at: "2024-05-06 03:07:04.816522"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-primeviewcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-primeviewcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-primeviewcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-primeviewcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:88c3500839da1dc555a43bcd170f403e6e74b071497244f06d9001bfce328fb9"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:ae864a33b326689a1ffe23b9f95f77d6807677c9684588f0d3ef9c5b586e9ea6", "2.18.0--r42hdfd78af_10": "sha256:aed6718598157afa26fbb8d4e7dcbdb809f03825efedbac865b9769473476f54", "2.18.0--r43hdfd78af_11": "sha256:ca0ac3afe540e1ba860682dc9ca6920b39725d84485a7c9ad2ed958b2552c78e", "2.18.0--r43hdfd78af_12": "sha256:88c3500839da1dc555a43bcd170f403e6e74b071497244f06d9001bfce328fb9"}, "docker": "quay.io/biocontainers/bioconductor-primeviewcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-primeviewcdf.
shpc-registry automated BioContainers addition for bioconductor-primeviewcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-primeviewcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-primeviewcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-primeviewcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-primeviewcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-primeviewcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-primeviewcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-primeviewcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-primeviewcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-primeviewcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-primeviewcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-primeviewcdf

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