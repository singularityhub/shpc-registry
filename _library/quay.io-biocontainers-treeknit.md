---
layout: container
name:  "quay.io/biocontainers/treeknit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treeknit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treeknit/container.yaml"
updated_at: "2026-10-29 08:11:03.626086"
latest: "1.0.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/treeknit"
aliases:
 - "treeknit"
versions:
 - "1.0.0--h9ee0642_0"
description: "singularity registry hpc automated addition for treeknit"
config: {"url": "https://biocontainers.pro/tools/treeknit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for treeknit", "latest": {"1.0.0--h9ee0642_0": "sha256:e7fa0e48b945643207fa063cc8cc8680b1c0338e3ac2ce8489db63304cc62328"}, "tags": {"1.0.0--h9ee0642_0": "sha256:e7fa0e48b945643207fa063cc8cc8680b1c0338e3ac2ce8489db63304cc62328"}, "docker": "quay.io/biocontainers/treeknit", "aliases": {"treeknit": "/usr/local/bin/treeknit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treeknit.
singularity registry hpc automated addition for treeknit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treeknit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treeknit:1.0.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treeknit/1.0.0--h9ee0642_0
$ module help quay.io/biocontainers/treeknit/1.0.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treeknit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treeknit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treeknit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treeknit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treeknit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treeknit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### treeknit

```bash
$ singularity exec <container> /usr/local/bin/treeknit
$ podman run --it --rm --entrypoint /usr/local/bin/treeknit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeknit   -v ${PWD} -w ${PWD} <container> -c " $@"
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