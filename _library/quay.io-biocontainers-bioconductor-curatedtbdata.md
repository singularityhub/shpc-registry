---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedtbdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedtbdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedtbdata/container.yaml"
updated_at: "2023-08-29 03:59:35.895067"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedtbdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedtbdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedtbdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedtbdata", "latest": {"1.6.0--r43hdfd78af_0": "sha256:d80ae2c4c04963c49a4578018e35e15051988025e70e626ffa8a6947abfd631a"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:95afeb6766915b3ed62b07dda01619ff03efa833454b96e19ef7f9a96156fca1", "1.4.0--r42hdfd78af_0": "sha256:87f7c7132f8a8c66d760d2647180a4e8faf4b6d56c527a41a4e522dadc9a69cd", "1.6.0--r43hdfd78af_0": "sha256:d80ae2c4c04963c49a4578018e35e15051988025e70e626ffa8a6947abfd631a"}, "docker": "quay.io/biocontainers/bioconductor-curatedtbdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedtbdata.
shpc-registry automated BioContainers addition for bioconductor-curatedtbdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedtbdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedtbdata:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedtbdata/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedtbdata/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedtbdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedtbdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedtbdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedtbdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedtbdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedtbdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-curatedtbdata

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