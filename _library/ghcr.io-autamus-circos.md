---
layout: container
name:  "ghcr.io/autamus/circos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/circos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/circos/container.yaml"
updated_at: "2024-08-15 03:27:54.754325"
latest: "0.69.6"
container_url: "https://github.com/orgs/autamus/packages/container/package/circos"
aliases:
 - "circos"
versions:
 - "0.69.6"
 - "latest"
description: "Circos is a software package for visualizing data and information."
config: {"docker": "ghcr.io/autamus/circos", "url": "https://github.com/orgs/autamus/packages/container/package/circos", "maintainer": "@vsoch", "description": "Circos is a software package for visualizing data and information.", "latest": {"0.69.6": "sha256:e5513d32d93522d2c7a86f45fe0fdd23bea53ed0bfebfe4e3fcdbde5a03608fa"}, "tags": {"0.69.6": "sha256:e5513d32d93522d2c7a86f45fe0fdd23bea53ed0bfebfe4e3fcdbde5a03608fa", "latest": "sha256:e5513d32d93522d2c7a86f45fe0fdd23bea53ed0bfebfe4e3fcdbde5a03608fa"}, "aliases": {"circos": "/opt/view/bin/circos"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/circos.
Circos is a software package for visualizing data and information.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/circos
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/circos:0.69.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/circos/0.69.6
$ module help ghcr.io/autamus/circos/0.69.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### circos

```bash
$ singularity exec <container> /opt/view/bin/circos
$ podman run --it --rm --entrypoint /opt/view/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
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