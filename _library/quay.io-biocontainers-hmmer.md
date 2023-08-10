---
layout: container
name:  "quay.io/biocontainers/hmmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmmer/container.yaml"
updated_at: "2023-08-10 03:06:12.158163"
latest: "3.3.2--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/hmmer"

versions:
 - "3.3.2--h87f3376_2"
 - "3.3.2--h87f3376_3"
 - "3.3.2--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for hmmer"
config: {"url": "https://biocontainers.pro/tools/hmmer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmmer", "latest": {"3.3.2--hdbdd923_4": "sha256:0398c520c477e8a1d638dd20d4f5014fad805ace67534e6a049f1907e4fecc00"}, "tags": {"3.3.2--h87f3376_2": "sha256:9fa6fb904bbd8bcaf5ecbb15affaad82d7b6b3ab8afc1a369d362d2c061f1237", "3.3.2--h87f3376_3": "sha256:6a80a68fe5f186ecc3e636636f5933e050ecca9c7f27692ee6af63fd3b97e467", "3.3.2--hdbdd923_4": "sha256:0398c520c477e8a1d638dd20d4f5014fad805ace67534e6a049f1907e4fecc00"}, "docker": "quay.io/biocontainers/hmmer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmer.
shpc-registry automated BioContainers addition for hmmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmer:3.3.2--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmer/3.3.2--hdbdd923_4
$ module help quay.io/biocontainers/hmmer/3.3.2--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### hmmer

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