---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneplast.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneplast.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneplast.data/container.yaml"
updated_at: "2023-06-04 03:21:59.560133"
latest: "0.99.6--r42hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-geneplast.data"

versions:
 - "0.99.6--r41hdfd78af_0"
 - "0.99.6--r42hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-geneplast.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneplast.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneplast.data", "latest": {"0.99.6--r42hdfd78af_1": "sha256:7dc74ca635be29e237ee383f9b9dd18fa1a6f75f7eebf76c37976181bba9a105"}, "tags": {"0.99.6--r41hdfd78af_0": "sha256:c50f566af4fabb8dfe72d18b0c7cf751a5c040f3b0b40ad058a3c720085ffe9d", "0.99.6--r42hdfd78af_1": "sha256:7dc74ca635be29e237ee383f9b9dd18fa1a6f75f7eebf76c37976181bba9a105"}, "docker": "quay.io/biocontainers/bioconductor-geneplast.data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneplast.data.
shpc-registry automated BioContainers addition for bioconductor-geneplast.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneplast.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneplast.data:0.99.6--r42hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneplast.data/0.99.6--r42hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-geneplast.data/0.99.6--r42hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneplast.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneplast.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneplast.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneplast.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneplast.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneplast.data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geneplast.data

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