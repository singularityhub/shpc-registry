---
layout: container
name:  "quay.io/biocontainers/bioconductor-tradeseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tradeseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tradeseq/container.yaml"
updated_at: "2024-11-12 03:27:01.948749"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tradeseq"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tradeseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tradeseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tradeseq", "latest": {"1.16.0--r43hdfd78af_0": "sha256:79d82f1915d1c1290050170c15eee970a02f2ad0d3ab950824756d5f805fbf38"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:8871e88317ce06c163f0b8debefc59300e812b66113e52bd9d9125bc05b6b7e6", "1.12.0--r42hdfd78af_0": "sha256:065dd4fa5f2a6ef3469cd20fd0a25d66849d1fc235857fd57286aa6e945e31b8", "1.14.0--r43hdfd78af_0": "sha256:692def78abdf75a6d914c1e54caf226e4f269eaf4c977db1516b6aadf2f72132", "1.16.0--r43hdfd78af_0": "sha256:79d82f1915d1c1290050170c15eee970a02f2ad0d3ab950824756d5f805fbf38"}, "docker": "quay.io/biocontainers/bioconductor-tradeseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tradeseq.
shpc-registry automated BioContainers addition for bioconductor-tradeseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tradeseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tradeseq:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tradeseq/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tradeseq/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tradeseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tradeseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tradeseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tradeseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tradeseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tradeseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tradeseq

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