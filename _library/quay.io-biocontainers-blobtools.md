---
layout: container
name:  "quay.io/biocontainers/blobtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blobtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/blobtools/container.yaml"
updated_at: "2022-10-27 00:53:49.736113"
latest: "1.1.1--py_1"
container_url: "https://biocontainers.pro/tools/blobtools"
aliases:
 - "blobtools"
 - "blobtools-build_nodesdb"
versions:
 - "1.1.1--py_1"
description: "shpc-registry automated BioContainers addition for blobtools"
config: {"url": "https://biocontainers.pro/tools/blobtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blobtools", "latest": {"1.1.1--py_1": "sha256:0803c20d87fd54c2c5b03f2d7e7ae15c119dacfc3368379ff7a5f48264cff755"}, "tags": {"1.1.1--py_1": "sha256:0803c20d87fd54c2c5b03f2d7e7ae15c119dacfc3368379ff7a5f48264cff755"}, "docker": "quay.io/biocontainers/blobtools", "aliases": {"blobtools": "/usr/local/bin/blobtools", "blobtools-build_nodesdb": "/usr/local/bin/blobtools-build_nodesdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blobtools.
shpc-registry automated BioContainers addition for blobtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blobtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blobtools:1.1.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blobtools/1.1.1--py_1
$ module help quay.io/biocontainers/blobtools/1.1.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blobtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blobtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blobtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blobtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blobtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blobtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blobtools

```bash
$ singularity exec <container> /usr/local/bin/blobtools
$ podman run --it --rm --entrypoint /usr/local/bin/blobtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blobtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blobtools-build_nodesdb

```bash
$ singularity exec <container> /usr/local/bin/blobtools-build_nodesdb
$ podman run --it --rm --entrypoint /usr/local/bin/blobtools-build_nodesdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blobtools-build_nodesdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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