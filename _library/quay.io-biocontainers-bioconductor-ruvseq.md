---
layout: container
name:  "quay.io/biocontainers/bioconductor-ruvseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ruvseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ruvseq/container.yaml"
updated_at: "2025-12-22 04:03:57.998970"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ruvseq"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ruvseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ruvseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ruvseq", "latest": {"1.40.0--r44hdfd78af_0": "sha256:1ff92e389ba526d5e526d722602b085732d47bc03947d44c37acb8460fbf408c"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:d038ce6abe74328ff764d4419aec07454ed3cb74e980c62988fd1628a06a40fd", "1.32.0--r42hdfd78af_0": "sha256:994cca77ccd57216f7c7068d86c07f4bd221cc3154a4d66b5a743a91c3f6002e", "1.34.0--r43hdfd78af_0": "sha256:b139f692a67fae7840919092033b9229bffc741a093585e8853d9cf28608f98c", "1.36.0--r43hdfd78af_0": "sha256:bcf1d975bc27fcc6765391d81f1b71c942364c382c30ff64466e5465473a3b39", "1.40.0--r44hdfd78af_0": "sha256:1ff92e389ba526d5e526d722602b085732d47bc03947d44c37acb8460fbf408c"}, "docker": "quay.io/biocontainers/bioconductor-ruvseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ruvseq.
shpc-registry automated BioContainers addition for bioconductor-ruvseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ruvseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ruvseq:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ruvseq/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ruvseq/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ruvseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ruvseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ruvseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ruvseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ruvseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ruvseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ruvseq

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