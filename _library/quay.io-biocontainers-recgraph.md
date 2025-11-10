---
layout: container
name:  "quay.io/biocontainers/recgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/recgraph/container.yaml"
updated_at: "2025-11-10 04:12:04.800271"
latest: "1.0.0--h7b50bb2_1"
container_url: "https://biocontainers.pro/tools/recgraph"
aliases:
 - "recgraph"
versions:
 - "1.0.0--h031d066_0"
 - "1.0.0--h7b50bb2_1"
description: "singularity registry hpc automated addition for recgraph"
config: {"url": "https://biocontainers.pro/tools/recgraph", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for recgraph", "latest": {"1.0.0--h7b50bb2_1": "sha256:a1198a52e671241ccea337a034aa0b6d627b4ce763d96e2293b0c23cfff38ab0"}, "tags": {"1.0.0--h031d066_0": "sha256:3534eba6ca4986a588c86067f458b201764ca85a0b8770ca74e5111a71514beb", "1.0.0--h7b50bb2_1": "sha256:a1198a52e671241ccea337a034aa0b6d627b4ce763d96e2293b0c23cfff38ab0"}, "docker": "quay.io/biocontainers/recgraph", "aliases": {"recgraph": "/usr/local/bin/recgraph"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recgraph.
singularity registry hpc automated addition for recgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recgraph:1.0.0--h7b50bb2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recgraph/1.0.0--h7b50bb2_1
$ module help quay.io/biocontainers/recgraph/1.0.0--h7b50bb2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### recgraph

```bash
$ singularity exec <container> /usr/local/bin/recgraph
$ podman run --it --rm --entrypoint /usr/local/bin/recgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
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