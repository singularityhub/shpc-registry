---
layout: container
name:  "quay.io/biocontainers/picrust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/picrust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/picrust/container.yaml"
updated_at: "2023-12-20 02:57:26.190575"
latest: "1.1.4--pyh5ca1d4c_1"
container_url: "https://biocontainers.pro/tools/picrust"

versions:
 - "1.1.4--pyh5ca1d4c_1"
description: "shpc-registry automated BioContainers addition for picrust"
config: {"url": "https://biocontainers.pro/tools/picrust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for picrust", "latest": {"1.1.4--pyh5ca1d4c_1": "sha256:1ea5a82f6ef6a3d194d86310cbe884c4b57abaa200af4c11d306684d911cc9fa"}, "tags": {"1.1.4--pyh5ca1d4c_1": "sha256:1ea5a82f6ef6a3d194d86310cbe884c4b57abaa200af4c11d306684d911cc9fa"}, "docker": "quay.io/biocontainers/picrust"}
---

This module is a singularity container wrapper for quay.io/biocontainers/picrust.
shpc-registry automated BioContainers addition for picrust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/picrust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/picrust:1.1.4--pyh5ca1d4c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/picrust/1.1.4--pyh5ca1d4c_1
$ module help quay.io/biocontainers/picrust/1.1.4--pyh5ca1d4c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### picrust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### picrust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### picrust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### picrust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### picrust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### picrust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### picrust

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