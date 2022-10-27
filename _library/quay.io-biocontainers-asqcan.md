---
layout: container
name:  "quay.io/biocontainers/asqcan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/asqcan/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/asqcan/container.yaml"
updated_at: "2022-10-27 00:27:17.371024"
latest: "0.2--py_2"
container_url: "https://biocontainers.pro/tools/asqcan"
aliases:
 - "asqcan"
 - "blobtools"
 - "blobtools-build_nodesdb"
versions:
 - "0.2--py_2"
description: "shpc-registry automated BioContainers addition for asqcan"
config: {"url": "https://biocontainers.pro/tools/asqcan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for asqcan", "latest": {"0.2--py_2": "sha256:d610b3b88acf999b7d60b8ab802c422e7bdd3566bf79ab1810009c3a90905086"}, "tags": {"0.2--py_2": "sha256:d610b3b88acf999b7d60b8ab802c422e7bdd3566bf79ab1810009c3a90905086"}, "docker": "quay.io/biocontainers/asqcan", "aliases": {"asqcan": "/usr/local/bin/asqcan", "blobtools": "/usr/local/bin/blobtools", "blobtools-build_nodesdb": "/usr/local/bin/blobtools-build_nodesdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/asqcan.
shpc-registry automated BioContainers addition for asqcan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/asqcan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/asqcan:0.2--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/asqcan/0.2--py_2
$ module help quay.io/biocontainers/asqcan/0.2--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### asqcan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### asqcan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### asqcan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### asqcan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### asqcan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### asqcan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asqcan

```bash
$ singularity exec <container> /usr/local/bin/asqcan
$ podman run --it --rm --entrypoint /usr/local/bin/asqcan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asqcan   -v ${PWD} -w ${PWD} <container> -c " $@"
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