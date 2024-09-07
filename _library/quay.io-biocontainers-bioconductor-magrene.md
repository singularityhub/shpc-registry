---
layout: container
name:  "quay.io/biocontainers/bioconductor-magrene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-magrene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-magrene/container.yaml"
updated_at: "2024-09-07 03:22:43.967220"
latest: "1.4.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-magrene"

versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-magrene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-magrene", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-magrene", "latest": {"1.4.0--r43hdfd78af_0": "sha256:4aaf04f7c6ae4b8363f8e200c15ca4fee64505db9358c8e0e78e29b15806a890"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:e769bdc2c5da027ccb552aba6520c79c1a9f77c1dd4a04418e16f52420facb08", "1.2.0--r43hdfd78af_0": "sha256:9dd636f04d0dfd5006c1ac308494b94e69b854c40403d1070fd3f1b11b50ae2e", "1.4.0--r43hdfd78af_0": "sha256:4aaf04f7c6ae4b8363f8e200c15ca4fee64505db9358c8e0e78e29b15806a890"}, "docker": "quay.io/biocontainers/bioconductor-magrene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-magrene.
singularity registry hpc automated addition for bioconductor-magrene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-magrene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-magrene:1.4.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-magrene/1.4.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-magrene/1.4.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-magrene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-magrene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-magrene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-magrene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-magrene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-magrene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-magrene

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