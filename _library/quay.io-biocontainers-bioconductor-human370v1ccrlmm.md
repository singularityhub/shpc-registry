---
layout: container
name:  "quay.io/biocontainers/bioconductor-human370v1ccrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human370v1ccrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human370v1ccrlmm/container.yaml"
updated_at: "2025-05-24 11:24:19.349175"
latest: "1.0.2--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-human370v1ccrlmm"

versions:
 - "1.0.2--r41hdfd78af_9"
 - "1.0.2--r42hdfd78af_10"
 - "1.0.2--r43hdfd78af_11"
 - "1.0.2--r43hdfd78af_12"
 - "1.0.2--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-human370v1ccrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human370v1ccrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human370v1ccrlmm", "latest": {"1.0.2--r44hdfd78af_13": "sha256:fee1078bd2debf57ebfa702b5d009979e09683ccfc92a4eddbb2c6a2486268a5"}, "tags": {"1.0.2--r41hdfd78af_9": "sha256:7440cb416c425605160c40e8e39487d865c150e583906bbbc4a5f4d216ab387c", "1.0.2--r42hdfd78af_10": "sha256:81f2a41b6d24df95c7cc5a71d1520e9d5f663a39895b8ed2a4e3cec956f851c9", "1.0.2--r43hdfd78af_11": "sha256:8dc76c276c73d281d0b5749583e09dfadddf62c59cb5e7be1373d2bcb5e9e299", "1.0.2--r43hdfd78af_12": "sha256:0abffdc6dacadc7e80b42f8517cb48099e1df5a04b5779ebf648649cc1bafa39", "1.0.2--r44hdfd78af_13": "sha256:fee1078bd2debf57ebfa702b5d009979e09683ccfc92a4eddbb2c6a2486268a5"}, "docker": "quay.io/biocontainers/bioconductor-human370v1ccrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human370v1ccrlmm.
shpc-registry automated BioContainers addition for bioconductor-human370v1ccrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human370v1ccrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human370v1ccrlmm:1.0.2--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human370v1ccrlmm/1.0.2--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-human370v1ccrlmm/1.0.2--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human370v1ccrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human370v1ccrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human370v1ccrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human370v1ccrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human370v1ccrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human370v1ccrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human370v1ccrlmm

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