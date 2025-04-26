---
layout: container
name:  "quay.io/biocontainers/kmc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmc/container.yaml"
updated_at: "2025-04-26 03:18:57.172698"
latest: "3.2.4--haf24da9_3"
container_url: "https://biocontainers.pro/tools/kmc"
aliases:
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
versions:
 - "3.2.1--hf1761c0_2"
 - "3.2.4--h6dccd9a_1"
 - "3.2.4--h6dccd9a_2"
 - "3.2.4--haf24da9_3"
description: "shpc-registry automated BioContainers addition for kmc"
config: {"url": "https://biocontainers.pro/tools/kmc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kmc", "latest": {"3.2.4--haf24da9_3": "sha256:c1d3d3f0539900cd4c135ea9551ac286b3c701c716839727e801f7b66081fcb0"}, "tags": {"3.2.1--hf1761c0_2": "sha256:caf06b4128b4a848e7782ac1f88e4f9f85e9ee8d4c7e03249168ce79be212e25", "3.2.4--h6dccd9a_1": "sha256:e02813f006a1a3df285f82bab31f539f2d2be2d2871c1f57203e9e4d12f4201e", "3.2.4--h6dccd9a_2": "sha256:ed0bd6d69caf09e384dad1a838281751b0b27bf463a0d0ddf19ebef242d61568", "3.2.4--haf24da9_3": "sha256:c1d3d3f0539900cd4c135ea9551ac286b3c701c716839727e801f7b66081fcb0"}, "docker": "quay.io/biocontainers/kmc", "aliases": {"kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmc.
shpc-registry automated BioContainers addition for kmc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmc:3.2.4--haf24da9_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmc/3.2.4--haf24da9_3
$ module help quay.io/biocontainers/kmc/3.2.4--haf24da9_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
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