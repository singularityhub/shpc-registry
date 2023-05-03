---
layout: container
name:  "quay.io/biocontainers/xtensor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xtensor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xtensor/container.yaml"
updated_at: "2023-05-03 02:54:07.098469"
latest: "0.19.1"
container_url: "https://biocontainers.pro/tools/xtensor"

versions:
 - "0.19.1"
description: "shpc-registry automated BioContainers addition for xtensor"
config: {"url": "https://biocontainers.pro/tools/xtensor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xtensor", "latest": {"0.19.1": "sha256:7627945cdba1801aa258cf4d19fda8cb600c8df93360612d469d2bffe005c6c3"}, "tags": {"0.19.1": "sha256:7627945cdba1801aa258cf4d19fda8cb600c8df93360612d469d2bffe005c6c3"}, "docker": "quay.io/biocontainers/xtensor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/xtensor.
shpc-registry automated BioContainers addition for xtensor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xtensor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xtensor:0.19.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xtensor/0.19.1
$ module help quay.io/biocontainers/xtensor/0.19.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xtensor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xtensor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xtensor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xtensor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xtensor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xtensor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### xtensor

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