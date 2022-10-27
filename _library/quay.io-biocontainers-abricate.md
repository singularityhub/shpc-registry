---
layout: container
name:  "quay.io/biocontainers/abricate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abricate/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abricate/container.yaml"
updated_at: "2022-10-27 01:10:27.509868"
latest: "1.0.1--ha8f3691_1"
container_url: "https://biocontainers.pro/tools/abricate"
aliases:
 - "abricate"
 - "abricate-get_db"
versions:
 - "1.0.1--ha8f3691_1"
description: "shpc-registry automated BioContainers addition for abricate"
config: {"url": "https://biocontainers.pro/tools/abricate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abricate", "latest": {"1.0.1--ha8f3691_1": "sha256:9de8b0d3edb97f9946ac8d57e2a1207d48801ae7a3b1f263f0a0e5773904451e"}, "tags": {"1.0.1--ha8f3691_1": "sha256:9de8b0d3edb97f9946ac8d57e2a1207d48801ae7a3b1f263f0a0e5773904451e"}, "docker": "quay.io/biocontainers/abricate", "aliases": {"abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abricate.
shpc-registry automated BioContainers addition for abricate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abricate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abricate:1.0.1--ha8f3691_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abricate/1.0.1--ha8f3691_1
$ module help quay.io/biocontainers/abricate/1.0.1--ha8f3691_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abricate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abricate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abricate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abricate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abricate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abricate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
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