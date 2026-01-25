---
layout: container
name:  "quay.io/biocontainers/fstic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fstic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fstic/container.yaml"
updated_at: "2026-01-25 04:48:19.023641"
latest: "1.0.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/fstic"
aliases:
 - "fstic"
versions:
 - "1.0.0--h4349ce8_0"
description: "singularity registry hpc automated addition for fstic"
config: {"url": "https://biocontainers.pro/tools/fstic", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fstic", "latest": {"1.0.0--h4349ce8_0": "sha256:170556752d24a2e3edb49434d4f18889554d595b293892bbc4e7bc2cf6c445d3"}, "tags": {"1.0.0--h4349ce8_0": "sha256:170556752d24a2e3edb49434d4f18889554d595b293892bbc4e7bc2cf6c445d3"}, "docker": "quay.io/biocontainers/fstic", "aliases": {"fstic": "/usr/local/bin/fstic"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fstic.
singularity registry hpc automated addition for fstic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fstic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fstic:1.0.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fstic/1.0.0--h4349ce8_0
$ module help quay.io/biocontainers/fstic/1.0.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fstic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fstic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fstic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fstic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fstic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fstic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fstic

```bash
$ singularity exec <container> /usr/local/bin/fstic
$ podman run --it --rm --entrypoint /usr/local/bin/fstic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fstic   -v ${PWD} -w ${PWD} <container> -c " $@"
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