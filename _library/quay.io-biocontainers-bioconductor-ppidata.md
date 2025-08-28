---
layout: container
name:  "quay.io/biocontainers/bioconductor-ppidata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ppidata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ppidata/container.yaml"
updated_at: "2025-08-28 12:22:13.683681"
latest: "0.32.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ppidata"

versions:
 - "0.32.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ppidata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ppidata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ppidata", "latest": {"0.32.0--r41hdfd78af_1": "sha256:d17259bc134e102ec0eb04415660e6b75cc21d4e57ff3c3bf4da41471f08ee4d"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:d17259bc134e102ec0eb04415660e6b75cc21d4e57ff3c3bf4da41471f08ee4d"}, "docker": "quay.io/biocontainers/bioconductor-ppidata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ppidata.
shpc-registry automated BioContainers addition for bioconductor-ppidata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ppidata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ppidata:0.32.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ppidata/0.32.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-ppidata/0.32.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ppidata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ppidata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ppidata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ppidata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ppidata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ppidata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ppidata

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