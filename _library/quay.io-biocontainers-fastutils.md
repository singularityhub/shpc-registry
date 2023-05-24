---
layout: container
name:  "quay.io/biocontainers/fastutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastutils/container.yaml"
updated_at: "2023-05-24 03:18:34.654251"
latest: "0.3--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/fastutils"
aliases:
 - "fastutils"
versions:
 - "0.3--hd03093a_2"
 - "0.3--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for fastutils"
config: {"url": "https://biocontainers.pro/tools/fastutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastutils", "latest": {"0.3--hdcf5f25_4": "sha256:748a27be745748a3772407038710c45878c813fb3485e4ff5471fe5f58e59866"}, "tags": {"0.3--hd03093a_2": "sha256:742f84851fbf62a76365eb2a6e001596e79f7ef3d194c29f53b3e57efaf3b8ab", "0.3--hdcf5f25_4": "sha256:748a27be745748a3772407038710c45878c813fb3485e4ff5471fe5f58e59866"}, "docker": "quay.io/biocontainers/fastutils", "aliases": {"fastutils": "/usr/local/bin/fastutils"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastutils.
shpc-registry automated BioContainers addition for fastutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastutils:0.3--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastutils/0.3--hdcf5f25_4
$ module help quay.io/biocontainers/fastutils/0.3--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastutils

```bash
$ singularity exec <container> /usr/local/bin/fastutils
$ podman run --it --rm --entrypoint /usr/local/bin/fastutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastutils   -v ${PWD} -w ${PWD} <container> -c " $@"
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