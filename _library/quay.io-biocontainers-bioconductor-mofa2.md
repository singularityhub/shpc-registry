---
layout: container
name:  "quay.io/biocontainers/bioconductor-mofa2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mofa2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mofa2/container.yaml"
updated_at: "2023-12-09 03:01:37.494727"
latest: "1.10.0--r43h9ee0642_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mofa2"

versions:
 - "1.4.0--r41h9ee0642_0"
 - "1.8.0--r42h9ee0642_0"
 - "1.10.0--r43h9ee0642_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mofa2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mofa2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mofa2", "latest": {"1.10.0--r43h9ee0642_0": "sha256:e862f6b999b61233fa0d163466e163f25b5d7a13698abec1265ca653ef1b3fdb"}, "tags": {"1.4.0--r41h9ee0642_0": "sha256:f392e6e982fa61fb19a3d9e476d7a8643902e46675bc8ada3ea6733d22860f99", "1.8.0--r42h9ee0642_0": "sha256:c26430c8d51f239058f8a08ba6c2ef516c555b543b9c2065b25edeca08442674", "1.10.0--r43h9ee0642_0": "sha256:e862f6b999b61233fa0d163466e163f25b5d7a13698abec1265ca653ef1b3fdb"}, "docker": "quay.io/biocontainers/bioconductor-mofa2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mofa2.
shpc-registry automated BioContainers addition for bioconductor-mofa2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mofa2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mofa2:1.10.0--r43h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mofa2/1.10.0--r43h9ee0642_0
$ module help quay.io/biocontainers/bioconductor-mofa2/1.10.0--r43h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mofa2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mofa2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mofa2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mofa2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mofa2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mofa2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mofa2

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