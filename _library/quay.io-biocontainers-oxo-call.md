---
layout: container
name:  "quay.io/biocontainers/oxo-call"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oxo-call/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oxo-call/container.yaml"
updated_at: "2026-04-03 05:15:36.425201"
latest: "0.9.2--h54198d6_0"
container_url: "https://biocontainers.pro/tools/oxo-call"
aliases:
 - "oxo-call"
versions:
 - "0.9.2--h54198d6_0"
description: "singularity registry hpc automated addition for oxo-call"
config: {"url": "https://biocontainers.pro/tools/oxo-call", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for oxo-call", "latest": {"0.9.2--h54198d6_0": "sha256:9eece5e56aa0b2e7e53aaeb201e4d887a3e9d371b077ef8676a3bb1736a50f9d"}, "tags": {"0.9.2--h54198d6_0": "sha256:9eece5e56aa0b2e7e53aaeb201e4d887a3e9d371b077ef8676a3bb1736a50f9d"}, "docker": "quay.io/biocontainers/oxo-call", "aliases": {"oxo-call": "/usr/local/bin/oxo-call"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oxo-call.
singularity registry hpc automated addition for oxo-call
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oxo-call
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oxo-call:0.9.2--h54198d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oxo-call/0.9.2--h54198d6_0
$ module help quay.io/biocontainers/oxo-call/0.9.2--h54198d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oxo-call-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oxo-call-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oxo-call-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oxo-call-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oxo-call-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oxo-call-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### oxo-call

```bash
$ singularity exec <container> /usr/local/bin/oxo-call
$ podman run --it --rm --entrypoint /usr/local/bin/oxo-call   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oxo-call   -v ${PWD} -w ${PWD} <container> -c " $@"
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