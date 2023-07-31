---
layout: container
name:  "quay.io/biocontainers/bioconductor-biobtreer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biobtreer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biobtreer/container.yaml"
updated_at: "2023-07-31 03:29:45.486260"
latest: "1.10.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biobtreer"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biobtreer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biobtreer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biobtreer", "latest": {"1.10.0--r42hdfd78af_0": "sha256:5dc7730f2e5010d90f96a694dc3fede2891a40f0e427cc9f5d86b05e96e0ee06"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:9dbda507303a3aaab53f775f57e33ee27771ed9961d33e102fca97e2668b65c8", "1.10.0--r42hdfd78af_0": "sha256:5dc7730f2e5010d90f96a694dc3fede2891a40f0e427cc9f5d86b05e96e0ee06"}, "docker": "quay.io/biocontainers/bioconductor-biobtreer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biobtreer.
shpc-registry automated BioContainers addition for bioconductor-biobtreer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biobtreer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biobtreer:1.10.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biobtreer/1.10.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biobtreer/1.10.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biobtreer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biobtreer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biobtreer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biobtreer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biobtreer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biobtreer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biobtreer

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