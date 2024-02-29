---
layout: container
name:  "quay.io/biocontainers/bamstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamstats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamstats/container.yaml"
updated_at: "2024-02-29 02:55:50.739265"
latest: "0.3.5--he881be0_0"
container_url: "https://biocontainers.pro/tools/bamstats"
aliases:
 - "bamstats"
versions:
 - "0.3.5--he881be0_0"
description: "singularity registry hpc automated addition for bamstats"
config: {"url": "https://biocontainers.pro/tools/bamstats", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bamstats", "latest": {"0.3.5--he881be0_0": "sha256:179a9d7aad5efee29b749fa71d3d955f1d4aac5d1aec3a52ccb9b65fa34a6b91"}, "tags": {"0.3.5--he881be0_0": "sha256:179a9d7aad5efee29b749fa71d3d955f1d4aac5d1aec3a52ccb9b65fa34a6b91"}, "docker": "quay.io/biocontainers/bamstats", "aliases": {"bamstats": "/usr/local/bin/bamstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamstats.
singularity registry hpc automated addition for bamstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamstats:0.3.5--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamstats/0.3.5--he881be0_0
$ module help quay.io/biocontainers/bamstats/0.3.5--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamstats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamstats

```bash
$ singularity exec <container> /usr/local/bin/bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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