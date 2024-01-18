---
layout: container
name:  "quay.io/biocontainers/bioconductor-targetsearchdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-targetsearchdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-targetsearchdata/container.yaml"
updated_at: "2024-01-18 02:39:49.942929"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-targetsearchdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.2--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-targetsearchdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-targetsearchdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-targetsearchdata", "latest": {"1.40.0--r43hdfd78af_0": "sha256:2ef5d4ccf8eade9aed069d603666e529878fd6697281b4d88a3589a2a8a47940"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:4fbc3e52139c59f159633c3e677c175936844d4d423b06984a63557ad6c75684", "1.35.2--r42hdfd78af_0": "sha256:2a6e120a40d569c5d8457b43c163a979ac63170dd1b6771a9531ab31aeee39b6", "1.38.0--r43hdfd78af_0": "sha256:d227d97a86d51923d008c08ea049437bd6107162ee1d7f6c49e6a1946a539641", "1.40.0--r43hdfd78af_0": "sha256:2ef5d4ccf8eade9aed069d603666e529878fd6697281b4d88a3589a2a8a47940"}, "docker": "quay.io/biocontainers/bioconductor-targetsearchdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-targetsearchdata.
shpc-registry automated BioContainers addition for bioconductor-targetsearchdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-targetsearchdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-targetsearchdata:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-targetsearchdata/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-targetsearchdata/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-targetsearchdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetsearchdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetsearchdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-targetsearchdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-targetsearchdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-targetsearchdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-targetsearchdata

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