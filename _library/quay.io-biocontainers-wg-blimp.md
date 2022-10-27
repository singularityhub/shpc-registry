---
layout: container
name:  "quay.io/biocontainers/wg-blimp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wg-blimp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/wg-blimp/container.yaml"
updated_at: "2022-10-27 00:34:05.981103"
latest: "0.9.9--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/wg-blimp"
aliases:
 - "wg-blimp"
versions:
 - "0.9.9--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for wg-blimp"
config: {"url": "https://biocontainers.pro/tools/wg-blimp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wg-blimp", "latest": {"0.9.9--pyh5e36f6f_0": "sha256:511443539165a79a647ae77ab960d57fe450f0e25b613d680c199bf8d4621475"}, "tags": {"0.9.9--pyh5e36f6f_0": "sha256:511443539165a79a647ae77ab960d57fe450f0e25b613d680c199bf8d4621475"}, "docker": "quay.io/biocontainers/wg-blimp", "aliases": {"wg-blimp": "/usr/local/bin/wg-blimp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wg-blimp.
shpc-registry automated BioContainers addition for wg-blimp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wg-blimp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wg-blimp:0.9.9--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wg-blimp/0.9.9--pyh5e36f6f_0
$ module help quay.io/biocontainers/wg-blimp/0.9.9--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wg-blimp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wg-blimp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wg-blimp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wg-blimp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wg-blimp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wg-blimp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wg-blimp

```bash
$ singularity exec <container> /usr/local/bin/wg-blimp
$ podman run --it --rm --entrypoint /usr/local/bin/wg-blimp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wg-blimp   -v ${PWD} -w ${PWD} <container> -c " $@"
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