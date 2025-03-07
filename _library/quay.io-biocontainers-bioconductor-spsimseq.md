---
layout: container
name:  "quay.io/biocontainers/bioconductor-spsimseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spsimseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spsimseq/container.yaml"
updated_at: "2025-03-07 03:43:48.357552"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spsimseq"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spsimseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spsimseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spsimseq", "latest": {"1.16.0--r44hdfd78af_0": "sha256:516dd27dc2b4655654ec25474ffeae7fa3300e71b16634b2657dd028c83a0dcb"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:19114b9bc419dfe5ed3dca677933b5259fa7b360078db947dd80e4efa7272373", "1.8.0--r42hdfd78af_0": "sha256:eac076f53a3593479c50725bd0b8dd99329d4e0f3d9d052b3fdad7d86d15b56d", "1.10.0--r43hdfd78af_0": "sha256:0317e824c7b01d640bba984801796d9e76a6b0fd21b0228a68ca49434e79b43d", "1.12.0--r43hdfd78af_0": "sha256:f2eef63a973845959a4d3d36fb2f91a262aa26cd2db85c3072f2604d2e617504", "1.16.0--r44hdfd78af_0": "sha256:516dd27dc2b4655654ec25474ffeae7fa3300e71b16634b2657dd028c83a0dcb"}, "docker": "quay.io/biocontainers/bioconductor-spsimseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spsimseq.
shpc-registry automated BioContainers addition for bioconductor-spsimseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spsimseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spsimseq:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spsimseq/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spsimseq/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spsimseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spsimseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spsimseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spsimseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spsimseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spsimseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spsimseq

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