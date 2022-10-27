---
layout: container
name:  "quay.io/biocontainers/optimir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/optimir/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/optimir/container.yaml"
updated_at: "2022-10-27 01:11:34.256032"
latest: "1.2--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/optimir"
aliases:
 - "optimir"
versions:
 - "1.2--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for optimir"
config: {"url": "https://biocontainers.pro/tools/optimir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for optimir", "latest": {"1.2--pyh5e36f6f_0": "sha256:7fa9916e26968a11683af4278f9347ad538a16b1ec9e54f14d9ac21fadce009f"}, "tags": {"1.2--pyh5e36f6f_0": "sha256:7fa9916e26968a11683af4278f9347ad538a16b1ec9e54f14d9ac21fadce009f"}, "docker": "quay.io/biocontainers/optimir", "aliases": {"optimir": "/usr/local/bin/optimir"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/optimir.
shpc-registry automated BioContainers addition for optimir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/optimir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/optimir:1.2--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/optimir/1.2--pyh5e36f6f_0
$ module help quay.io/biocontainers/optimir/1.2--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### optimir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### optimir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### optimir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### optimir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### optimir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### optimir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### optimir

```bash
$ singularity exec <container> /usr/local/bin/optimir
$ podman run --it --rm --entrypoint /usr/local/bin/optimir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optimir   -v ${PWD} -w ${PWD} <container> -c " $@"
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