---
layout: container
name:  "quay.io/biocontainers/bioconductor-awst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-awst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-awst/container.yaml"
updated_at: "2025-11-21 15:57:47.630033"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-awst"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-awst"
config: {"url": "https://biocontainers.pro/tools/bioconductor-awst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-awst", "latest": {"1.14.0--r44hdfd78af_0": "sha256:13c157920b70544a3f419b2d407f60e20296bc1515cb4e972e061bfb4b136231"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:afaf3e4ee35d29de551e7cb294a8dede50f4f7a1918f3d1ecfd7612906bc42b2", "1.6.0--r42hdfd78af_0": "sha256:5ba8f20d8e2bd756a9d1fd3ae40d0d08ae38b758547e1044ac1948ceb6ad25a3", "1.8.0--r43hdfd78af_0": "sha256:e56b73e749160bc6a847449bf4c201cf4a34f434d676d9e7ea1cd49231b78d1f", "1.10.0--r43hdfd78af_0": "sha256:93fe5830c6c2d70328a5eafb6bbe8e9f9d4822b53aa12f3f1f6a7e2528672d05", "1.14.0--r44hdfd78af_0": "sha256:13c157920b70544a3f419b2d407f60e20296bc1515cb4e972e061bfb4b136231"}, "docker": "quay.io/biocontainers/bioconductor-awst"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-awst.
shpc-registry automated BioContainers addition for bioconductor-awst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-awst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-awst:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-awst/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-awst/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-awst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-awst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-awst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-awst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-awst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-awst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-awst

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