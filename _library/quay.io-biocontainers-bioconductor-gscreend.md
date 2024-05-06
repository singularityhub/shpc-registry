---
layout: container
name:  "quay.io/biocontainers/bioconductor-gscreend"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gscreend/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gscreend/container.yaml"
updated_at: "2024-05-06 03:04:09.397724"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gscreend"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gscreend"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gscreend", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gscreend", "latest": {"1.14.0--r43hdfd78af_0": "sha256:9fa52506c89e56fce5290f4c9113673c5232ca0a8165d1d9a5f9422d3bfd9acb"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:d86124a467ce21b770bff7700e23fa6fa24af1feb8c63ab3480524adf546e566", "1.12.0--r42hdfd78af_0": "sha256:635e9af8202d5fe847b5166c9458d38a99328c7d5d0bf3625b781bdfff1ab4c4", "1.14.0--r43hdfd78af_0": "sha256:9fa52506c89e56fce5290f4c9113673c5232ca0a8165d1d9a5f9422d3bfd9acb"}, "docker": "quay.io/biocontainers/bioconductor-gscreend"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gscreend.
shpc-registry automated BioContainers addition for bioconductor-gscreend
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gscreend
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gscreend:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gscreend/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gscreend/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gscreend-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gscreend-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gscreend-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gscreend-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gscreend-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gscreend-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gscreend

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