---
layout: container
name:  "quay.io/biocontainers/byobu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/byobu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/byobu/container.yaml"
updated_at: "2025-11-22 03:42:52.675158"
latest: "5.98--hb42da9c_2"
container_url: "https://biocontainers.pro/tools/byobu"

versions:
 - "5.98--hb42da9c_2"
description: "shpc-registry automated BioContainers addition for byobu"
config: {"url": "https://biocontainers.pro/tools/byobu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for byobu", "latest": {"5.98--hb42da9c_2": "sha256:7037203cac6bd78e0f080872e3573c1311f1c47086e7c6a0301330443bc84176"}, "tags": {"5.98--hb42da9c_2": "sha256:7037203cac6bd78e0f080872e3573c1311f1c47086e7c6a0301330443bc84176"}, "docker": "quay.io/biocontainers/byobu"}
---

This module is a singularity container wrapper for quay.io/biocontainers/byobu.
shpc-registry automated BioContainers addition for byobu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/byobu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/byobu:5.98--hb42da9c_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/byobu/5.98--hb42da9c_2
$ module help quay.io/biocontainers/byobu/5.98--hb42da9c_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### byobu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### byobu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### byobu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### byobu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### byobu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### byobu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### byobu

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