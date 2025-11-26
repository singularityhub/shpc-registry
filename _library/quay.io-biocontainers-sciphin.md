---
layout: container
name:  "quay.io/biocontainers/sciphin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sciphin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sciphin/container.yaml"
updated_at: "2025-11-26 03:56:55.955024"
latest: "1.0.1--h077b44d_4"
container_url: "https://biocontainers.pro/tools/sciphin"
aliases:
 - "sciphin"
versions:
 - "1.0.1--h7ff8a90_1"
 - "1.0.1--h21ec9f0_2"
 - "1.0.1--hdcf5f25_3"
 - "1.0.1--h077b44d_4"
description: "singularity registry hpc automated addition for sciphin"
config: {"url": "https://biocontainers.pro/tools/sciphin", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sciphin", "latest": {"1.0.1--h077b44d_4": "sha256:abac69fee96d7f421d8fd37f11024aeea6f73ec73bcd3296555a00b4305ffee8"}, "tags": {"1.0.1--h7ff8a90_1": "sha256:c9586cd3ed93dd56927a4609a62101051a1f8adbf0e61632bfa39ae41df6b171", "1.0.1--h21ec9f0_2": "sha256:8b0b36726b3e384665600e5e5289be38bcf13abaefdad9f35847301f98ddb0f6", "1.0.1--hdcf5f25_3": "sha256:1c897d53eac4d95261f58b889a1a1f2ab5cd688e026e478c58a6300780fdf5e0", "1.0.1--h077b44d_4": "sha256:abac69fee96d7f421d8fd37f11024aeea6f73ec73bcd3296555a00b4305ffee8"}, "docker": "quay.io/biocontainers/sciphin", "aliases": {"sciphin": "/usr/local/bin/sciphin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sciphin.
singularity registry hpc automated addition for sciphin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sciphin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sciphin:1.0.1--h077b44d_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sciphin/1.0.1--h077b44d_4
$ module help quay.io/biocontainers/sciphin/1.0.1--h077b44d_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sciphin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sciphin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sciphin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sciphin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sciphin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sciphin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sciphin

```bash
$ singularity exec <container> /usr/local/bin/sciphin
$ podman run --it --rm --entrypoint /usr/local/bin/sciphin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sciphin   -v ${PWD} -w ${PWD} <container> -c " $@"
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