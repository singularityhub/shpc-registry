---
layout: container
name:  "quay.io/biocontainers/r-leapp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-leapp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-leapp/container.yaml"
updated_at: "2025-05-08 05:51:47.495399"
latest: "1.3--r44h3342da4_3"
container_url: "https://biocontainers.pro/tools/r-leapp"

versions:
 - "1.3--r41h3342da4_0"
 - "1.3--r42h3342da4_1"
 - "1.3--r43h3342da4_2"
 - "1.3--r44h3342da4_3"
description: "shpc-registry automated BioContainers addition for r-leapp"
config: {"url": "https://biocontainers.pro/tools/r-leapp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-leapp", "latest": {"1.3--r44h3342da4_3": "sha256:a8e5183dc0d871b7153279b436c8b1ad8d4fb14ef3e96c6f79dcfbe8ecfed8f7"}, "tags": {"1.3--r41h3342da4_0": "sha256:cb13e5e88d0814d675aa5f3b6a49fca3ebde7ab2070f63149a2f8c6d730d0049", "1.3--r42h3342da4_1": "sha256:01d5f98ace9392303ffe24b2aed72670ffd02450aa1aa0303f1ced7a631d7664", "1.3--r43h3342da4_2": "sha256:965c404f5052926263e4f202fa37c781713278ebecea393d4c6644b05adedd21", "1.3--r44h3342da4_3": "sha256:a8e5183dc0d871b7153279b436c8b1ad8d4fb14ef3e96c6f79dcfbe8ecfed8f7"}, "docker": "quay.io/biocontainers/r-leapp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-leapp.
shpc-registry automated BioContainers addition for r-leapp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-leapp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-leapp:1.3--r44h3342da4_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-leapp/1.3--r44h3342da4_3
$ module help quay.io/biocontainers/r-leapp/1.3--r44h3342da4_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-leapp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-leapp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-leapp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-leapp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-leapp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-leapp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-leapp

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