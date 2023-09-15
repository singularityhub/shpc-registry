---
layout: container
name:  "quay.io/biocontainers/bioconductor-msfeatures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msfeatures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msfeatures/container.yaml"
updated_at: "2023-09-15 02:39:00.161408"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msfeatures"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msfeatures"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msfeatures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msfeatures", "latest": {"1.8.0--r43hdfd78af_0": "sha256:cb5546b586d6f87a1d8d14a153fcb14da05ce1ce81115d936b985853c7063cfb"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:f2d00cdfdb0183a0aefae31f14357c9bcffb2e3c80e83342715372c4acbc0668", "1.6.0--r42hdfd78af_0": "sha256:ec672eb2c184df7e7dd4dd43e7451cf9dace5e416743edc80c01c4b6b3816bed", "1.8.0--r43hdfd78af_0": "sha256:cb5546b586d6f87a1d8d14a153fcb14da05ce1ce81115d936b985853c7063cfb"}, "docker": "quay.io/biocontainers/bioconductor-msfeatures"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msfeatures.
shpc-registry automated BioContainers addition for bioconductor-msfeatures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msfeatures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msfeatures:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msfeatures/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msfeatures/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msfeatures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msfeatures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msfeatures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msfeatures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msfeatures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msfeatures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msfeatures

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