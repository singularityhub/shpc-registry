---
layout: container
name:  "quay.io/biocontainers/samsifter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samsifter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samsifter/container.yaml"
updated_at: "2024-08-08 03:41:57.088651"
latest: "1.0.0--py35h3978dc7_3"
container_url: "https://biocontainers.pro/tools/samsifter"

versions:
 - "1.0.0--py35h3978dc7_3"
 - "1.0.0--py36h3978dc7_3"
description: "shpc-registry automated BioContainers addition for samsifter"
config: {"url": "https://biocontainers.pro/tools/samsifter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samsifter", "latest": {"1.0.0--py35h3978dc7_3": "sha256:2c3bd0ceb557050993c1be433bc1795366e06d4ac7b09d9c984a75fb92b5fcbd"}, "tags": {"1.0.0--py35h3978dc7_3": "sha256:2c3bd0ceb557050993c1be433bc1795366e06d4ac7b09d9c984a75fb92b5fcbd", "1.0.0--py36h3978dc7_3": "sha256:3ae30293dd48607c5e8f39ae3d3e0f959e5294006caf2777e066ba1f2d1d8fdd"}, "docker": "quay.io/biocontainers/samsifter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/samsifter.
shpc-registry automated BioContainers addition for samsifter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samsifter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samsifter:1.0.0--py35h3978dc7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samsifter/1.0.0--py35h3978dc7_3
$ module help quay.io/biocontainers/samsifter/1.0.0--py35h3978dc7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samsifter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samsifter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samsifter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samsifter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samsifter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samsifter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### samsifter

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