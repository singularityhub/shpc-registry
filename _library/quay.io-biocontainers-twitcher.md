---
layout: container
name:  "quay.io/biocontainers/twitcher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/twitcher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/twitcher/container.yaml"
updated_at: "2026-10-28 08:08:50.309177"
latest: "0.8.1--hc38652c_0"
container_url: "https://biocontainers.pro/tools/twitcher"
aliases:
 - "twitcher"
versions:
 - "0.8.1--hc38652c_0"
description: "singularity registry hpc automated addition for twitcher"
config: {"url": "https://biocontainers.pro/tools/twitcher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for twitcher", "latest": {"0.8.1--hc38652c_0": "sha256:fd5fe0b747dea0d630d2a28ee76e5b90c79531cd47c6e8a863994c167c3cf200"}, "tags": {"0.8.1--hc38652c_0": "sha256:fd5fe0b747dea0d630d2a28ee76e5b90c79531cd47c6e8a863994c167c3cf200"}, "docker": "quay.io/biocontainers/twitcher", "aliases": {"twitcher": "/usr/local/bin/twitcher"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/twitcher.
singularity registry hpc automated addition for twitcher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/twitcher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/twitcher:0.8.1--hc38652c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/twitcher/0.8.1--hc38652c_0
$ module help quay.io/biocontainers/twitcher/0.8.1--hc38652c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### twitcher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### twitcher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### twitcher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### twitcher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### twitcher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### twitcher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### twitcher

```bash
$ singularity exec <container> /usr/local/bin/twitcher
$ podman run --it --rm --entrypoint /usr/local/bin/twitcher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twitcher   -v ${PWD} -w ${PWD} <container> -c " $@"
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