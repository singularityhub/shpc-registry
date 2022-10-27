---
layout: container
name:  "quay.io/biocontainers/uritemplate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uritemplate/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/uritemplate/container.yaml"
updated_at: "2022-10-27 00:37:41.059842"
latest: "0.6--py36_0"
container_url: "https://biocontainers.pro/tools/uritemplate"

versions:
 - "0.6--py36_0"
description: "shpc-registry automated BioContainers addition for uritemplate"
config: {"url": "https://biocontainers.pro/tools/uritemplate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for uritemplate", "latest": {"0.6--py36_0": "sha256:c95df5d3859ada96708b1523d1adb9053ca02a23fe58f3106417bb17d0e724a6"}, "tags": {"0.6--py36_0": "sha256:c95df5d3859ada96708b1523d1adb9053ca02a23fe58f3106417bb17d0e724a6"}, "docker": "quay.io/biocontainers/uritemplate"}
---

This module is a singularity container wrapper for quay.io/biocontainers/uritemplate.
shpc-registry automated BioContainers addition for uritemplate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uritemplate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uritemplate:0.6--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uritemplate/0.6--py36_0
$ module help quay.io/biocontainers/uritemplate/0.6--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uritemplate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uritemplate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uritemplate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uritemplate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uritemplate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uritemplate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### uritemplate

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