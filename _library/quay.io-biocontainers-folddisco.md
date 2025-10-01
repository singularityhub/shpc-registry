---
layout: container
name:  "quay.io/biocontainers/folddisco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/folddisco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/folddisco/container.yaml"
updated_at: "2025-10-01 03:55:53.853028"
latest: "1.7514114--ha6fb395_1"
container_url: "https://biocontainers.pro/tools/folddisco"
aliases:
 - "folddisco"
versions:
 - "1.7514114--ha6fb395_1"
description: "singularity registry hpc automated addition for folddisco"
config: {"url": "https://biocontainers.pro/tools/folddisco", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for folddisco", "latest": {"1.7514114--ha6fb395_1": "sha256:aea72513f1a7f41352951cd05237f1edff72a48676780ab3e83b17e1bb5e87f5"}, "tags": {"1.7514114--ha6fb395_1": "sha256:aea72513f1a7f41352951cd05237f1edff72a48676780ab3e83b17e1bb5e87f5"}, "docker": "quay.io/biocontainers/folddisco", "aliases": {"folddisco": "/usr/local/bin/folddisco"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/folddisco.
singularity registry hpc automated addition for folddisco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/folddisco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/folddisco:1.7514114--ha6fb395_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/folddisco/1.7514114--ha6fb395_1
$ module help quay.io/biocontainers/folddisco/1.7514114--ha6fb395_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### folddisco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### folddisco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### folddisco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### folddisco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### folddisco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### folddisco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### folddisco

```bash
$ singularity exec <container> /usr/local/bin/folddisco
$ podman run --it --rm --entrypoint /usr/local/bin/folddisco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/folddisco   -v ${PWD} -w ${PWD} <container> -c " $@"
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