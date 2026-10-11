---
layout: container
name:  "quay.io/biocontainers/flashpca2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flashpca2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flashpca2/container.yaml"
updated_at: "2026-10-11 09:00:21.599613"
latest: "2.0--ha987a51_0"
container_url: "https://biocontainers.pro/tools/flashpca2"
aliases:
 - "flashpca"
versions:
 - "2.0--ha987a51_0"
description: "singularity registry hpc automated addition for flashpca2"
config: {"url": "https://biocontainers.pro/tools/flashpca2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for flashpca2", "latest": {"2.0--ha987a51_0": "sha256:4c4b9bff4f1000b5b2ba1704f5fef715d70c963ae6ad3075423417c5ff806045"}, "tags": {"2.0--ha987a51_0": "sha256:4c4b9bff4f1000b5b2ba1704f5fef715d70c963ae6ad3075423417c5ff806045"}, "docker": "quay.io/biocontainers/flashpca2", "aliases": {"flashpca": "/usr/local/bin/flashpca"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flashpca2.
singularity registry hpc automated addition for flashpca2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flashpca2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flashpca2:2.0--ha987a51_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flashpca2/2.0--ha987a51_0
$ module help quay.io/biocontainers/flashpca2/2.0--ha987a51_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flashpca2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flashpca2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flashpca2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flashpca2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flashpca2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flashpca2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flashpca

```bash
$ singularity exec <container> /usr/local/bin/flashpca
$ podman run --it --rm --entrypoint /usr/local/bin/flashpca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flashpca   -v ${PWD} -w ${PWD} <container> -c " $@"
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