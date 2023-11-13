---
layout: container
name:  "quay.io/biocontainers/pigz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pigz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pigz/container.yaml"
updated_at: "2023-11-13 03:28:33.339851"
latest: "2.3.4"
container_url: "https://biocontainers.pro/tools/pigz"
aliases:
 - "pigz"
 - "unpigz"
versions:
 - "2.3.4"
description: "shpc-registry automated BioContainers addition for pigz"
config: {"url": "https://biocontainers.pro/tools/pigz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pigz", "latest": {"2.3.4": "sha256:6309e2ad5f921ec09eab7166b68b1ea0fcb8702bee34aa499f0dca9065584c36"}, "tags": {"2.3.4": "sha256:6309e2ad5f921ec09eab7166b68b1ea0fcb8702bee34aa499f0dca9065584c36"}, "docker": "quay.io/biocontainers/pigz", "aliases": {"pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pigz.
shpc-registry automated BioContainers addition for pigz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pigz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pigz:2.3.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pigz/2.3.4
$ module help quay.io/biocontainers/pigz/2.3.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pigz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pigz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pigz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pigz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pigz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pigz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
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