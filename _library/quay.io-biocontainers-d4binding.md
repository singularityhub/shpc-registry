---
layout: container
name:  "quay.io/biocontainers/d4binding"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/d4binding/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/d4binding/container.yaml"
updated_at: "2024-09-11 03:28:14.188365"
latest: "0.3.4--h87f3376_0"
container_url: "https://biocontainers.pro/tools/d4binding"
aliases:
 - "starcode"
versions:
 - "0.3.4--h87f3376_0"
description: "singularity registry hpc automated addition for d4binding"
config: {"url": "https://biocontainers.pro/tools/d4binding", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for d4binding", "latest": {"0.3.4--h87f3376_0": "sha256:5f55a16b97075b91f86c54ff4dd7fe11324af217880775ab1ee53433517657bb"}, "tags": {"0.3.4--h87f3376_0": "sha256:5f55a16b97075b91f86c54ff4dd7fe11324af217880775ab1ee53433517657bb"}, "docker": "quay.io/biocontainers/d4binding", "aliases": {"starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/d4binding.
singularity registry hpc automated addition for d4binding
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/d4binding
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/d4binding:0.3.4--h87f3376_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/d4binding/0.3.4--h87f3376_0
$ module help quay.io/biocontainers/d4binding/0.3.4--h87f3376_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### d4binding-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### d4binding-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### d4binding-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### d4binding-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### d4binding-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### d4binding-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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