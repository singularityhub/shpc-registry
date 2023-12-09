---
layout: container
name:  "quay.io/biocontainers/bioconductor-xtropicaliscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xtropicaliscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xtropicaliscdf/container.yaml"
updated_at: "2023-12-09 02:47:19.436994"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-xtropicaliscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-xtropicaliscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xtropicaliscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xtropicaliscdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:5937dcb0b5eefadbed1c72a406c32f9c40e86c37fedcd1117200dcb87a97c64e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5d42e2b261697b8b6c2b8d3537f3a3ab3133f4f4565f4ffd1a89a813acb1f744", "2.18.0--r42hdfd78af_10": "sha256:ef5dacfe8a9aff3b0423b43311419dd81932f930495d7f52e8c21dbaa8833255", "2.18.0--r43hdfd78af_11": "sha256:5937dcb0b5eefadbed1c72a406c32f9c40e86c37fedcd1117200dcb87a97c64e"}, "docker": "quay.io/biocontainers/bioconductor-xtropicaliscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xtropicaliscdf.
shpc-registry automated BioContainers addition for bioconductor-xtropicaliscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xtropicaliscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xtropicaliscdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xtropicaliscdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-xtropicaliscdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xtropicaliscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xtropicaliscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xtropicaliscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xtropicaliscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xtropicaliscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xtropicaliscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xtropicaliscdf

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