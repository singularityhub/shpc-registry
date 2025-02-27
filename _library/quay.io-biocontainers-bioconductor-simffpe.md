---
layout: container
name:  "quay.io/biocontainers/bioconductor-simffpe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simffpe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simffpe/container.yaml"
updated_at: "2025-02-27 03:37:40.226910"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simffpe"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simffpe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simffpe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simffpe", "latest": {"1.18.0--r44hdfd78af_0": "sha256:84d8e1e1bde6511865729412e914e3d52a767b2d71cf1d3efb6b3b1bc120dff4"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:93af389ab17b1731e280dbbc3fb62c8b9ffc715794f3e1814f75a94a349e0902", "1.10.0--r42hdfd78af_0": "sha256:66a1b106d0cf87063ff47237fd40a693a6079971c49b234923ab26e2104dde97", "1.12.0--r43hdfd78af_0": "sha256:6652d4593b6cee12d2a4cb4e4ae126b3ae222a5b31ac117ebff9edebeb72a08a", "1.14.0--r43hdfd78af_0": "sha256:18d9f3b866b315f66f6ca2a043744dab49f1d3951ed521128065c0431623aa68", "1.18.0--r44hdfd78af_0": "sha256:84d8e1e1bde6511865729412e914e3d52a767b2d71cf1d3efb6b3b1bc120dff4"}, "docker": "quay.io/biocontainers/bioconductor-simffpe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simffpe.
shpc-registry automated BioContainers addition for bioconductor-simffpe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simffpe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simffpe:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simffpe/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-simffpe/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simffpe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simffpe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simffpe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simffpe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simffpe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simffpe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-simffpe

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