---
layout: container
name:  "quay.io/biocontainers/bioconductor-pcatools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pcatools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pcatools/container.yaml"
updated_at: "2023-05-18 03:17:27.612144"
latest: "2.10.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pcatools"

versions:
 - "2.6.0--r41hc247a5b_2"
 - "2.10.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pcatools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pcatools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pcatools", "latest": {"2.10.0--r42hc247a5b_0": "sha256:cfe52596c08d57a337eec5873bb84e503bbc1497b74db5a64f64f5051ec5a5c9"}, "tags": {"2.6.0--r41hc247a5b_2": "sha256:ecc5a61ff97f7cf1ae1807a5d1530c04b4ed91d1e2863a6d85063ba4a24c4734", "2.10.0--r42hc247a5b_0": "sha256:cfe52596c08d57a337eec5873bb84e503bbc1497b74db5a64f64f5051ec5a5c9"}, "docker": "quay.io/biocontainers/bioconductor-pcatools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pcatools.
shpc-registry automated BioContainers addition for bioconductor-pcatools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pcatools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pcatools:2.10.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pcatools/2.10.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-pcatools/2.10.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pcatools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcatools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcatools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pcatools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pcatools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pcatools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pcatools

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