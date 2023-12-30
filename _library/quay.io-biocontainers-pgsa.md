---
layout: container
name:  "quay.io/biocontainers/pgsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgsa/container.yaml"
updated_at: "2023-12-30 02:40:43.512521"
latest: "1.2--hdbdd923_6"
container_url: "https://biocontainers.pro/tools/pgsa"
aliases:
 - "PgSAgen"
 - "PgSAtest"
versions:
 - "1.2--h87f3376_4"
 - "1.2--h87f3376_5"
 - "1.2--hdbdd923_6"
description: "shpc-registry automated BioContainers addition for pgsa"
config: {"url": "https://biocontainers.pro/tools/pgsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pgsa", "latest": {"1.2--hdbdd923_6": "sha256:fe2673896604d0d1f5932641c64ae4776528d92c9ff8eebd3a673d4982cb9fc3"}, "tags": {"1.2--h87f3376_4": "sha256:bd43ae4be8f01c0dd6feeb50759f622b7fa0a3d3eb59967534b1fca70c392d7a", "1.2--h87f3376_5": "sha256:9586f778a9410ee7499b0321813df3171b7230c2986f69d88c287b6b32d66fa4", "1.2--hdbdd923_6": "sha256:fe2673896604d0d1f5932641c64ae4776528d92c9ff8eebd3a673d4982cb9fc3"}, "docker": "quay.io/biocontainers/pgsa", "aliases": {"PgSAgen": "/usr/local/bin/PgSAgen", "PgSAtest": "/usr/local/bin/PgSAtest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgsa.
shpc-registry automated BioContainers addition for pgsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgsa:1.2--hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgsa/1.2--hdbdd923_6
$ module help quay.io/biocontainers/pgsa/1.2--hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PgSAgen

```bash
$ singularity exec <container> /usr/local/bin/PgSAgen
$ podman run --it --rm --entrypoint /usr/local/bin/PgSAgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PgSAgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PgSAtest

```bash
$ singularity exec <container> /usr/local/bin/PgSAtest
$ podman run --it --rm --entrypoint /usr/local/bin/PgSAtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PgSAtest   -v ${PWD} -w ${PWD} <container> -c " $@"
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