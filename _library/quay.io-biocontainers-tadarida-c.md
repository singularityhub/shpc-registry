---
layout: container
name:  "quay.io/biocontainers/tadarida-c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tadarida-c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tadarida-c/container.yaml"
updated_at: "2025-11-02 03:58:38.029583"
latest: "1.2--r351_1"
container_url: "https://biocontainers.pro/tools/tadarida-c"
aliases:
 - "tadaridaC.r"
versions:
 - "1.2--r351_1"
description: "shpc-registry automated BioContainers addition for tadarida-c"
config: {"url": "https://biocontainers.pro/tools/tadarida-c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tadarida-c", "latest": {"1.2--r351_1": "sha256:c42931f045b99a4e912adb48b0392425535737a488e6dc324041db70311dc329"}, "tags": {"1.2--r351_1": "sha256:c42931f045b99a4e912adb48b0392425535737a488e6dc324041db70311dc329"}, "docker": "quay.io/biocontainers/tadarida-c", "aliases": {"tadaridaC.r": "/usr/local/bin/tadaridaC.r"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tadarida-c.
shpc-registry automated BioContainers addition for tadarida-c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tadarida-c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tadarida-c:1.2--r351_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tadarida-c/1.2--r351_1
$ module help quay.io/biocontainers/tadarida-c/1.2--r351_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tadarida-c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tadarida-c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tadarida-c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tadarida-c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tadarida-c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tadarida-c-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tadaridaC.r

```bash
$ singularity exec <container> /usr/local/bin/tadaridaC.r
$ podman run --it --rm --entrypoint /usr/local/bin/tadaridaC.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tadaridaC.r   -v ${PWD} -w ${PWD} <container> -c " $@"
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