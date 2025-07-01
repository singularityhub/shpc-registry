---
layout: container
name:  "quay.io/biocontainers/usearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/usearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/usearch/container.yaml"
updated_at: "2025-07-01 04:02:10.225841"
latest: "12.0_beta--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/usearch"
aliases:
 - "usearch"
versions:
 - "12.0_beta--h9ee0642_1"
description: "singularity registry hpc automated addition for usearch"
config: {"url": "https://biocontainers.pro/tools/usearch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for usearch", "latest": {"12.0_beta--h9ee0642_1": "sha256:9c78816e17a25875585203153578319983c7444fa26da5d86fa3d00c85f0fead"}, "tags": {"12.0_beta--h9ee0642_1": "sha256:9c78816e17a25875585203153578319983c7444fa26da5d86fa3d00c85f0fead"}, "docker": "quay.io/biocontainers/usearch", "aliases": {"usearch": "/usr/local/bin/usearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/usearch.
singularity registry hpc automated addition for usearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/usearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/usearch:12.0_beta--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/usearch/12.0_beta--h9ee0642_1
$ module help quay.io/biocontainers/usearch/12.0_beta--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### usearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### usearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### usearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### usearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### usearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### usearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### usearch

```bash
$ singularity exec <container> /usr/local/bin/usearch
$ podman run --it --rm --entrypoint /usr/local/bin/usearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/usearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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