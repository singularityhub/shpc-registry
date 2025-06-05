---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu19ksubb.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu19ksubb.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu19ksubb.db/container.yaml"
updated_at: "2025-06-05 03:38:30.450104"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mu19ksubb.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mu19ksubb.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu19ksubb.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu19ksubb.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:b473f0a7fb0b7f4fc7e6ddd6f77a5a544d498dab408f7c6074f87296686b6b8a"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:bd0899d0d3c2b0577231cc11551965a16bdd4ca87acc4dc50ae057140ecbcdb6", "3.13.0--r41hdfd78af_1": "sha256:47c5394f04123236ffc62b3183a4efc8dd7101f6b85704aa59cf39176fc8b160", "3.13.0--r42hdfd78af_2": "sha256:b7640e5ef04a6ad1408edf4dadc11a303bce083a1343a23079e8e6a3bc368d93", "3.13.0--r43hdfd78af_3": "sha256:ade49ba5638cb960aacfd9594d233a2c05bc9dd1eba25afe4bdf83ca2f929f7a", "3.13.0--r43hdfd78af_4": "sha256:95013965b1a206b86805a5e2d76042979d8e37575c34c280160b2305a398396f", "3.13.0--r44hdfd78af_5": "sha256:b473f0a7fb0b7f4fc7e6ddd6f77a5a544d498dab408f7c6074f87296686b6b8a"}, "docker": "quay.io/biocontainers/bioconductor-mu19ksubb.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu19ksubb.db.
shpc-registry automated BioContainers addition for bioconductor-mu19ksubb.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubb.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubb.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu19ksubb.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mu19ksubb.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu19ksubb.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubb.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubb.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu19ksubb.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu19ksubb.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu19ksubb.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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