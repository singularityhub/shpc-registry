---
layout: container
name:  "quay.io/biocontainers/bioconductor-enmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enmix/container.yaml"
updated_at: "2024-01-15 02:56:20.021913"
latest: "1.38.01--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enmix"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.01--r43hdfd78af_0"
 - "1.38.01--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enmix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enmix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enmix", "latest": {"1.38.01--r43hdfd78af_0": "sha256:dbbeb93fa3120a3a197061731afab41e973e695f6255d5db323aa3ba92e9b510"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:a4a353f88686e3347a2a3c215a15c8ab7d1f404798e8acb437157dd247d7d61f", "1.34.0--r42hdfd78af_0": "sha256:d0b71c1a497defcacd01daf68e752c8b2fbb34225ceeff1e10fbdad4e63382a5", "1.36.01--r43hdfd78af_0": "sha256:e8384371c8dadcca3011f1ddc52b638718325d5987c6ac97cbee302e3d5e10fa", "1.38.01--r43hdfd78af_0": "sha256:dbbeb93fa3120a3a197061731afab41e973e695f6255d5db323aa3ba92e9b510"}, "docker": "quay.io/biocontainers/bioconductor-enmix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enmix.
shpc-registry automated BioContainers addition for bioconductor-enmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enmix:1.38.01--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enmix/1.38.01--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-enmix/1.38.01--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-enmix

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