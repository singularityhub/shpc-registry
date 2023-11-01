---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowmap/container.yaml"
updated_at: "2023-11-01 03:04:59.962010"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowmap"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowmap", "latest": {"1.38.0--r43hdfd78af_0": "sha256:e757f7e288b84196c6323479926e761e87cc579266434f8f1b956769456c7672"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:93d49acfa99288acee0a4b6753a21189d7f14afcc7c646e82781d9699c612ead", "1.36.0--r42hdfd78af_0": "sha256:ed0436a8df56344f32d26b4c5d02e9cf0a2ab36b235ac39e9a4d627df90f0da2", "1.38.0--r43hdfd78af_0": "sha256:e757f7e288b84196c6323479926e761e87cc579266434f8f1b956769456c7672"}, "docker": "quay.io/biocontainers/bioconductor-flowmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowmap.
shpc-registry automated BioContainers addition for bioconductor-flowmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmap:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowmap/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowmap/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowmap

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