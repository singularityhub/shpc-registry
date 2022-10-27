---
layout: container
name:  "quay.io/biocontainers/sierrapy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sierrapy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sierrapy/container.yaml"
updated_at: "2022-10-27 00:19:06.913080"
latest: "0.4.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/sierrapy"
aliases:
 - "gql-cli"
 - "sierrapy"
versions:
 - "0.4.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for sierrapy"
config: {"url": "https://biocontainers.pro/tools/sierrapy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sierrapy", "latest": {"0.4.1--pyh7cba7a3_0": "sha256:3e197e4530011075c0228c07976cd0567bd89c07296b76d0a9b5aae481ba53c7"}, "tags": {"0.4.1--pyh7cba7a3_0": "sha256:3e197e4530011075c0228c07976cd0567bd89c07296b76d0a9b5aae481ba53c7"}, "docker": "quay.io/biocontainers/sierrapy", "aliases": {"gql-cli": "/usr/local/bin/gql-cli", "sierrapy": "/usr/local/bin/sierrapy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sierrapy.
shpc-registry automated BioContainers addition for sierrapy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sierrapy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sierrapy:0.4.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sierrapy/0.4.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/sierrapy/0.4.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sierrapy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sierrapy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sierrapy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sierrapy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sierrapy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sierrapy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gql-cli

```bash
$ singularity exec <container> /usr/local/bin/gql-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sierrapy

```bash
$ singularity exec <container> /usr/local/bin/sierrapy
$ podman run --it --rm --entrypoint /usr/local/bin/sierrapy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sierrapy   -v ${PWD} -w ${PWD} <container> -c " $@"
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