---
layout: container
name:  "quay.io/biocontainers/bioconductor-spktools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spktools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spktools/container.yaml"
updated_at: "2023-04-26 02:54:41.787961"
latest: "1.54.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spktools"

versions:
 - "1.50.0--r41hdfd78af_0"
 - "1.54.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spktools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spktools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spktools", "latest": {"1.54.0--r42hdfd78af_0": "sha256:5f3cf187376dee21a27c7626a9e24dfe7fef970b12fe779353dbf0e8a9aa9ca3"}, "tags": {"1.50.0--r41hdfd78af_0": "sha256:1318786d3c76c41d11012576f320d1a7daa601f2a51b2d9b1255366484957082", "1.54.0--r42hdfd78af_0": "sha256:5f3cf187376dee21a27c7626a9e24dfe7fef970b12fe779353dbf0e8a9aa9ca3"}, "docker": "quay.io/biocontainers/bioconductor-spktools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spktools.
shpc-registry automated BioContainers addition for bioconductor-spktools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spktools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spktools:1.54.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spktools/1.54.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spktools/1.54.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spktools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spktools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spktools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spktools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spktools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spktools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spktools

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