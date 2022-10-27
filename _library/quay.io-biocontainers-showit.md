---
layout: container
name:  "quay.io/biocontainers/showit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/showit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/showit/container.yaml"
updated_at: "2022-10-27 00:22:53.998223"
latest: "1.1.4--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/showit"

versions:
 - "1.1.4--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for showit"
config: {"url": "https://biocontainers.pro/tools/showit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for showit", "latest": {"1.1.4--pyh864c0ab_1": "sha256:851d60cc62fb5eed690233b676ba217db6281ca3ee5f899e3a80b7297bed9344"}, "tags": {"1.1.4--pyh864c0ab_1": "sha256:851d60cc62fb5eed690233b676ba217db6281ca3ee5f899e3a80b7297bed9344"}, "docker": "quay.io/biocontainers/showit"}
---

This module is a singularity container wrapper for quay.io/biocontainers/showit.
shpc-registry automated BioContainers addition for showit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/showit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/showit:1.1.4--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/showit/1.1.4--pyh864c0ab_1
$ module help quay.io/biocontainers/showit/1.1.4--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### showit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### showit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### showit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### showit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### showit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### showit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### showit

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