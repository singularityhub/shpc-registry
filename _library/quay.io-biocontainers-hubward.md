---
layout: container
name:  "quay.io/biocontainers/hubward"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hubward/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hubward/container.yaml"
updated_at: "2024-02-08 08:25:14.462904"
latest: "0.2.2--py27_1"
container_url: "https://biocontainers.pro/tools/hubward"

versions:
 - "0.2.2--py27_1"
description: "shpc-registry automated BioContainers addition for hubward"
config: {"url": "https://biocontainers.pro/tools/hubward", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hubward", "latest": {"0.2.2--py27_1": "sha256:d88b301d815cdeb431d628553656c466fbc744f90b4fd28461fba3ecc629727c"}, "tags": {"0.2.2--py27_1": "sha256:d88b301d815cdeb431d628553656c466fbc744f90b4fd28461fba3ecc629727c"}, "docker": "quay.io/biocontainers/hubward"}
---

This module is a singularity container wrapper for quay.io/biocontainers/hubward.
shpc-registry automated BioContainers addition for hubward
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hubward
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hubward:0.2.2--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hubward/0.2.2--py27_1
$ module help quay.io/biocontainers/hubward/0.2.2--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hubward-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hubward-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hubward-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hubward-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hubward-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hubward-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### hubward

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