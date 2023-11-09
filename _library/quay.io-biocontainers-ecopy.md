---
layout: container
name:  "quay.io/biocontainers/ecopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ecopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ecopy/container.yaml"
updated_at: "2023-11-09 02:32:19.496511"
latest: "0.1.2.2--py35h470a237_1"
container_url: "https://biocontainers.pro/tools/ecopy"

versions:
 - "0.1.2.2--py35h470a237_1"
description: "shpc-registry automated BioContainers addition for ecopy"
config: {"url": "https://biocontainers.pro/tools/ecopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ecopy", "latest": {"0.1.2.2--py35h470a237_1": "sha256:5cef6e66abafa61e09fbe3590259050d1cdd27fc7d7e6fa310fb5f5528e76d65"}, "tags": {"0.1.2.2--py35h470a237_1": "sha256:5cef6e66abafa61e09fbe3590259050d1cdd27fc7d7e6fa310fb5f5528e76d65"}, "docker": "quay.io/biocontainers/ecopy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ecopy.
shpc-registry automated BioContainers addition for ecopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ecopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ecopy:0.1.2.2--py35h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ecopy/0.1.2.2--py35h470a237_1
$ module help quay.io/biocontainers/ecopy/0.1.2.2--py35h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ecopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ecopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ecopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ecopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ecopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ecopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ecopy

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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