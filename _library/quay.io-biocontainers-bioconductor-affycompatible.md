---
layout: container
name:  "quay.io/biocontainers/bioconductor-affycompatible"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affycompatible/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affycompatible/container.yaml"
updated_at: "2025-05-11 03:34:57.079182"
latest: "1.58.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affycompatible"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affycompatible"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affycompatible", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affycompatible", "latest": {"1.58.0--r42hdfd78af_0": "sha256:85c1a54eb8303e51c89bb894ba2034a2908962f909b3b1bc48bbafd8a45763c8"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:543a327dd341033ce71c8800de50940da30e443bdc7e7a72bf004071bf2e7029", "1.58.0--r42hdfd78af_0": "sha256:85c1a54eb8303e51c89bb894ba2034a2908962f909b3b1bc48bbafd8a45763c8"}, "docker": "quay.io/biocontainers/bioconductor-affycompatible"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affycompatible.
shpc-registry automated BioContainers addition for bioconductor-affycompatible
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affycompatible
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affycompatible:1.58.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affycompatible/1.58.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affycompatible/1.58.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affycompatible-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycompatible-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycompatible-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affycompatible-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affycompatible-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affycompatible-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affycompatible

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