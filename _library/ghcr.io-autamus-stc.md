---
layout: container
name:  "ghcr.io/autamus/stc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/stc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/stc/container.yaml"
updated_at: "2025-01-07 02:52:33.039360"
latest: "0.9.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/stc"
aliases:
 - "stc"
 - "swift-t"
versions:
 - "0.9.0"
 - "latest"
description: "The Swift-Turbine Compiler (STC)"
config: {"docker": "ghcr.io/autamus/stc", "url": "https://github.com/orgs/autamus/packages/container/package/stc", "maintainer": "@vsoch", "description": "The Swift-Turbine Compiler (STC)", "latest": {"0.9.0": "sha256:5f74444f5537365f9f9984c3e69dc0157bebca1b322c5ebfc6f3ad55749434e4"}, "tags": {"0.9.0": "sha256:5f74444f5537365f9f9984c3e69dc0157bebca1b322c5ebfc6f3ad55749434e4", "latest": "sha256:5f74444f5537365f9f9984c3e69dc0157bebca1b322c5ebfc6f3ad55749434e4"}, "aliases": {"stc": "/opt/view/bin/stc", "swift-t": "/opt/view/bin/swift-t"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/stc.
The Swift-Turbine Compiler (STC)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/stc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/stc:0.9.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/stc/0.9.0
$ module help ghcr.io/autamus/stc/0.9.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stc

```bash
$ singularity exec <container> /opt/view/bin/stc
$ podman run --it --rm --entrypoint /opt/view/bin/stc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/stc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swift-t

```bash
$ singularity exec <container> /opt/view/bin/swift-t
$ podman run --it --rm --entrypoint /opt/view/bin/swift-t   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/swift-t   -v ${PWD} -w ${PWD} <container> -c " $@"
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