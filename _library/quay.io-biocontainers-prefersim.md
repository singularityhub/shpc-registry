---
layout: container
name:  "quay.io/biocontainers/prefersim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prefersim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prefersim/container.yaml"
updated_at: "2024-06-27 02:51:10.264519"
latest: "1.0--h245ed52_6"
container_url: "https://biocontainers.pro/tools/prefersim"
aliases:
 - "PReFerSim"
versions:
 - "1.0--h940b034_4"
 - "1.0--h245ed52_6"
description: "shpc-registry automated BioContainers addition for prefersim"
config: {"url": "https://biocontainers.pro/tools/prefersim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prefersim", "latest": {"1.0--h245ed52_6": "sha256:6c0f9b1ec1cba6cf1a4f32199dbe2e80db72f14b77eef46063a9bfe54d27e6b3"}, "tags": {"1.0--h940b034_4": "sha256:19aa8bd10a372556f0ade847ebfbde520c6d5cfa7b3da13fa9fb9c3612a0660c", "1.0--h245ed52_6": "sha256:6c0f9b1ec1cba6cf1a4f32199dbe2e80db72f14b77eef46063a9bfe54d27e6b3"}, "docker": "quay.io/biocontainers/prefersim", "aliases": {"PReFerSim": "/usr/local/bin/PReFerSim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prefersim.
shpc-registry automated BioContainers addition for prefersim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prefersim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prefersim:1.0--h245ed52_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prefersim/1.0--h245ed52_6
$ module help quay.io/biocontainers/prefersim/1.0--h245ed52_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prefersim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prefersim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prefersim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prefersim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prefersim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prefersim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PReFerSim

```bash
$ singularity exec <container> /usr/local/bin/PReFerSim
$ podman run --it --rm --entrypoint /usr/local/bin/PReFerSim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PReFerSim   -v ${PWD} -w ${PWD} <container> -c " $@"
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