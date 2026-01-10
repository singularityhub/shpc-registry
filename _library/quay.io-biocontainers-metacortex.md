---
layout: container
name:  "quay.io/biocontainers/metacortex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metacortex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metacortex/container.yaml"
updated_at: "2026-01-10 04:05:15.665399"
latest: "0.5.1--h7b50bb2_3"
container_url: "https://biocontainers.pro/tools/metacortex"
aliases:
 - "metacortex"
versions:
 - "0.5.1--hec16e2b_0"
 - "0.5.1--h031d066_2"
 - "0.5.1--h7b50bb2_3"
description: "singularity registry hpc automated addition for metacortex"
config: {"url": "https://biocontainers.pro/tools/metacortex", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metacortex", "latest": {"0.5.1--h7b50bb2_3": "sha256:b4daee8f062622ebf0396feee92696b03242fcbf3b01cf11458f79dc8e32a4e6"}, "tags": {"0.5.1--hec16e2b_0": "sha256:f8dc79c38f7432b2d3a6bd12a2b5439f2568986a63b2259bec0932b424acd7f7", "0.5.1--h031d066_2": "sha256:90bfd16ea85898fb61a6757761b6a0df4377330fdecd11a200b738b6660a778e", "0.5.1--h7b50bb2_3": "sha256:b4daee8f062622ebf0396feee92696b03242fcbf3b01cf11458f79dc8e32a4e6"}, "docker": "quay.io/biocontainers/metacortex", "aliases": {"metacortex": "/usr/local/bin/metacortex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metacortex.
singularity registry hpc automated addition for metacortex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metacortex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metacortex:0.5.1--h7b50bb2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metacortex/0.5.1--h7b50bb2_3
$ module help quay.io/biocontainers/metacortex/0.5.1--h7b50bb2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metacortex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metacortex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metacortex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metacortex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metacortex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metacortex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metacortex

```bash
$ singularity exec <container> /usr/local/bin/metacortex
$ podman run --it --rm --entrypoint /usr/local/bin/metacortex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacortex   -v ${PWD} -w ${PWD} <container> -c " $@"
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