---
layout: container
name:  "quay.io/biocontainers/bioconductor-harmandata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-harmandata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-harmandata/container.yaml"
updated_at: "2023-10-26 03:18:45.842997"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-harmandata"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.25.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-harmandata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-harmandata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-harmandata", "latest": {"1.28.0--r43hdfd78af_0": "sha256:90e15be38df3a01e5f56f16cac359bb7754389e09c5551b1ed0e9fcd114be5fa"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:52f95ebe3ef2eb3e6f88476b35c4a2816c83b28c227a37ba0f1fcc1b7fc6546e", "1.25.0--r42hdfd78af_0": "sha256:86bcaade80d990da594722010eebe776d9d12afdb67d6cba3eca634215350888", "1.28.0--r43hdfd78af_0": "sha256:90e15be38df3a01e5f56f16cac359bb7754389e09c5551b1ed0e9fcd114be5fa"}, "docker": "quay.io/biocontainers/bioconductor-harmandata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-harmandata.
shpc-registry automated BioContainers addition for bioconductor-harmandata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-harmandata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-harmandata:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-harmandata/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-harmandata/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-harmandata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harmandata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harmandata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-harmandata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-harmandata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-harmandata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-harmandata

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