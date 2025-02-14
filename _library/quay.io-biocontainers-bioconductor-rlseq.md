---
layout: container
name:  "quay.io/biocontainers/bioconductor-rlseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rlseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rlseq/container.yaml"
updated_at: "2025-02-14 03:14:54.849150"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rlseq"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.1--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rlseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rlseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rlseq", "latest": {"1.6.0--r43hdfd78af_0": "sha256:2e4fbad65108f6940a958ee388a39479c6b146b5d8b6965ff465a1955593fa11"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:7b21b1cb2af6e13d2f2122bc6c83d5a8105086893e433e613d717f0c36d98df3", "1.4.1--r42hdfd78af_0": "sha256:6094e6a74ff0ff831b129f44aee665a58310b71d7c1daebe1c798c06a6fb7d6c", "1.6.0--r43hdfd78af_0": "sha256:2e4fbad65108f6940a958ee388a39479c6b146b5d8b6965ff465a1955593fa11"}, "docker": "quay.io/biocontainers/bioconductor-rlseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rlseq.
shpc-registry automated BioContainers addition for bioconductor-rlseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rlseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rlseq:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rlseq/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rlseq/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rlseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rlseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rlseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rlseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rlseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rlseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rlseq

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