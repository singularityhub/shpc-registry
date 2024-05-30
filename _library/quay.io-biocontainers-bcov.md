---
layout: container
name:  "quay.io/biocontainers/bcov"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bcov/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bcov/container.yaml"
updated_at: "2024-05-30 03:09:19.185054"
latest: "1.0--ha16aae7_8"
container_url: "https://biocontainers.pro/tools/bcov"
aliases:
 - "bcov"
 - "glpsol"
versions:
 - "1.0--h2b57dba_4"
 - "1.0--h7dd7c9e_5"
 - "1.0--ha16aae7_7"
 - "1.0--ha16aae7_8"
description: "shpc-registry automated BioContainers addition for bcov"
config: {"url": "https://biocontainers.pro/tools/bcov", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bcov", "latest": {"1.0--ha16aae7_8": "sha256:c47f4367d0ea516453c413b7dfab036b3da80e5926d569d1547ca1b4813d27eb"}, "tags": {"1.0--h2b57dba_4": "sha256:9a011f8c9acd441b220a24866ff94e4c9b601ea060b75c442b05c58a47d971a4", "1.0--h7dd7c9e_5": "sha256:fb024166348604b0f0d3e7ddaa51f2013aaa502309883a55faf101136d3e2747", "1.0--ha16aae7_7": "sha256:68318115f2a37afb1b13ba2e835dd2a012cef08644957865fec02b5a346d652b", "1.0--ha16aae7_8": "sha256:c47f4367d0ea516453c413b7dfab036b3da80e5926d569d1547ca1b4813d27eb"}, "docker": "quay.io/biocontainers/bcov", "aliases": {"bcov": "/usr/local/bin/bcov", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bcov.
shpc-registry automated BioContainers addition for bcov
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bcov
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bcov:1.0--ha16aae7_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bcov/1.0--ha16aae7_8
$ module help quay.io/biocontainers/bcov/1.0--ha16aae7_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcov-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcov-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcov-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcov-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcov-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcov-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcov

```bash
$ singularity exec <container> /usr/local/bin/bcov
$ podman run --it --rm --entrypoint /usr/local/bin/bcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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