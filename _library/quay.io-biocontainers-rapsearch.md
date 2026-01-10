---
layout: container
name:  "quay.io/biocontainers/rapsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rapsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rapsearch/container.yaml"
updated_at: "2026-01-10 03:45:57.337498"
latest: "2.24--h376f1d3_7"
container_url: "https://biocontainers.pro/tools/rapsearch"
aliases:
 - "prerapsearch"
 - "rapsearch"
versions:
 - "2.24--h2df963e_5"
 - "2.24--h376f1d3_7"
description: "shpc-registry automated BioContainers addition for rapsearch"
config: {"url": "https://biocontainers.pro/tools/rapsearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rapsearch", "latest": {"2.24--h376f1d3_7": "sha256:eabb58114b05e1edd4aefb05bb60901689eb68e1abc0556577e09b3ca39cb336"}, "tags": {"2.24--h2df963e_5": "sha256:2d789f3c7e2fa71baa602f900756bb03909ede7c124f2b8eb9c048aeed07b88e", "2.24--h376f1d3_7": "sha256:eabb58114b05e1edd4aefb05bb60901689eb68e1abc0556577e09b3ca39cb336"}, "docker": "quay.io/biocontainers/rapsearch", "aliases": {"prerapsearch": "/usr/local/bin/prerapsearch", "rapsearch": "/usr/local/bin/rapsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rapsearch.
shpc-registry automated BioContainers addition for rapsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rapsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rapsearch:2.24--h376f1d3_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rapsearch/2.24--h376f1d3_7
$ module help quay.io/biocontainers/rapsearch/2.24--h376f1d3_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prerapsearch

```bash
$ singularity exec <container> /usr/local/bin/prerapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapsearch

```bash
$ singularity exec <container> /usr/local/bin/rapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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