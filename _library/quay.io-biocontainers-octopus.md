---
layout: container
name:  "quay.io/biocontainers/octopus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/octopus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/octopus/container.yaml"
updated_at: "2024-12-26 03:28:24.510544"
latest: "0.7.4--ha3c1580_2"
container_url: "https://biocontainers.pro/tools/octopus"
aliases:
 - "octopus"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.7.4--ha3c1580_2"
description: "shpc-registry automated BioContainers addition for octopus"
config: {"url": "https://biocontainers.pro/tools/octopus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for octopus", "latest": {"0.7.4--ha3c1580_2": "sha256:342401712c1cb3f3e63fa01ab931a59bc1801ab75de95f1c2b3fb5b15d643db1"}, "tags": {"0.7.4--ha3c1580_2": "sha256:342401712c1cb3f3e63fa01ab931a59bc1801ab75de95f1c2b3fb5b15d643db1"}, "docker": "quay.io/biocontainers/octopus", "aliases": {"octopus": "/usr/local/bin/octopus", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/octopus.
shpc-registry automated BioContainers addition for octopus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/octopus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/octopus:0.7.4--ha3c1580_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/octopus/0.7.4--ha3c1580_2
$ module help quay.io/biocontainers/octopus/0.7.4--ha3c1580_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### octopus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### octopus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### octopus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### octopus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### octopus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### octopus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### octopus

```bash
$ singularity exec <container> /usr/local/bin/octopus
$ podman run --it --rm --entrypoint /usr/local/bin/octopus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octopus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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