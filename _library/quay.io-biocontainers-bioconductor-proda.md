---
layout: container
name:  "quay.io/biocontainers/bioconductor-proda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proda/container.yaml"
updated_at: "2025-10-31 04:28:17.212056"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proda"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proda"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proda", "latest": {"1.20.0--r44hdfd78af_0": "sha256:82d5ddbc663bd17bb85650c2087a3712d0ec49d5f47d9edf9ce39786d02b8582"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:d3044149ee65a893aae9e10f5ceb9c4f92e8bf6f1d43faf959279009d79f8778", "1.12.0--r42hdfd78af_0": "sha256:27ca8e5786a305043cce745836522d406ccdd80564eb9d1b118dbb6b22816dff", "1.14.0--r43hdfd78af_0": "sha256:c49d9820cab85f761a6cb22da70ef8e5112ef547bccf901f3572bb0648c77aa0", "1.16.0--r43hdfd78af_0": "sha256:2eb87098f4e03cb11ac72d8894ebec916abe59e09b3fbbda53764e0ccaf2773e", "1.20.0--r44hdfd78af_0": "sha256:82d5ddbc663bd17bb85650c2087a3712d0ec49d5f47d9edf9ce39786d02b8582"}, "docker": "quay.io/biocontainers/bioconductor-proda"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proda.
shpc-registry automated BioContainers addition for bioconductor-proda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proda:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proda/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-proda/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-proda

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