---
layout: container
name:  "quay.io/biocontainers/bioconductor-scbfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scbfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scbfa/container.yaml"
updated_at: "2024-09-19 02:49:30.829518"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scbfa"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scbfa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scbfa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scbfa", "latest": {"1.16.0--r43hdfd78af_0": "sha256:36cf964193dcab1a8aeb0d345aee5e9028231aea30a9c7e8d0e1ccc4e68353d8"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:609374ff73f9118ab6fdc27b303173af4574394ad6bccf1dca5f9c9509d1c9d0", "1.12.0--r42hdfd78af_0": "sha256:d133b2b2321076d696a9372bfb14a41ba72ecce657dd44379cf97aef50c9622a", "1.14.0--r43hdfd78af_0": "sha256:1c95e7c9716e96ccbbb9a5f812d9856d46355d9de6a591dc039b6790d0611576", "1.16.0--r43hdfd78af_0": "sha256:36cf964193dcab1a8aeb0d345aee5e9028231aea30a9c7e8d0e1ccc4e68353d8"}, "docker": "quay.io/biocontainers/bioconductor-scbfa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scbfa.
shpc-registry automated BioContainers addition for bioconductor-scbfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scbfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scbfa:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scbfa/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scbfa/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scbfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scbfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scbfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scbfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scbfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scbfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scbfa

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