---
layout: container
name:  "quay.io/biocontainers/bioconductor-phipdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phipdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phipdata/container.yaml"
updated_at: "2023-03-16 03:38:17.798984"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phipdata"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phipdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phipdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phipdata", "latest": {"1.6.0--r42hdfd78af_0": "sha256:8ed8880877ad395f165c8302c48c9ee8da5f1917256ae02a96b637b38b6d0c29"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:69f62f71b4eaf6dbfaf70fe6dd47fa5b7d48d90bc26737b7eb018053bae1889c", "1.6.0--r42hdfd78af_0": "sha256:8ed8880877ad395f165c8302c48c9ee8da5f1917256ae02a96b637b38b6d0c29"}, "docker": "quay.io/biocontainers/bioconductor-phipdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phipdata.
shpc-registry automated BioContainers addition for bioconductor-phipdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phipdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phipdata:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phipdata/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phipdata/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phipdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phipdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phipdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phipdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phipdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phipdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phipdata

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