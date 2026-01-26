---
layout: container
name:  "quay.io/biocontainers/covar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/covar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/covar/container.yaml"
updated_at: "2026-01-26 04:58:44.136957"
latest: "0.3.0--h3dc2dae_0"
container_url: "https://biocontainers.pro/tools/covar"
aliases:
 - "covar"
versions:
 - "0.2.0--h3dc2dae_1"
 - "0.3.0--h3dc2dae_0"
description: "singularity registry hpc automated addition for covar"
config: {"url": "https://biocontainers.pro/tools/covar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for covar", "latest": {"0.3.0--h3dc2dae_0": "sha256:a01f396dac3d5248353ea58ca7da7c7ceb4ce2816fc92ea59f39706e03b1bf8b"}, "tags": {"0.2.0--h3dc2dae_1": "sha256:e3ef45c91617372eb882ec4fcd20950b912149f71f7939e2f9e77d6337ce8d95", "0.3.0--h3dc2dae_0": "sha256:a01f396dac3d5248353ea58ca7da7c7ceb4ce2816fc92ea59f39706e03b1bf8b"}, "docker": "quay.io/biocontainers/covar", "aliases": {"covar": "/usr/local/bin/covar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/covar.
singularity registry hpc automated addition for covar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/covar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/covar:0.3.0--h3dc2dae_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/covar/0.3.0--h3dc2dae_0
$ module help quay.io/biocontainers/covar/0.3.0--h3dc2dae_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### covar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### covar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### covar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### covar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### covar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### covar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### covar

```bash
$ singularity exec <container> /usr/local/bin/covar
$ podman run --it --rm --entrypoint /usr/local/bin/covar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covar   -v ${PWD} -w ${PWD} <container> -c " $@"
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