---
layout: container
name:  "quay.io/biocontainers/bioconductor-dearseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dearseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dearseq/container.yaml"
updated_at: "2024-11-10 03:40:41.346030"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dearseq"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.1--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dearseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dearseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dearseq", "latest": {"1.14.0--r43hdfd78af_0": "sha256:4ec777431189bb40605aeaca1a42979b19248b68e06b0c01b2f5416ec81ddcee"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:6a7a747130e39ba7a83563bcfe9c848f7490e050909487bbf735a24f3af5623b", "1.10.0--r42hdfd78af_0": "sha256:4d408c45a0bccb572cb1d7aac19dd8c8cd9807aa0d215cae572b824f7eb14b97", "1.12.1--r43hdfd78af_0": "sha256:8565b818e2116197f394aa4f78473a86a47c4808f64b96d03720867d6194dcca", "1.14.0--r43hdfd78af_0": "sha256:4ec777431189bb40605aeaca1a42979b19248b68e06b0c01b2f5416ec81ddcee"}, "docker": "quay.io/biocontainers/bioconductor-dearseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dearseq.
shpc-registry automated BioContainers addition for bioconductor-dearseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dearseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dearseq:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dearseq/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dearseq/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dearseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dearseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dearseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dearseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dearseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dearseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dearseq

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