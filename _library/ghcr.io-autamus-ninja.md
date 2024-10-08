---
layout: container
name:  "ghcr.io/autamus/ninja"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ninja/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/ninja/container.yaml"
updated_at: "2024-10-08 03:42:19.857116"
latest: "1.11.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/ninja"
aliases:
 - "ninja"
 - "ninja-build"
versions:
 - "1.10.2"
 - "latest"
 - "1.11.1"
description: "Ninja is a small build system with a focus on speed."
config: {"docker": "ghcr.io/autamus/ninja", "url": "https://github.com/orgs/autamus/packages/container/package/ninja", "maintainer": "@vsoch", "description": "Ninja is a small build system with a focus on speed.", "latest": {"1.11.1": "sha256:ae9869ef5131ea4ca7dc25269fdc065dffa9ebc4c3d020b3b71ae39d5f735e03"}, "tags": {"1.10.2": "sha256:41ff2df8bff8339897ff31120dfb0509dc328aa5396946c497d2a4df0adc9d36", "latest": "sha256:ae9869ef5131ea4ca7dc25269fdc065dffa9ebc4c3d020b3b71ae39d5f735e03", "1.11.1": "sha256:ae9869ef5131ea4ca7dc25269fdc065dffa9ebc4c3d020b3b71ae39d5f735e03"}, "aliases": {"ninja": "/opt/view/bin/ninja", "ninja-build": "/opt/view/bin/ninja-build"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/ninja.
Ninja is a small build system with a focus on speed.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/ninja
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ninja:1.11.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ninja/1.11.1
$ module help ghcr.io/autamus/ninja/1.11.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ninja-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ninja-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ninja-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ninja-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ninja-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ninja-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ninja

```bash
$ singularity exec <container> /opt/view/bin/ninja
$ podman run --it --rm --entrypoint /opt/view/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ninja-build

```bash
$ singularity exec <container> /opt/view/bin/ninja-build
$ podman run --it --rm --entrypoint /opt/view/bin/ninja-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ninja-build   -v ${PWD} -w ${PWD} <container> -c " $@"
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