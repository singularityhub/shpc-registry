---
layout: container
name:  "quay.io/biocontainers/bioconductor-scanvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scanvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scanvis/container.yaml"
updated_at: "2025-01-27 06:47:04.392417"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scanvis"

versions:
 - "1.7.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scanvis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scanvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scanvis", "latest": {"1.20.0--r44hdfd78af_0": "sha256:7e81cd642c56b9a9dbe296afaaa24c537328d4fc8af185c401a735e6862f382b"}, "tags": {"1.7.0--r41hdfd78af_0": "sha256:5d2c0f083c51c5901e8427cb774c3d02d1d9c097df1c6b6e8cf8b607be88c133", "1.12.0--r42hdfd78af_0": "sha256:207ac23309cdfb6b1c6b992857aa01ce83383984eb57e6ea4a0c868da49d9896", "1.14.0--r43hdfd78af_0": "sha256:7c8c0dba79e296af155d02dee9242157da7e875213ff8c466db4f18a0b337155", "1.16.0--r43hdfd78af_0": "sha256:a0c0293ce304bedaecf97a49ede50bbbb73cc9333b4e694b471367fa544e8c4d", "1.20.0--r44hdfd78af_0": "sha256:7e81cd642c56b9a9dbe296afaaa24c537328d4fc8af185c401a735e6862f382b"}, "docker": "quay.io/biocontainers/bioconductor-scanvis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scanvis.
shpc-registry automated BioContainers addition for bioconductor-scanvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scanvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scanvis:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scanvis/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scanvis/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scanvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scanvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scanvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scanvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scanvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scanvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scanvis

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