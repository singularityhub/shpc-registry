---
layout: container
name:  "quay.io/biocontainers/bioconductor-globalseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-globalseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-globalseq/container.yaml"
updated_at: "2023-12-06 02:31:07.274876"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-globalseq"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-globalseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-globalseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-globalseq", "latest": {"1.30.0--r43hdfd78af_0": "sha256:8c19c24849a0d3f671e1accc60073855a11aebc1d9c70fae40e5f2e768a80da5"}, "tags": {"1.8.0--r351_0": "sha256:f09ebf3fe3800aadcd0041448e1ab4f9d4245b6ff7201c41e133d918d628f2af", "1.26.0--r42hdfd78af_0": "sha256:a3ee04e64274a5070dac442bf358b0f2b4649c262748cf818e3066b8ef54c30f", "1.22.0--r41hdfd78af_0": "sha256:7b19ba84385a9350c59275517789f63a2d28b4189f2d8b30b6851c0edfe98684", "1.20.0--r41hdfd78af_0": "sha256:322b0d782e7e59a6fec428c0ce2d698f71154e058335d3ebe8cd8eaeffb633b2", "1.18.0--r40hdfd78af_1": "sha256:510e9130fe7324878bd9baf24a8a11f5f06e2098c4114b49e7c60fb654d6eac3", "1.16.0--r40_0": "sha256:c4e0dbd62e99fc08afd596d46808985a6758db1b50843b90f9cda1644fe4dddf", "1.28.0--r43hdfd78af_0": "sha256:ce3b8b64b86066d56ffdeb3eda40d4e6db7e9f348bdd42466b8973151335390b", "1.30.0--r43hdfd78af_0": "sha256:8c19c24849a0d3f671e1accc60073855a11aebc1d9c70fae40e5f2e768a80da5"}, "docker": "quay.io/biocontainers/bioconductor-globalseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-globalseq.
shpc-registry automated BioContainers addition for bioconductor-globalseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-globalseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-globalseq:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-globalseq/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-globalseq/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-globalseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-globalseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-globalseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-globalseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-globalseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-globalseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-globalseq

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