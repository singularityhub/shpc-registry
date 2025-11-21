---
layout: container
name:  "quay.io/biocontainers/bioconductor-genotypeeval"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genotypeeval/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genotypeeval/container.yaml"
updated_at: "2025-11-21 15:46:41.969689"
latest: "1.30.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genotypeeval"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genotypeeval"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genotypeeval", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genotypeeval", "latest": {"1.30.0--r42hdfd78af_0": "sha256:7cf6c9b878c00777cb605fb2dc2e524d2f9aa90d19d7d834955f7179aea988e8"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:4776b529872e113629c42aead3c9cb1c3b7a3750889877c9626b0d98e8a7a018", "1.30.0--r42hdfd78af_0": "sha256:7cf6c9b878c00777cb605fb2dc2e524d2f9aa90d19d7d834955f7179aea988e8"}, "docker": "quay.io/biocontainers/bioconductor-genotypeeval"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genotypeeval.
shpc-registry automated BioContainers addition for bioconductor-genotypeeval
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genotypeeval
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genotypeeval:1.30.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genotypeeval/1.30.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genotypeeval/1.30.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genotypeeval-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genotypeeval-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genotypeeval-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genotypeeval-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genotypeeval-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genotypeeval-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genotypeeval

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