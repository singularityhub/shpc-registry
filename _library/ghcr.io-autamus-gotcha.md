---
layout: container
name:  "ghcr.io/autamus/gotcha"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gotcha/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/gotcha/container.yaml"
updated_at: "2025-06-07 03:15:56.645470"
latest: "1.0.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/gotcha"

versions:
 - "1.0.3"
 - "latest"
description: "C software library for shared library function wrapping, enables tools to intercept calls into shared libraries"
config: {"docker": "ghcr.io/autamus/gotcha", "url": "https://github.com/orgs/autamus/packages/container/package/gotcha", "maintainer": "@vsoch", "description": "C software library for shared library function wrapping, enables tools to intercept calls into shared libraries", "latest": {"1.0.3": "sha256:931a3e1dfd0bef321dda3bb8157cfff6d6cb2d6a579eb2c3d9df6b971dbc6423"}, "tags": {"1.0.3": "sha256:931a3e1dfd0bef321dda3bb8157cfff6d6cb2d6a579eb2c3d9df6b971dbc6423", "latest": "sha256:931a3e1dfd0bef321dda3bb8157cfff6d6cb2d6a579eb2c3d9df6b971dbc6423"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gotcha.
C software library for shared library function wrapping, enables tools to intercept calls into shared libraries
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gotcha
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gotcha:1.0.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gotcha/1.0.3
$ module help ghcr.io/autamus/gotcha/1.0.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gotcha-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gotcha-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gotcha-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gotcha-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gotcha-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gotcha-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gotcha

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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