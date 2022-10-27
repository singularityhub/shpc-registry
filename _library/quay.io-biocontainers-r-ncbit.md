---
layout: container
name:  "quay.io/biocontainers/r-ncbit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ncbit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-ncbit/container.yaml"
updated_at: "2022-10-27 00:30:42.679341"
latest: "2013.03.29--r40h6115d3f_3"
container_url: "https://biocontainers.pro/tools/r-ncbit"

versions:
 - "2013.03.29--r40h6115d3f_3"
description: "shpc-registry automated BioContainers addition for r-ncbit"
config: {"url": "https://biocontainers.pro/tools/r-ncbit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ncbit", "latest": {"2013.03.29--r40h6115d3f_3": "sha256:10cba53d6ad15af8f7eaa246c32c7b4a4e0227671a7b020665d3e38591c065df"}, "tags": {"2013.03.29--r40h6115d3f_3": "sha256:10cba53d6ad15af8f7eaa246c32c7b4a4e0227671a7b020665d3e38591c065df"}, "docker": "quay.io/biocontainers/r-ncbit"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ncbit.
shpc-registry automated BioContainers addition for r-ncbit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ncbit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ncbit:2013.03.29--r40h6115d3f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ncbit/2013.03.29--r40h6115d3f_3
$ module help quay.io/biocontainers/r-ncbit/2013.03.29--r40h6115d3f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ncbit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ncbit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ncbit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ncbit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ncbit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ncbit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-ncbit

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