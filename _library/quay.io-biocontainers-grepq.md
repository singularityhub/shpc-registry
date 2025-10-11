---
layout: container
name:  "quay.io/biocontainers/grepq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grepq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grepq/container.yaml"
updated_at: "2025-10-11 03:13:41.152733"
latest: "1.5.4--h6ce8773_0"
container_url: "https://biocontainers.pro/tools/grepq"
aliases:
 - "grepq"
versions:
 - "1.4.1--ha6fb395_0"
 - "1.4.7--ha6fb395_0"
 - "1.4.9--h6ce8773_0"
 - "1.5.4--h6ce8773_0"
description: "singularity registry hpc automated addition for grepq"
config: {"url": "https://biocontainers.pro/tools/grepq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grepq", "latest": {"1.5.4--h6ce8773_0": "sha256:c577d5cf997b82ff496ad88de06f2b1e416151e10e1ccc7ed170880e0e555772"}, "tags": {"1.4.1--ha6fb395_0": "sha256:ff454b701ddd5e8252f3642eaa25c1aecbedbb12f99eed19694d43a9e6e04b79", "1.4.7--ha6fb395_0": "sha256:fd0df0e593a6f0249ff307b3ae87053fe3402b16aba72e956ea3c5de93686ccb", "1.4.9--h6ce8773_0": "sha256:5849fd8253a89de4cd00f62d9315da8860faa7888a8a17c33cb5c1d407ac826a", "1.5.4--h6ce8773_0": "sha256:c577d5cf997b82ff496ad88de06f2b1e416151e10e1ccc7ed170880e0e555772"}, "docker": "quay.io/biocontainers/grepq", "aliases": {"grepq": "/usr/local/bin/grepq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grepq.
singularity registry hpc automated addition for grepq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grepq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grepq:1.5.4--h6ce8773_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grepq/1.5.4--h6ce8773_0
$ module help quay.io/biocontainers/grepq/1.5.4--h6ce8773_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grepq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grepq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grepq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grepq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grepq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grepq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grepq

```bash
$ singularity exec <container> /usr/local/bin/grepq
$ podman run --it --rm --entrypoint /usr/local/bin/grepq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grepq   -v ${PWD} -w ${PWD} <container> -c " $@"
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