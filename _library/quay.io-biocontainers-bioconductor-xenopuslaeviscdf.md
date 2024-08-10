---
layout: container
name:  "quay.io/biocontainers/bioconductor-xenopuslaeviscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xenopuslaeviscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xenopuslaeviscdf/container.yaml"
updated_at: "2024-08-10 03:24:48.576058"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-xenopuslaeviscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-xenopuslaeviscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xenopuslaeviscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xenopuslaeviscdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:2602326262b3a53164d17372be315b5bc810b28f922ac03767c91b29d92f6051"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:208ff238fb3c9ae10bfe7c9cdde895a04e9d07480388fc7d634b320da587a5f6", "2.18.0--r42hdfd78af_10": "sha256:c70e121d6e78c80e3d9af8bf14ecae78357d226c85b61f042f8e664c9ac6f983", "2.18.0--r43hdfd78af_11": "sha256:0b96afc08d1c9496601f7e92567f1d18bb2118ec451eb5627a81e594652c7422", "2.18.0--r43hdfd78af_12": "sha256:2602326262b3a53164d17372be315b5bc810b28f922ac03767c91b29d92f6051"}, "docker": "quay.io/biocontainers/bioconductor-xenopuslaeviscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xenopuslaeviscdf.
shpc-registry automated BioContainers addition for bioconductor-xenopuslaeviscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xenopuslaeviscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xenopuslaeviscdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xenopuslaeviscdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-xenopuslaeviscdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xenopuslaeviscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xenopuslaeviscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xenopuslaeviscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xenopuslaeviscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xenopuslaeviscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xenopuslaeviscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xenopuslaeviscdf

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