---
layout: container
name:  "quay.io/biocontainers/beagle-lib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beagle-lib/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/beagle-lib/container.yaml"
updated_at: "2022-10-27 01:10:57.036249"
latest: "4.0.0--h9f5acd7_0"
container_url: "https://biocontainers.pro/tools/beagle-lib"

versions:
 - "4.0.0--h9f5acd7_0"
description: "shpc-registry automated BioContainers addition for beagle-lib"
config: {"url": "https://biocontainers.pro/tools/beagle-lib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for beagle-lib", "latest": {"4.0.0--h9f5acd7_0": "sha256:026cbb53b3eb273e21e1cc409ecc19dbc2d62955cc9c9c24ebcafed07a4cd2a9"}, "tags": {"4.0.0--h9f5acd7_0": "sha256:026cbb53b3eb273e21e1cc409ecc19dbc2d62955cc9c9c24ebcafed07a4cd2a9"}, "docker": "quay.io/biocontainers/beagle-lib"}
---

This module is a singularity container wrapper for quay.io/biocontainers/beagle-lib.
shpc-registry automated BioContainers addition for beagle-lib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beagle-lib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beagle-lib:4.0.0--h9f5acd7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beagle-lib/4.0.0--h9f5acd7_0
$ module help quay.io/biocontainers/beagle-lib/4.0.0--h9f5acd7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beagle-lib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beagle-lib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beagle-lib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beagle-lib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beagle-lib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beagle-lib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### beagle-lib

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