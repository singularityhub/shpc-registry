---
layout: container
name:  "quay.io/biocontainers/bioconductor-metagenomeseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metagenomeseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metagenomeseq/container.yaml"
updated_at: "2023-09-11 02:32:03.064133"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metagenomeseq"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metagenomeseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metagenomeseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metagenomeseq", "latest": {"1.42.0--r43hdfd78af_0": "sha256:3f003453d90551f2e2f44a08157411afefa9a8bae9d43b0ebf97a90c66f8b090"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:53f7c8dfb087dd07f525bc2d9b77f4e87082a579ca3ab84efaba611846503f28", "1.40.0--r42hdfd78af_0": "sha256:12b9ce8f073115b6bb5032fcb04f0a50bcefdef7429fe9401f7de07a4d7c204e", "1.42.0--r43hdfd78af_0": "sha256:3f003453d90551f2e2f44a08157411afefa9a8bae9d43b0ebf97a90c66f8b090"}, "docker": "quay.io/biocontainers/bioconductor-metagenomeseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metagenomeseq.
shpc-registry automated BioContainers addition for bioconductor-metagenomeseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metagenomeseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metagenomeseq:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metagenomeseq/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metagenomeseq/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metagenomeseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metagenomeseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metagenomeseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metagenomeseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metagenomeseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metagenomeseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metagenomeseq

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