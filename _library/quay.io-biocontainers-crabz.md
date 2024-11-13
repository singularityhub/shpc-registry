---
layout: container
name:  "quay.io/biocontainers/crabz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crabz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crabz/container.yaml"
updated_at: "2024-11-13 02:55:03.084468"
latest: "0.9.0"
container_url: "https://biocontainers.pro/tools/crabz"
aliases:
 - "crabz"
versions:
 - "0.9.0"
description: "singularity registry hpc automated addition for crabz"
config: {"url": "https://biocontainers.pro/tools/crabz", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for crabz", "latest": {"0.9.0": "sha256:1b65229b4ecf4425cb67d91cb49dcfa695aa51d812078d28164dbcefcb9adafd"}, "tags": {"0.9.0": "sha256:1b65229b4ecf4425cb67d91cb49dcfa695aa51d812078d28164dbcefcb9adafd"}, "docker": "quay.io/biocontainers/crabz", "aliases": {"crabz": "/usr/local/bin/crabz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crabz.
singularity registry hpc automated addition for crabz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crabz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crabz:0.9.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crabz/0.9.0
$ module help quay.io/biocontainers/crabz/0.9.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crabz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crabz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crabz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crabz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crabz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crabz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crabz

```bash
$ singularity exec <container> /usr/local/bin/crabz
$ podman run --it --rm --entrypoint /usr/local/bin/crabz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crabz   -v ${PWD} -w ${PWD} <container> -c " $@"
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