---
layout: container
name:  "quay.io/biocontainers/rsrq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rsrq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rsrq/container.yaml"
updated_at: "2024-03-17 02:52:42.168127"
latest: "1.1.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/rsrq"
aliases:
 - "rsrq"
versions:
 - "1.1.0--h4349ce8_0"
description: "singularity registry hpc automated addition for rsrq"
config: {"url": "https://biocontainers.pro/tools/rsrq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rsrq", "latest": {"1.1.0--h4349ce8_0": "sha256:94b7d9d6f1e406a3682aba22a9e5b0a456efa6eeb9a1a608320c12b85b6d8c04"}, "tags": {"1.1.0--h4349ce8_0": "sha256:94b7d9d6f1e406a3682aba22a9e5b0a456efa6eeb9a1a608320c12b85b6d8c04"}, "docker": "quay.io/biocontainers/rsrq", "aliases": {"rsrq": "/usr/local/bin/rsrq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rsrq.
singularity registry hpc automated addition for rsrq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rsrq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rsrq:1.1.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rsrq/1.1.0--h4349ce8_0
$ module help quay.io/biocontainers/rsrq/1.1.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rsrq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rsrq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rsrq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rsrq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rsrq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rsrq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rsrq

```bash
$ singularity exec <container> /usr/local/bin/rsrq
$ podman run --it --rm --entrypoint /usr/local/bin/rsrq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsrq   -v ${PWD} -w ${PWD} <container> -c " $@"
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