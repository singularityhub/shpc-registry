---
layout: container
name:  "quay.io/biocontainers/go-yq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/go-yq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/go-yq/container.yaml"
updated_at: "2026-10-10 19:23:29.110985"
latest: "4.53.3"
container_url: "https://biocontainers.pro/tools/go-yq"
aliases:
 - "yq"
versions:
 - "4.53.3"
description: "singularity registry hpc automated addition for go-yq"
config: {"url": "https://biocontainers.pro/tools/go-yq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for go-yq", "latest": {"4.53.3": "sha256:dba83f7a07334203210d6ee8da5974d7eb5c9e0ffc8e4507e6b013b14c8cf61b"}, "tags": {"4.53.3": "sha256:dba83f7a07334203210d6ee8da5974d7eb5c9e0ffc8e4507e6b013b14c8cf61b"}, "docker": "quay.io/biocontainers/go-yq", "aliases": {"yq": "/usr/local/bin/yq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/go-yq.
singularity registry hpc automated addition for go-yq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/go-yq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/go-yq:4.53.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/go-yq/4.53.3
$ module help quay.io/biocontainers/go-yq/4.53.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### go-yq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### go-yq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### go-yq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### go-yq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### go-yq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### go-yq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### yq

```bash
$ singularity exec <container> /usr/local/bin/yq
$ podman run --it --rm --entrypoint /usr/local/bin/yq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yq   -v ${PWD} -w ${PWD} <container> -c " $@"
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