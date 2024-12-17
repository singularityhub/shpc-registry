---
layout: container
name:  "quay.io/biocontainers/bioconductor-orderedlist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-orderedlist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-orderedlist/container.yaml"
updated_at: "2024-12-17 03:15:14.051874"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-orderedlist"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-orderedlist"
config: {"url": "https://biocontainers.pro/tools/bioconductor-orderedlist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-orderedlist", "latest": {"1.74.0--r43hdfd78af_0": "sha256:74162b5a5476cc59c8bf6428deb0947738f56416fc698a2cc9a80717b8fe542a"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:8de59ef1eda6e750f91055f6b850a54c571a542501d80449c7f91b31f8e71d3b", "1.70.0--r42hdfd78af_0": "sha256:537cb4c4d0f0163e0e1b5190db47e826e991c5367d6b2b8df68098e96f430e6d", "1.72.0--r43hdfd78af_0": "sha256:8400c849415bdb706ee66f06910529d8cf94f6269a518c6a5b0d48e4d849c844", "1.74.0--r43hdfd78af_0": "sha256:74162b5a5476cc59c8bf6428deb0947738f56416fc698a2cc9a80717b8fe542a"}, "docker": "quay.io/biocontainers/bioconductor-orderedlist"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-orderedlist.
shpc-registry automated BioContainers addition for bioconductor-orderedlist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-orderedlist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-orderedlist:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-orderedlist/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-orderedlist/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-orderedlist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orderedlist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orderedlist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-orderedlist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-orderedlist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-orderedlist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-orderedlist

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