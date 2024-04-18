---
layout: container
name:  "quay.io/biocontainers/soapsplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapsplice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapsplice/container.yaml"
updated_at: "2024-04-18 03:20:20.305330"
latest: "1.10--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/soapsplice"
aliases:
 - "2bwt-builder"
 - "soapsplice"
versions:
 - "1.10--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for soapsplice"
config: {"url": "https://biocontainers.pro/tools/soapsplice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapsplice", "latest": {"1.10--h9ee0642_3": "sha256:11c0f0136c991a61d27525837c28a42535fcb8f476872ca6c7a8b2b5b98b6fcf"}, "tags": {"1.10--h9ee0642_3": "sha256:11c0f0136c991a61d27525837c28a42535fcb8f476872ca6c7a8b2b5b98b6fcf"}, "docker": "quay.io/biocontainers/soapsplice", "aliases": {"2bwt-builder": "/usr/local/bin/2bwt-builder", "soapsplice": "/usr/local/bin/soapsplice"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapsplice.
shpc-registry automated BioContainers addition for soapsplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapsplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapsplice:1.10--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapsplice/1.10--h9ee0642_3
$ module help quay.io/biocontainers/soapsplice/1.10--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapsplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapsplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapsplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapsplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapsplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapsplice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2bwt-builder

```bash
$ singularity exec <container> /usr/local/bin/2bwt-builder
$ podman run --it --rm --entrypoint /usr/local/bin/2bwt-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2bwt-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soapsplice

```bash
$ singularity exec <container> /usr/local/bin/soapsplice
$ podman run --it --rm --entrypoint /usr/local/bin/soapsplice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soapsplice   -v ${PWD} -w ${PWD} <container> -c " $@"
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