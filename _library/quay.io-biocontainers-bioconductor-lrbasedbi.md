---
layout: container
name:  "quay.io/biocontainers/bioconductor-lrbasedbi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lrbasedbi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lrbasedbi/container.yaml"
updated_at: "2025-09-05 03:12:46.728429"
latest: "2.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lrbasedbi"

versions:
 - "2.4.0--r41hdfd78af_0"
 - "2.8.0--r42hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lrbasedbi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lrbasedbi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lrbasedbi", "latest": {"2.16.0--r44hdfd78af_0": "sha256:4a4074ec4f284a90252b3418516837d970a263d7891271b55a765882bea607c0"}, "tags": {"2.4.0--r41hdfd78af_0": "sha256:a7c13f461a12f99d3d2ddd27344920b544d770623f5e819bcc00900aaadafaa0", "2.8.0--r42hdfd78af_0": "sha256:219868701d4c614261a3ffbe56da2cd94c0aabf23fc448770803e9c9d86fac21", "2.10.0--r43hdfd78af_0": "sha256:7b1473560abfc3ed813b7637e1b101ef68d95f0fdfd64a6d5be0c700bb023393", "2.12.0--r43hdfd78af_0": "sha256:85cdaf458f1ce482cd2dcb39c6506f87d711a31c2dc64cca30e6abb2e23e3017", "2.16.0--r44hdfd78af_0": "sha256:4a4074ec4f284a90252b3418516837d970a263d7891271b55a765882bea607c0"}, "docker": "quay.io/biocontainers/bioconductor-lrbasedbi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lrbasedbi.
shpc-registry automated BioContainers addition for bioconductor-lrbasedbi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lrbasedbi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lrbasedbi:2.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lrbasedbi/2.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lrbasedbi/2.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lrbasedbi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrbasedbi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrbasedbi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lrbasedbi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lrbasedbi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lrbasedbi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lrbasedbi

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