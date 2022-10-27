---
layout: container
name:  "quay.io/biocontainers/tracy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tracy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tracy/container.yaml"
updated_at: "2022-10-27 01:13:16.423531"
latest: "0.7.2--ha41ced6_1"
container_url: "https://biocontainers.pro/tools/tracy"
aliases:
 - "tracy"
versions:
 - "0.7.2--ha41ced6_1"
description: "shpc-registry automated BioContainers addition for tracy"
config: {"url": "https://biocontainers.pro/tools/tracy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tracy", "latest": {"0.7.2--ha41ced6_1": "sha256:4f4dccdf37ed2df042da3430f7dbb498e297b729639677664b1edd35bf3f1397"}, "tags": {"0.7.2--ha41ced6_1": "sha256:4f4dccdf37ed2df042da3430f7dbb498e297b729639677664b1edd35bf3f1397"}, "docker": "quay.io/biocontainers/tracy", "aliases": {"tracy": "/usr/local/bin/tracy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tracy.
shpc-registry automated BioContainers addition for tracy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tracy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tracy:0.7.2--ha41ced6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tracy/0.7.2--ha41ced6_1
$ module help quay.io/biocontainers/tracy/0.7.2--ha41ced6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tracy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tracy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tracy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tracy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tracy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tracy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tracy

```bash
$ singularity exec <container> /usr/local/bin/tracy
$ podman run --it --rm --entrypoint /usr/local/bin/tracy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tracy   -v ${PWD} -w ${PWD} <container> -c " $@"
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