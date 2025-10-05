---
layout: container
name:  "quay.io/biocontainers/riboraptor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riboraptor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riboraptor/container.yaml"
updated_at: "2025-10-05 03:27:55.158899"
latest: "0.2.2--py_2"
container_url: "https://biocontainers.pro/tools/riboraptor"

versions:
 - "0.2.2--py_2"
description: "shpc-registry automated BioContainers addition for riboraptor"
config: {"url": "https://biocontainers.pro/tools/riboraptor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for riboraptor", "latest": {"0.2.2--py_2": "sha256:a510463e49f2b2973fbeaa02d086815e8b5d47db151211d7845f82c84cbb4e02"}, "tags": {"0.2.2--py_2": "sha256:a510463e49f2b2973fbeaa02d086815e8b5d47db151211d7845f82c84cbb4e02"}, "docker": "quay.io/biocontainers/riboraptor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/riboraptor.
shpc-registry automated BioContainers addition for riboraptor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riboraptor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riboraptor:0.2.2--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riboraptor/0.2.2--py_2
$ module help quay.io/biocontainers/riboraptor/0.2.2--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riboraptor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riboraptor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riboraptor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riboraptor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riboraptor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riboraptor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### riboraptor

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