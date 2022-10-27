---
layout: container
name:  "quay.io/biocontainers/r-prabclus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-prabclus/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-prabclus/container.yaml"
updated_at: "2022-10-27 01:12:44.685198"
latest: "2.2_6--r3.3.2_0"
container_url: "https://biocontainers.pro/tools/r-prabclus"

versions:
 - "2.2_6--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-prabclus"
config: {"url": "https://biocontainers.pro/tools/r-prabclus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-prabclus", "latest": {"2.2_6--r3.3.2_0": "sha256:f93e7b10d1cf4458d006daac387038cd17e7c525fef7bc2f5e6bde5c195c34ec"}, "tags": {"2.2_6--r3.3.2_0": "sha256:f93e7b10d1cf4458d006daac387038cd17e7c525fef7bc2f5e6bde5c195c34ec"}, "docker": "quay.io/biocontainers/r-prabclus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-prabclus.
shpc-registry automated BioContainers addition for r-prabclus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-prabclus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-prabclus:2.2_6--r3.3.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-prabclus/2.2_6--r3.3.2_0
$ module help quay.io/biocontainers/r-prabclus/2.2_6--r3.3.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-prabclus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-prabclus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-prabclus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-prabclus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-prabclus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-prabclus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-prabclus

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