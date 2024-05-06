---
layout: container
name:  "quay.io/biocontainers/pglite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pglite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pglite/container.yaml"
updated_at: "2024-05-06 02:48:26.193574"
latest: "0.1--0"
container_url: "https://biocontainers.pro/tools/pglite"
aliases:
 - "pglite"
versions:
 - "0.1--0"
description: "shpc-registry automated BioContainers addition for pglite"
config: {"url": "https://biocontainers.pro/tools/pglite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pglite", "latest": {"0.1--0": "sha256:9b1d0361d5a5ec3b131d1f1d3301ddf56f23c3ab9d3667a1cde37a3c6176c853"}, "tags": {"0.1--0": "sha256:9b1d0361d5a5ec3b131d1f1d3301ddf56f23c3ab9d3667a1cde37a3c6176c853"}, "docker": "quay.io/biocontainers/pglite", "aliases": {"pglite": "/usr/local/bin/pglite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pglite.
shpc-registry automated BioContainers addition for pglite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pglite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pglite:0.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pglite/0.1--0
$ module help quay.io/biocontainers/pglite/0.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pglite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pglite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pglite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pglite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pglite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pglite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pglite

```bash
$ singularity exec <container> /usr/local/bin/pglite
$ podman run --it --rm --entrypoint /usr/local/bin/pglite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pglite   -v ${PWD} -w ${PWD} <container> -c " $@"
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