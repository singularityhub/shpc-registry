---
layout: container
name:  "quay.io/biocontainers/selectfasta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/selectfasta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/selectfasta/container.yaml"
updated_at: "2024-04-04 04:29:30.744598"
latest: "3.1--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/selectfasta"
aliases:
 - "selectFasta"
versions:
 - "1.0--h87f3376_2"
 - "2.0--h87f3376_0"
 - "2.0--hdbdd923_2"
 - "3.1--hdbdd923_0"
description: "shpc-registry automated BioContainers addition for selectfasta"
config: {"url": "https://biocontainers.pro/tools/selectfasta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for selectfasta", "latest": {"3.1--hdbdd923_0": "sha256:b142cb8a657b064966be6c904f082ddf439a95848bdfcdb3d570a225fe451d37"}, "tags": {"1.0--h87f3376_2": "sha256:0ab0962da29d3fa98022c74ef21fc5df2dedefd209e836a96102d20891e7ab7e", "2.0--h87f3376_0": "sha256:c369e5483e8b17ecfc6df02595548d1f8e0b5faed2ad412da805e0fa43992893", "2.0--hdbdd923_2": "sha256:81cc6c14a49e76e9edc3b8567454fc7cdeaa0a33c5c3a1c584b3852d94088fcb", "3.1--hdbdd923_0": "sha256:b142cb8a657b064966be6c904f082ddf439a95848bdfcdb3d570a225fe451d37"}, "docker": "quay.io/biocontainers/selectfasta", "aliases": {"selectFasta": "/usr/local/bin/selectFasta"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/selectfasta.
shpc-registry automated BioContainers addition for selectfasta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/selectfasta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/selectfasta:3.1--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/selectfasta/3.1--hdbdd923_0
$ module help quay.io/biocontainers/selectfasta/3.1--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### selectfasta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### selectfasta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### selectfasta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### selectfasta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### selectfasta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### selectfasta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### selectFasta

```bash
$ singularity exec <container> /usr/local/bin/selectFasta
$ podman run --it --rm --entrypoint /usr/local/bin/selectFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selectFasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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