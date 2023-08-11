---
layout: container
name:  "quay.io/biocontainers/smina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smina/container.yaml"
updated_at: "2023-08-11 02:54:42.714722"
latest: "2017.11.9--0"
container_url: "https://biocontainers.pro/tools/smina"
aliases:
 - "smina"
versions:
 - "2017.11.9--0"
description: "shpc-registry automated BioContainers addition for smina"
config: {"url": "https://biocontainers.pro/tools/smina", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smina", "latest": {"2017.11.9--0": "sha256:502e7be073c9ec35b996656a48e9560e05746ad6d98649c56f98af9a724875b4"}, "tags": {"2017.11.9--0": "sha256:502e7be073c9ec35b996656a48e9560e05746ad6d98649c56f98af9a724875b4"}, "docker": "quay.io/biocontainers/smina", "aliases": {"smina": "/usr/local/bin/smina"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smina.
shpc-registry automated BioContainers addition for smina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smina:2017.11.9--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smina/2017.11.9--0
$ module help quay.io/biocontainers/smina/2017.11.9--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smina-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smina

```bash
$ singularity exec <container> /usr/local/bin/smina
$ podman run --it --rm --entrypoint /usr/local/bin/smina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smina   -v ${PWD} -w ${PWD} <container> -c " $@"
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