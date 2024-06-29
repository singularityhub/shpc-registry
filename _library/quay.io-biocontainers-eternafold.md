---
layout: container
name:  "quay.io/biocontainers/eternafold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eternafold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eternafold/container.yaml"
updated_at: "2024-06-29 03:06:01.235126"
latest: "1.3.1--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/eternafold"
aliases:
 - "eternafold"
versions:
 - "1.3.1--h4ac6f70_0"
description: "singularity registry hpc automated addition for eternafold"
config: {"url": "https://biocontainers.pro/tools/eternafold", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for eternafold", "latest": {"1.3.1--h4ac6f70_0": "sha256:06d7af0fc874d33e3a927696edbe080678afb09f944dbd152ecd34fd4cec84e4"}, "tags": {"1.3.1--h4ac6f70_0": "sha256:06d7af0fc874d33e3a927696edbe080678afb09f944dbd152ecd34fd4cec84e4"}, "docker": "quay.io/biocontainers/eternafold", "aliases": {"eternafold": "/usr/local/bin/eternafold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eternafold.
singularity registry hpc automated addition for eternafold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eternafold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eternafold:1.3.1--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eternafold/1.3.1--h4ac6f70_0
$ module help quay.io/biocontainers/eternafold/1.3.1--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eternafold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eternafold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eternafold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eternafold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eternafold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eternafold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eternafold

```bash
$ singularity exec <container> /usr/local/bin/eternafold
$ podman run --it --rm --entrypoint /usr/local/bin/eternafold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eternafold   -v ${PWD} -w ${PWD} <container> -c " $@"
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