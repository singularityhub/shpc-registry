---
layout: container
name:  "quay.io/biocontainers/doebase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/doebase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/doebase/container.yaml"
updated_at: "2024-12-27 03:05:36.326277"
latest: "2.0.2"
container_url: "https://biocontainers.pro/tools/doebase"

versions:
 - "2.0.2"
 - "v2.0.2"
description: "shpc-registry automated BioContainers addition for doebase"
config: {"url": "https://biocontainers.pro/tools/doebase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for doebase", "latest": {"2.0.2": "sha256:359898a4daa75c8e484e3c1eeb89536bc7db0c807a7d86ee6c7c67f881e6dd60"}, "tags": {"2.0.2": "sha256:359898a4daa75c8e484e3c1eeb89536bc7db0c807a7d86ee6c7c67f881e6dd60", "v2.0.2": "sha256:7d596626854c9979203e58adec68cd4789096b047b712c0b39a68f90e2c98aef"}, "docker": "quay.io/biocontainers/doebase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/doebase.
shpc-registry automated BioContainers addition for doebase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/doebase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/doebase:2.0.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/doebase/2.0.2
$ module help quay.io/biocontainers/doebase/2.0.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### doebase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### doebase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### doebase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### doebase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### doebase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### doebase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### doebase

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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