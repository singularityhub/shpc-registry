---
layout: container
name:  "quay.io/biocontainers/muscle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/muscle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/muscle/container.yaml"
updated_at: "2025-01-30 03:15:07.288780"
latest: "5.3--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/muscle"
aliases:
 - "muscle"
versions:
 - "5.1--h9f5acd7_1"
 - "5.1--h9f5acd7_2"
 - "5.1--h4ac6f70_3"
 - "5.3--h4ac6f70_0"
 - "5.2--h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for muscle"
config: {"url": "https://biocontainers.pro/tools/muscle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for muscle", "latest": {"5.3--h4ac6f70_0": "sha256:516e1137f2067651d8cd748c369b8ac255864675040c2120d261ef6cf0d68bbd"}, "tags": {"5.1--h9f5acd7_1": "sha256:f8875d3ab2357f8909ed6df60df1adfe9ce9ab03d3660412e2b7d88bed347a69", "5.1--h9f5acd7_2": "sha256:5145c135276cb6178bdaccec0556b087533f04b44b4d5583d1ac442b3aeb0a68", "5.1--h4ac6f70_3": "sha256:3c1d2f181e13a36880ba757609b7672abc2f3ea09be237cee2510e22c6a60992", "5.3--h4ac6f70_0": "sha256:516e1137f2067651d8cd748c369b8ac255864675040c2120d261ef6cf0d68bbd", "5.2--h4ac6f70_0": "sha256:bb11a1b7a62ff880ff512090ca5147069048207fe0eda92838e3f68aa95a06c8"}, "docker": "quay.io/biocontainers/muscle", "aliases": {"muscle": "/usr/local/bin/muscle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/muscle.
shpc-registry automated BioContainers addition for muscle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/muscle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/muscle:5.3--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/muscle/5.3--h4ac6f70_0
$ module help quay.io/biocontainers/muscle/5.3--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### muscle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### muscle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### muscle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### muscle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### muscle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### muscle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
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