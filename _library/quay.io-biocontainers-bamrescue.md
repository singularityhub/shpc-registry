---
layout: container
name:  "quay.io/biocontainers/bamrescue"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamrescue/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamrescue/container.yaml"
updated_at: "2025-10-27 03:24:29.176523"
latest: "0.3.0--h4349ce8_1"
container_url: "https://biocontainers.pro/tools/bamrescue"
aliases:
 - "bamrescue"
versions:
 - "0.3.0--h4349ce8_1"
description: "singularity registry hpc automated addition for bamrescue"
config: {"url": "https://biocontainers.pro/tools/bamrescue", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bamrescue", "latest": {"0.3.0--h4349ce8_1": "sha256:57a3eefaedb8aa17be327a6f3939f6889528e6709bd37e949c629351bbb37d85"}, "tags": {"0.3.0--h4349ce8_1": "sha256:57a3eefaedb8aa17be327a6f3939f6889528e6709bd37e949c629351bbb37d85"}, "docker": "quay.io/biocontainers/bamrescue", "aliases": {"bamrescue": "/usr/local/bin/bamrescue"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamrescue.
singularity registry hpc automated addition for bamrescue
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamrescue
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamrescue:0.3.0--h4349ce8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamrescue/0.3.0--h4349ce8_1
$ module help quay.io/biocontainers/bamrescue/0.3.0--h4349ce8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamrescue-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamrescue-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamrescue-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamrescue-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamrescue-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamrescue-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamrescue

```bash
$ singularity exec <container> /usr/local/bin/bamrescue
$ podman run --it --rm --entrypoint /usr/local/bin/bamrescue   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamrescue   -v ${PWD} -w ${PWD} <container> -c " $@"
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