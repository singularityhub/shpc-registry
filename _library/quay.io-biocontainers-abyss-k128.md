---
layout: container
name:  "quay.io/biocontainers/abyss-k128"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abyss-k128/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abyss-k128/container.yaml"
updated_at: "2023-12-29 02:52:48.181806"
latest: "2.0.2--boost1.64_2"
container_url: "https://biocontainers.pro/tools/abyss-k128"

versions:
 - "2.0.2--boost1.64_2"
description: "shpc-registry automated BioContainers addition for abyss-k128"
config: {"url": "https://biocontainers.pro/tools/abyss-k128", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abyss-k128", "latest": {"2.0.2--boost1.64_2": "sha256:d9f6fbc0d0bfb1a90839b84a440758fa6dd83e150672eb99b5cab945980b15ab"}, "tags": {"2.0.2--boost1.64_2": "sha256:d9f6fbc0d0bfb1a90839b84a440758fa6dd83e150672eb99b5cab945980b15ab"}, "docker": "quay.io/biocontainers/abyss-k128"}
---

This module is a singularity container wrapper for quay.io/biocontainers/abyss-k128.
shpc-registry automated BioContainers addition for abyss-k128
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abyss-k128
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abyss-k128:2.0.2--boost1.64_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abyss-k128/2.0.2--boost1.64_2
$ module help quay.io/biocontainers/abyss-k128/2.0.2--boost1.64_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abyss-k128-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abyss-k128-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abyss-k128-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abyss-k128-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abyss-k128-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abyss-k128-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### abyss-k128

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