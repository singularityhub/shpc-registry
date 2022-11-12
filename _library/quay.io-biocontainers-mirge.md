---
layout: container
name:  "quay.io/biocontainers/mirge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mirge/container.yaml"
updated_at: "2022-11-12 00:47:44.038319"
latest: "2.0.6--pyh5ca1d4c_6"
container_url: "https://biocontainers.pro/tools/mirge"

versions:
 - "2.0.6--pyh5ca1d4c_6"
description: "shpc-registry automated BioContainers addition for mirge"
config: {"url": "https://biocontainers.pro/tools/mirge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirge", "latest": {"2.0.6--pyh5ca1d4c_6": "sha256:92a9ecdf2ab946d0288dc1771c60ce62a8879001e76b604c8ab5a3fcbd9a6326"}, "tags": {"2.0.6--pyh5ca1d4c_6": "sha256:92a9ecdf2ab946d0288dc1771c60ce62a8879001e76b604c8ab5a3fcbd9a6326"}, "docker": "quay.io/biocontainers/mirge"}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirge.
shpc-registry automated BioContainers addition for mirge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirge:2.0.6--pyh5ca1d4c_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirge/2.0.6--pyh5ca1d4c_6
$ module help quay.io/biocontainers/mirge/2.0.6--pyh5ca1d4c_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mirge

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