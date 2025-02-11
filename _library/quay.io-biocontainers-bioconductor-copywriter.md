---
layout: container
name:  "quay.io/biocontainers/bioconductor-copywriter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-copywriter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-copywriter/container.yaml"
updated_at: "2025-02-11 03:19:21.515558"
latest: "2.29.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-copywriter"

versions:
 - "2.26.0--r41hdfd78af_0"
 - "2.29.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-copywriter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-copywriter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-copywriter", "latest": {"2.29.0--r42hdfd78af_0": "sha256:b75a77d301296cd54fe0a4c3354e8d54be00ea68a62e5ddb3f6517052b9b9e81"}, "tags": {"2.26.0--r41hdfd78af_0": "sha256:b862874d49689b46f9924d8778bd66c5a7d60522e69f19100d218a35fcb848e7", "2.29.0--r42hdfd78af_0": "sha256:b75a77d301296cd54fe0a4c3354e8d54be00ea68a62e5ddb3f6517052b9b9e81"}, "docker": "quay.io/biocontainers/bioconductor-copywriter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-copywriter.
shpc-registry automated BioContainers addition for bioconductor-copywriter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-copywriter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-copywriter:2.29.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-copywriter/2.29.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-copywriter/2.29.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-copywriter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copywriter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copywriter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-copywriter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-copywriter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-copywriter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-copywriter

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