---
layout: container
name:  "quay.io/biocontainers/bioconductor-htratfocusprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htratfocusprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htratfocusprobe/container.yaml"
updated_at: "2023-05-05 03:15:01.212408"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-htratfocusprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-htratfocusprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htratfocusprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htratfocusprobe", "latest": {"2.18.0--r42hdfd78af_10": "sha256:e2f6da3a6f8e4f147ce8ad1e4eaaf4baace8a3bde7281bbbc5f34f79298c4fca"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:296f6306b2aaf9ea0354d8a2182f1cb1d6ca24c02fb891bc1472224d55569be6", "2.18.0--r42hdfd78af_10": "sha256:e2f6da3a6f8e4f147ce8ad1e4eaaf4baace8a3bde7281bbbc5f34f79298c4fca"}, "docker": "quay.io/biocontainers/bioconductor-htratfocusprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htratfocusprobe.
shpc-registry automated BioContainers addition for bioconductor-htratfocusprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htratfocusprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htratfocusprobe:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htratfocusprobe/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-htratfocusprobe/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htratfocusprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htratfocusprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htratfocusprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htratfocusprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htratfocusprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htratfocusprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htratfocusprobe

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