---
layout: container
name:  "quay.io/biocontainers/gsort"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gsort/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gsort/container.yaml"
updated_at: "2024-09-16 03:27:26.750063"
latest: "0.1.4--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/gsort"
aliases:
 - "gsort"
versions:
 - "0.1.4--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for gsort"
config: {"url": "https://biocontainers.pro/tools/gsort", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gsort", "latest": {"0.1.4--h9ee0642_1": "sha256:541997a3c49e03dd7ea26de2f144830636f0f9b378ff04ae12a6c82d1f9f9d03"}, "tags": {"0.1.4--h9ee0642_1": "sha256:541997a3c49e03dd7ea26de2f144830636f0f9b378ff04ae12a6c82d1f9f9d03"}, "docker": "quay.io/biocontainers/gsort", "aliases": {"gsort": "/usr/local/bin/gsort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gsort.
shpc-registry automated BioContainers addition for gsort
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gsort
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gsort:0.1.4--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gsort/0.1.4--h9ee0642_1
$ module help quay.io/biocontainers/gsort/0.1.4--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gsort-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gsort-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gsort-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gsort-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gsort-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gsort-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gsort

```bash
$ singularity exec <container> /usr/local/bin/gsort
$ podman run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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