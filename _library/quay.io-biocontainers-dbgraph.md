---
layout: container
name:  "quay.io/biocontainers/dbgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dbgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dbgraph/container.yaml"
updated_at: "2024-11-06 02:51:48.344908"
latest: "v1.0.0--h6bb024c_1"
container_url: "https://biocontainers.pro/tools/dbgraph"
aliases:
 - "DBGraph2Pro"
 - "DBGraphPep2Pro"
versions:
 - "v1.0.0--h6bb024c_1"
description: "shpc-registry automated BioContainers addition for dbgraph"
config: {"url": "https://biocontainers.pro/tools/dbgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dbgraph", "latest": {"v1.0.0--h6bb024c_1": "sha256:790328a5fef33094f1e01d6b02aec144d4a617877c118362c3fb3c8bd1ad8a0b"}, "tags": {"v1.0.0--h6bb024c_1": "sha256:790328a5fef33094f1e01d6b02aec144d4a617877c118362c3fb3c8bd1ad8a0b"}, "docker": "quay.io/biocontainers/dbgraph", "aliases": {"DBGraph2Pro": "/usr/local/bin/DBGraph2Pro", "DBGraphPep2Pro": "/usr/local/bin/DBGraphPep2Pro"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dbgraph.
shpc-registry automated BioContainers addition for dbgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dbgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dbgraph:v1.0.0--h6bb024c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dbgraph/v1.0.0--h6bb024c_1
$ module help quay.io/biocontainers/dbgraph/v1.0.0--h6bb024c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dbgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dbgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dbgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dbgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dbgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dbgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DBGraph2Pro

```bash
$ singularity exec <container> /usr/local/bin/DBGraph2Pro
$ podman run --it --rm --entrypoint /usr/local/bin/DBGraph2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBGraph2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBGraphPep2Pro

```bash
$ singularity exec <container> /usr/local/bin/DBGraphPep2Pro
$ podman run --it --rm --entrypoint /usr/local/bin/DBGraphPep2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBGraphPep2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
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