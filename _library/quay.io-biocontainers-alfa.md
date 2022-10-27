---
layout: container
name:  "quay.io/biocontainers/alfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alfa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/alfa/container.yaml"
updated_at: "2022-10-27 00:43:52.247919"
latest: "1.1.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/alfa"
aliases:
 - "alfa"
versions:
 - "1.1.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for alfa"
config: {"url": "https://biocontainers.pro/tools/alfa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for alfa", "latest": {"1.1.1--pyh5e36f6f_0": "sha256:fcb14e5153096d7faada4911989566038f1eca4899db82706478a360fe9af660"}, "tags": {"1.1.1--pyh5e36f6f_0": "sha256:fcb14e5153096d7faada4911989566038f1eca4899db82706478a360fe9af660"}, "docker": "quay.io/biocontainers/alfa", "aliases": {"alfa": "/usr/local/bin/alfa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alfa.
shpc-registry automated BioContainers addition for alfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alfa:1.1.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alfa/1.1.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/alfa/1.1.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alfa

```bash
$ singularity exec <container> /usr/local/bin/alfa
$ podman run --it --rm --entrypoint /usr/local/bin/alfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alfa   -v ${PWD} -w ${PWD} <container> -c " $@"
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