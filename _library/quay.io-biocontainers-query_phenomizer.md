---
layout: container
name:  "quay.io/biocontainers/query_phenomizer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/query_phenomizer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/query_phenomizer/container.yaml"
updated_at: "2024-04-22 02:27:43.290229"
latest: "1.2.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/query_phenomizer"

versions:
 - "1.2--py_0"
 - "1.2.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for query_phenomizer"
config: {"url": "https://biocontainers.pro/tools/query_phenomizer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for query_phenomizer", "latest": {"1.2.1--pyh7cba7a3_0": "sha256:1b6c024e801886c110b871798c40376977e05b4536b4b4d6d0761501f0269684"}, "tags": {"1.2--py_0": "sha256:0cc7d4dd094b950d36b3ac2162e628e20fa44ad2610eaa861b652a04ee32e38f", "1.2.1--pyh7cba7a3_0": "sha256:1b6c024e801886c110b871798c40376977e05b4536b4b4d6d0761501f0269684"}, "docker": "quay.io/biocontainers/query_phenomizer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/query_phenomizer.
shpc-registry automated BioContainers addition for query_phenomizer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/query_phenomizer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/query_phenomizer:1.2.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/query_phenomizer/1.2.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/query_phenomizer/1.2.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### query_phenomizer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### query_phenomizer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### query_phenomizer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### query_phenomizer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### query_phenomizer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### query_phenomizer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### query_phenomizer

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