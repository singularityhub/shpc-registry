---
layout: container
name:  "quay.io/biocontainers/bioconductor-predasampledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-predasampledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-predasampledata/container.yaml"
updated_at: "2024-03-20 02:43:42.465368"
latest: "0.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-predasampledata"

versions:
 - "0.34.0--r41hdfd78af_1"
 - "0.38.0--r42hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
 - "0.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-predasampledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-predasampledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-predasampledata", "latest": {"0.42.0--r43hdfd78af_0": "sha256:cbd1fcbcdf0e4c0a61f7a30ea30f54fcef51eb871031220cac87c205eedf71bf"}, "tags": {"0.34.0--r41hdfd78af_1": "sha256:2e1995bf7cfd99edbb719aa1d6cf3580f9729351110399851543e8d5a438e9f2", "0.38.0--r42hdfd78af_0": "sha256:01099e1b12af01f0cb55afcdc8899d25cbc8c77ec8e5592ecf9307ed03051dcd", "0.40.0--r43hdfd78af_0": "sha256:6f2d544b4f8d385b3418efa3dca9801dc681a85e3499ef588d3c25d4808c2fe7", "0.42.0--r43hdfd78af_0": "sha256:cbd1fcbcdf0e4c0a61f7a30ea30f54fcef51eb871031220cac87c205eedf71bf"}, "docker": "quay.io/biocontainers/bioconductor-predasampledata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-predasampledata.
shpc-registry automated BioContainers addition for bioconductor-predasampledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-predasampledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-predasampledata:0.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-predasampledata/0.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-predasampledata/0.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-predasampledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-predasampledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-predasampledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-predasampledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-predasampledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-predasampledata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-predasampledata

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