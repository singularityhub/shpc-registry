---
layout: container
name:  "quay.io/biocontainers/iucn_sim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/iucn_sim/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/iucn_sim/container.yaml"
updated_at: "2022-10-27 00:51:28.482776"
latest: "2.2.0--pyr40_0"
container_url: "https://biocontainers.pro/tools/iucn_sim"
aliases:
 - "iucn_sim"
versions:
 - "2.2.0--pyr40_0"
description: "shpc-registry automated BioContainers addition for iucn_sim"
config: {"url": "https://biocontainers.pro/tools/iucn_sim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for iucn_sim", "latest": {"2.2.0--pyr40_0": "sha256:4ce938acfc1c76506558a872b9ca6646166b9078ff13a00c25c4f3d1906e473a"}, "tags": {"2.2.0--pyr40_0": "sha256:4ce938acfc1c76506558a872b9ca6646166b9078ff13a00c25c4f3d1906e473a"}, "docker": "quay.io/biocontainers/iucn_sim", "aliases": {"iucn_sim": "/usr/local/bin/iucn_sim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/iucn_sim.
shpc-registry automated BioContainers addition for iucn_sim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/iucn_sim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/iucn_sim:2.2.0--pyr40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/iucn_sim/2.2.0--pyr40_0
$ module help quay.io/biocontainers/iucn_sim/2.2.0--pyr40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iucn_sim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iucn_sim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iucn_sim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iucn_sim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iucn_sim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iucn_sim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iucn_sim

```bash
$ singularity exec <container> /usr/local/bin/iucn_sim
$ podman run --it --rm --entrypoint /usr/local/bin/iucn_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iucn_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
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