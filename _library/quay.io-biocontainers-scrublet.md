---
layout: container
name:  "quay.io/biocontainers/scrublet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scrublet/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scrublet/container.yaml"
updated_at: "2022-10-27 01:05:48.563429"
latest: "0.2.3--pyh5e36f6f_1"
container_url: "https://biocontainers.pro/tools/scrublet"

versions:
 - "0.2.3--pyh5e36f6f_1"
description: "shpc-registry automated BioContainers addition for scrublet"
config: {"url": "https://biocontainers.pro/tools/scrublet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scrublet", "latest": {"0.2.3--pyh5e36f6f_1": "sha256:2a4a79a2c72725db6560f3c9c823fd1128dd81b811816405cb3b752f83fe3421"}, "tags": {"0.2.3--pyh5e36f6f_1": "sha256:2a4a79a2c72725db6560f3c9c823fd1128dd81b811816405cb3b752f83fe3421"}, "docker": "quay.io/biocontainers/scrublet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/scrublet.
shpc-registry automated BioContainers addition for scrublet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scrublet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scrublet:0.2.3--pyh5e36f6f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scrublet/0.2.3--pyh5e36f6f_1
$ module help quay.io/biocontainers/scrublet/0.2.3--pyh5e36f6f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scrublet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scrublet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scrublet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scrublet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scrublet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scrublet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### scrublet

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