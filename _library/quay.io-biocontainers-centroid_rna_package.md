---
layout: container
name:  "quay.io/biocontainers/centroid_rna_package"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/centroid_rna_package/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/centroid_rna_package/container.yaml"
updated_at: "2022-10-27 00:49:27.351927"
latest: "0.0.16--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/centroid_rna_package"
aliases:
 - "centroid_alifold"
 - "centroid_fold"
 - "centroid_homfold"
versions:
 - "0.0.16--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for centroid_rna_package"
config: {"url": "https://biocontainers.pro/tools/centroid_rna_package", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for centroid_rna_package", "latest": {"0.0.16--h9ee0642_1": "sha256:aefd53ebc952defcf38f63a12dddf24c20426971d0533b81d25789572aecad57"}, "tags": {"0.0.16--h9ee0642_1": "sha256:aefd53ebc952defcf38f63a12dddf24c20426971d0533b81d25789572aecad57"}, "docker": "quay.io/biocontainers/centroid_rna_package", "aliases": {"centroid_alifold": "/usr/local/bin/centroid_alifold", "centroid_fold": "/usr/local/bin/centroid_fold", "centroid_homfold": "/usr/local/bin/centroid_homfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/centroid_rna_package.
shpc-registry automated BioContainers addition for centroid_rna_package
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/centroid_rna_package
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/centroid_rna_package:0.0.16--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/centroid_rna_package/0.0.16--h9ee0642_1
$ module help quay.io/biocontainers/centroid_rna_package/0.0.16--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### centroid_rna_package-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### centroid_rna_package-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### centroid_rna_package-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### centroid_rna_package-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### centroid_rna_package-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### centroid_rna_package-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centroid_alifold

```bash
$ singularity exec <container> /usr/local/bin/centroid_alifold
$ podman run --it --rm --entrypoint /usr/local/bin/centroid_alifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centroid_alifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centroid_fold

```bash
$ singularity exec <container> /usr/local/bin/centroid_fold
$ podman run --it --rm --entrypoint /usr/local/bin/centroid_fold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centroid_fold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centroid_homfold

```bash
$ singularity exec <container> /usr/local/bin/centroid_homfold
$ podman run --it --rm --entrypoint /usr/local/bin/centroid_homfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centroid_homfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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