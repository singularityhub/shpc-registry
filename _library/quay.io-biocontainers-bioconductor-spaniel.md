---
layout: container
name:  "quay.io/biocontainers/bioconductor-spaniel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spaniel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spaniel/container.yaml"
updated_at: "2025-06-14 03:44:49.698489"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spaniel"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spaniel"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spaniel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spaniel", "latest": {"1.20.0--r44hdfd78af_0": "sha256:c105ed12c56ceccf378a1dfa1645e90169e633b869c40015c973b6744de738c7"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:17974275754ba1793796bafef5cf399c6a95701fe3d42df13049cc2b49428030", "1.12.0--r42hdfd78af_0": "sha256:07e30eb78f675a5944554737955d71e4de70fdf238dceb5ed8e792bcde6176c4", "1.14.0--r43hdfd78af_0": "sha256:3c2bb04974d02233f0bc6d4f9e7c4a1be681bcdb6666cbf75be71e2353d41bfe", "1.16.0--r43hdfd78af_0": "sha256:dc03e7f58c2acdc60733f87a60c50ba134918ef50342d40105b2c9870265b816", "1.20.0--r44hdfd78af_0": "sha256:c105ed12c56ceccf378a1dfa1645e90169e633b869c40015c973b6744de738c7"}, "docker": "quay.io/biocontainers/bioconductor-spaniel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spaniel.
shpc-registry automated BioContainers addition for bioconductor-spaniel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spaniel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spaniel:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spaniel/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spaniel/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spaniel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spaniel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spaniel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spaniel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spaniel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spaniel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spaniel

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