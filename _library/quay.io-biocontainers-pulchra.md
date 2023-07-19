---
layout: container
name:  "quay.io/biocontainers/pulchra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pulchra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pulchra/container.yaml"
updated_at: "2023-07-19 04:10:22.175838"
latest: "3.06--h031d066_4"
container_url: "https://biocontainers.pro/tools/pulchra"
aliases:
 - "pulchra"
versions:
 - "3.06--hec16e2b_2"
 - "3.06--h031d066_4"
description: "shpc-registry automated BioContainers addition for pulchra"
config: {"url": "https://biocontainers.pro/tools/pulchra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pulchra", "latest": {"3.06--h031d066_4": "sha256:ee90cccfd03022181f2b8ce35eff63d7e112fa53edbcdd09b6388a77cb4af21b"}, "tags": {"3.06--hec16e2b_2": "sha256:9b68b17228447aafa87caa2a78a841179b5563180970eb9a9e621dc6ae644c4d", "3.06--h031d066_4": "sha256:ee90cccfd03022181f2b8ce35eff63d7e112fa53edbcdd09b6388a77cb4af21b"}, "docker": "quay.io/biocontainers/pulchra", "aliases": {"pulchra": "/usr/local/bin/pulchra"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pulchra.
shpc-registry automated BioContainers addition for pulchra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pulchra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pulchra:3.06--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pulchra/3.06--h031d066_4
$ module help quay.io/biocontainers/pulchra/3.06--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pulchra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pulchra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pulchra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pulchra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pulchra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pulchra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pulchra

```bash
$ singularity exec <container> /usr/local/bin/pulchra
$ podman run --it --rm --entrypoint /usr/local/bin/pulchra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulchra   -v ${PWD} -w ${PWD} <container> -c " $@"
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