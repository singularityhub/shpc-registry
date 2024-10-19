---
layout: container
name:  "quay.io/biocontainers/abundancebin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abundancebin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abundancebin/container.yaml"
updated_at: "2024-10-19 02:52:30.305749"
latest: "1.0.1--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/abundancebin"
aliases:
 - "abundancebin"
versions:
 - "1.0.1--h9f5acd7_4"
 - "1.0.1--h9f5acd7_5"
 - "1.0.1--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for abundancebin"
config: {"url": "https://biocontainers.pro/tools/abundancebin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abundancebin", "latest": {"1.0.1--h4ac6f70_6": "sha256:8bda624b6531d074a4ae6dbdf9352f888e5079dfecf3a5fe32a4af4f3c067ae7"}, "tags": {"1.0.1--h9f5acd7_4": "sha256:e76410ccbe886ff5c22e61568f392b8bcbd4f7afc05afd2b82dca10ce3569623", "1.0.1--h9f5acd7_5": "sha256:df5f713e91203566a88789a7ea9a600d92c57c6e9224a6753e02f1014ff7d231", "1.0.1--h4ac6f70_6": "sha256:8bda624b6531d074a4ae6dbdf9352f888e5079dfecf3a5fe32a4af4f3c067ae7"}, "docker": "quay.io/biocontainers/abundancebin", "aliases": {"abundancebin": "/usr/local/bin/abundancebin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abundancebin.
shpc-registry automated BioContainers addition for abundancebin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abundancebin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abundancebin:1.0.1--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abundancebin/1.0.1--h4ac6f70_6
$ module help quay.io/biocontainers/abundancebin/1.0.1--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abundancebin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abundancebin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abundancebin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abundancebin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abundancebin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abundancebin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abundancebin

```bash
$ singularity exec <container> /usr/local/bin/abundancebin
$ podman run --it --rm --entrypoint /usr/local/bin/abundancebin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abundancebin   -v ${PWD} -w ${PWD} <container> -c " $@"
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