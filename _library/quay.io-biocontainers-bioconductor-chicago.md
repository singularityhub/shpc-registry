---
layout: container
name:  "quay.io/biocontainers/bioconductor-chicago"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chicago/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chicago/container.yaml"
updated_at: "2024-10-20 03:11:16.220353"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chicago"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chicago"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chicago", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chicago", "latest": {"1.30.0--r43hdfd78af_0": "sha256:930b9fca17c12e4692ee05170bc334c4c35ac84ef1870fc79db25f0076d1d141"}, "tags": {"1.8.0--r351_0": "sha256:b92dbbc42c0d10be373798dc7e7759f6ef376547752202064d27252a77dd74ea", "1.26.0--r42hdfd78af_0": "sha256:8bf50d57a0eaead556f575ba2296c2d198f90ff609310f3bf67e2cec7eb873fc", "1.22.0--r41hdfd78af_0": "sha256:ff2bba6f6a85adda4905e5f1e15544a3553d04bd665aff248fe9a0498c534587", "1.20.0--r41hdfd78af_0": "sha256:3eaa7dda8fddc8b26fec0205c26f22fb1620e891af6c5b3bce9ce387877c140d", "1.18.0--r40hdfd78af_1": "sha256:05b3db44473944a042d1c7bbcf56549cd09b6946874fd8e75c976ee666b4c927", "1.16.0--r40_0": "sha256:ef158eb75edf6f452132d3aa73f7bdc8b15e9f3c2055dc88c9dd321c86ed10b6", "1.28.0--r43hdfd78af_0": "sha256:8a85973b171f00a6ab831cb4cb72ddd0062b7e58d4135bcb80038be085ce01ee", "1.30.0--r43hdfd78af_0": "sha256:930b9fca17c12e4692ee05170bc334c4c35ac84ef1870fc79db25f0076d1d141"}, "docker": "quay.io/biocontainers/bioconductor-chicago"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chicago.
shpc-registry automated BioContainers addition for bioconductor-chicago
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chicago
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chicago:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chicago/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chicago/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chicago-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chicago-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chicago-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chicago-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chicago-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chicago-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chicago

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