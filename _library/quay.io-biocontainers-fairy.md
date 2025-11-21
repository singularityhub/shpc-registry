---
layout: container
name:  "quay.io/biocontainers/fairy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fairy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fairy/container.yaml"
updated_at: "2025-11-21 16:17:38.581662"
latest: "0.5.8--hc1c3326_0"
container_url: "https://biocontainers.pro/tools/fairy"
aliases:
 - "fairy"
versions:
 - "0.5.3--h4ac6f70_0"
 - "0.5.4--h4ac6f70_0"
 - "0.5.5--h4ac6f70_0"
 - "0.5.7--h4ac6f70_0"
 - "0.5.7--ha6fb395_2"
 - "0.5.8--hc1c3326_0"
description: "singularity registry hpc automated addition for fairy"
config: {"url": "https://biocontainers.pro/tools/fairy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fairy", "latest": {"0.5.8--hc1c3326_0": "sha256:c2ccf6001960b926712eb9f343fd40bd99ee0eab4696bdb4b471de5003e75bb7"}, "tags": {"0.5.3--h4ac6f70_0": "sha256:a03cae5fdd092ec682ab7b36792379be4b45ca2067c0ce1c92c96e24ac12c44f", "0.5.4--h4ac6f70_0": "sha256:45fc91c2dd6bb21ab17464a718f9f497c8231a51c4916b9a67e3ced46f8c726c", "0.5.5--h4ac6f70_0": "sha256:52693e539afb23cd584aae7213dad6bbea53b50d8da912e53f9e90a0779c4d31", "0.5.7--h4ac6f70_0": "sha256:2be5cebffb762904254fab1222ead11b748b90fb8a7bb9223d24a2d27956755d", "0.5.7--ha6fb395_2": "sha256:9d8f2a1374aa1b75fe51c3d7b1ef3a95a079486e8bb6ff3e53e3461de2a65829", "0.5.8--hc1c3326_0": "sha256:c2ccf6001960b926712eb9f343fd40bd99ee0eab4696bdb4b471de5003e75bb7"}, "docker": "quay.io/biocontainers/fairy", "aliases": {"fairy": "/usr/local/bin/fairy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fairy.
singularity registry hpc automated addition for fairy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fairy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fairy:0.5.8--hc1c3326_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fairy/0.5.8--hc1c3326_0
$ module help quay.io/biocontainers/fairy/0.5.8--hc1c3326_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fairy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fairy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fairy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fairy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fairy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fairy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fairy

```bash
$ singularity exec <container> /usr/local/bin/fairy
$ podman run --it --rm --entrypoint /usr/local/bin/fairy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairy   -v ${PWD} -w ${PWD} <container> -c " $@"
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