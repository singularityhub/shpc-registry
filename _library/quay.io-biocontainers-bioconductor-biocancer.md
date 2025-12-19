---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocancer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocancer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocancer/container.yaml"
updated_at: "2025-12-19 05:17:11.583477"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocancer"
aliases:
 - "pandoc"
versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocancer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocancer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocancer", "latest": {"1.34.0--r44hdfd78af_0": "sha256:487541444e83604b1fffba9f166cedd4d4daa06cb430bac98835f345dcb55ebf"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:87f5f8091df9cc763c452753c7206f6a552591af5ffeaea00bb49cf8f6430913", "1.26.0--r42hdfd78af_0": "sha256:26b8f5a9c88cf21e43fcf47158a075827980e76d4862c71a55026b5e26381d00", "1.28.0--r43hdfd78af_0": "sha256:de30876050b7fd0e1cc334626632a9b7bf1922f6fed9a375b2a2276a66bf7f0e", "1.30.0--r43hdfd78af_0": "sha256:cfda261c0a6a477e23fb102ca1f00f2ec761249fcb99897c5ebfeaa679a07b4e", "1.34.0--r44hdfd78af_0": "sha256:487541444e83604b1fffba9f166cedd4d4daa06cb430bac98835f345dcb55ebf"}, "docker": "quay.io/biocontainers/bioconductor-biocancer", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocancer.
shpc-registry automated BioContainers addition for bioconductor-biocancer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocancer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocancer:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocancer/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocancer/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocancer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocancer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocancer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocancer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocancer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocancer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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