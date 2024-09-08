---
layout: container
name:  "quay.io/biocontainers/r-orqa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-orqa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-orqa/container.yaml"
updated_at: "2024-09-08 03:26:09.842260"
latest: "0.2.1--r43h21a89ab_10"
container_url: "https://biocontainers.pro/tools/r-orqa"

versions:
 - "0.2.1--r41hecf12ef_7"
 - "0.2.1--r42hecf12ef_8"
 - "0.2.1--r42h21a89ab_9"
 - "0.2.1--r43h21a89ab_10"
description: "shpc-registry automated BioContainers addition for r-orqa"
config: {"url": "https://biocontainers.pro/tools/r-orqa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-orqa", "latest": {"0.2.1--r43h21a89ab_10": "sha256:c8f90f3cd00f68cc1220c2325029284c4478386bee081e6e4e0c591596ddb12a"}, "tags": {"0.2.1--r41hecf12ef_7": "sha256:7a5479ea1c982cdbe57c58dab2235bfa7aa038f32e08a6ff1621aacfc0e57fbc", "0.2.1--r42hecf12ef_8": "sha256:6694ffb52109816c4f604690d8fcbb71163d49dbc7bd619bc9f090d7f2b879dd", "0.2.1--r42h21a89ab_9": "sha256:1130bc6c0649d6b8ab560d6291607acf332f87775e5d29bf8ab16414cc1df2ae", "0.2.1--r43h21a89ab_10": "sha256:c8f90f3cd00f68cc1220c2325029284c4478386bee081e6e4e0c591596ddb12a"}, "docker": "quay.io/biocontainers/r-orqa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-orqa.
shpc-registry automated BioContainers addition for r-orqa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-orqa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-orqa:0.2.1--r43h21a89ab_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-orqa/0.2.1--r43h21a89ab_10
$ module help quay.io/biocontainers/r-orqa/0.2.1--r43h21a89ab_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-orqa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-orqa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-orqa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-orqa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-orqa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-orqa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-orqa

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