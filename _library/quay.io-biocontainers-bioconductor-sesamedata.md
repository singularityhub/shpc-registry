---
layout: container
name:  "quay.io/biocontainers/bioconductor-sesamedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sesamedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sesamedata/container.yaml"
updated_at: "2023-10-30 04:22:55.724256"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sesamedata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.1--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sesamedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sesamedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sesamedata", "latest": {"1.18.0--r43hdfd78af_0": "sha256:c2f60f45849a10f1636b5c81afd0633b9a52e88c5ea45ef534a6d62416b5d422"}, "tags": {"1.8.1--r40hdfd78af_0": "sha256:19bdeec94f0f90864053d9b156d6e78977d52df56e08962e49d15408f388c2ba", "1.16.0--r42hdfd78af_0": "sha256:6125580fcbc46a50b01ff8774c75139074a8fb4ce15f4541564f65b49f9304f8", "1.12.0--r41hdfd78af_1": "sha256:b4df82c5ef2c80f21105670343e039420bf8b1d375d2767106b9c6e1a5059625", "1.10.0--r41hdfd78af_0": "sha256:84b43b9302c9124fc93f7dd2e85d21857dd56af39cbed35ac55022af2ff5831d", "1.18.0--r43hdfd78af_0": "sha256:c2f60f45849a10f1636b5c81afd0633b9a52e88c5ea45ef534a6d62416b5d422"}, "docker": "quay.io/biocontainers/bioconductor-sesamedata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sesamedata.
shpc-registry automated BioContainers addition for bioconductor-sesamedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sesamedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sesamedata:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sesamedata/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sesamedata/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sesamedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sesamedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sesamedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sesamedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sesamedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sesamedata-inspect-deffile:

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