---
layout: container
name:  "quay.io/biocontainers/ensemblcov"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ensemblcov/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ensemblcov/container.yaml"
updated_at: "2026-01-26 05:01:46.424001"
latest: "0.1.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/ensemblcov"
aliases:
 - "ensemblcov"
versions:
 - "0.1.0--h4349ce8_0"
description: "singularity registry hpc automated addition for ensemblcov"
config: {"url": "https://biocontainers.pro/tools/ensemblcov", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ensemblcov", "latest": {"0.1.0--h4349ce8_0": "sha256:12a05da63a83cf9bab2c9a7dd9651cc8831ab0f1124fb9e0ab51d48dd30ecefd"}, "tags": {"0.1.0--h4349ce8_0": "sha256:12a05da63a83cf9bab2c9a7dd9651cc8831ab0f1124fb9e0ab51d48dd30ecefd"}, "docker": "quay.io/biocontainers/ensemblcov", "aliases": {"ensemblcov": "/usr/local/bin/ensemblcov"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ensemblcov.
singularity registry hpc automated addition for ensemblcov
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ensemblcov
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ensemblcov:0.1.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ensemblcov/0.1.0--h4349ce8_0
$ module help quay.io/biocontainers/ensemblcov/0.1.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ensemblcov-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ensemblcov-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ensemblcov-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ensemblcov-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ensemblcov-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ensemblcov-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ensemblcov

```bash
$ singularity exec <container> /usr/local/bin/ensemblcov
$ podman run --it --rm --entrypoint /usr/local/bin/ensemblcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ensemblcov   -v ${PWD} -w ${PWD} <container> -c " $@"
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