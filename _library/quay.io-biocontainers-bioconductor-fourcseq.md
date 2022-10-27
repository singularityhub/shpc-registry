---
layout: container
name:  "quay.io/biocontainers/bioconductor-fourcseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fourcseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fourcseq/container.yaml"
updated_at: "2022-10-27 01:14:40.744910"
latest: "1.4.0--r3.3.1_1"
container_url: "https://biocontainers.pro/tools/bioconductor-fourcseq"

versions:
 - "1.4.0--r3.3.1_1"
description: "shpc-registry automated BioContainers addition for bioconductor-fourcseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fourcseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fourcseq", "latest": {"1.4.0--r3.3.1_1": "sha256:c8c5386080fc7e971bbe7f305620890aff49239e6c85c200f7756bd76e842d7d"}, "tags": {"1.4.0--r3.3.1_1": "sha256:c8c5386080fc7e971bbe7f305620890aff49239e6c85c200f7756bd76e842d7d"}, "docker": "quay.io/biocontainers/bioconductor-fourcseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fourcseq.
shpc-registry automated BioContainers addition for bioconductor-fourcseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fourcseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fourcseq:1.4.0--r3.3.1_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fourcseq/1.4.0--r3.3.1_1
$ module help quay.io/biocontainers/bioconductor-fourcseq/1.4.0--r3.3.1_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fourcseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fourcseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fourcseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fourcseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fourcseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fourcseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fourcseq

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