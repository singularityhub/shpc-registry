---
layout: container
name:  "quay.io/biocontainers/ganon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ganon/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ganon/container.yaml"
updated_at: "2022-10-27 01:10:57.487077"
latest: "1.1.2--py38h80bae55_1"
container_url: "https://biocontainers.pro/tools/ganon"
aliases:
 - "binpacking"
 - "ganon"
 - "ganon-build"
 - "ganon-classify"
 - "ganon-get-seq-info.sh"
 - "taxsbp"
versions:
 - "1.1.2--py38h80bae55_1"
description: "shpc-registry automated BioContainers addition for ganon"
config: {"url": "https://biocontainers.pro/tools/ganon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ganon", "latest": {"1.1.2--py38h80bae55_1": "sha256:80637fc5693e890f44ba56cdc00e407e319d7063801dfdeb178a53a9112d0594"}, "tags": {"1.1.2--py38h80bae55_1": "sha256:80637fc5693e890f44ba56cdc00e407e319d7063801dfdeb178a53a9112d0594"}, "docker": "quay.io/biocontainers/ganon", "aliases": {"binpacking": "/usr/local/bin/binpacking", "ganon": "/usr/local/bin/ganon", "ganon-build": "/usr/local/bin/ganon-build", "ganon-classify": "/usr/local/bin/ganon-classify", "ganon-get-seq-info.sh": "/usr/local/bin/ganon-get-seq-info.sh", "taxsbp": "/usr/local/bin/taxsbp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ganon.
shpc-registry automated BioContainers addition for ganon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ganon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ganon:1.1.2--py38h80bae55_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ganon/1.1.2--py38h80bae55_1
$ module help quay.io/biocontainers/ganon/1.1.2--py38h80bae55_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ganon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ganon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ganon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ganon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ganon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ganon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binpacking

```bash
$ singularity exec <container> /usr/local/bin/binpacking
$ podman run --it --rm --entrypoint /usr/local/bin/binpacking   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binpacking   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon

```bash
$ singularity exec <container> /usr/local/bin/ganon
$ podman run --it --rm --entrypoint /usr/local/bin/ganon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-build

```bash
$ singularity exec <container> /usr/local/bin/ganon-build
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-classify

```bash
$ singularity exec <container> /usr/local/bin/ganon-classify
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-classify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-classify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-get-seq-info.sh

```bash
$ singularity exec <container> /usr/local/bin/ganon-get-seq-info.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-get-seq-info.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-get-seq-info.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxsbp

```bash
$ singularity exec <container> /usr/local/bin/taxsbp
$ podman run --it --rm --entrypoint /usr/local/bin/taxsbp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxsbp   -v ${PWD} -w ${PWD} <container> -c " $@"
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