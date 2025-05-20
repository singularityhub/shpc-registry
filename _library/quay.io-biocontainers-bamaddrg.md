---
layout: container
name:  "quay.io/biocontainers/bamaddrg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamaddrg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamaddrg/container.yaml"
updated_at: "2025-05-20 03:34:41.815711"
latest: "9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2"
container_url: "https://biocontainers.pro/tools/bamaddrg"
aliases:
 - "bamaddrg"
versions:
 - "9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2"
description: "shpc-registry automated BioContainers addition for bamaddrg"
config: {"url": "https://biocontainers.pro/tools/bamaddrg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamaddrg", "latest": {"9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2": "sha256:a0f416c2cb10a266a05814a39cf040e0322a2162f32269eec041964b0e535472"}, "tags": {"9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2": "sha256:a0f416c2cb10a266a05814a39cf040e0322a2162f32269eec041964b0e535472"}, "docker": "quay.io/biocontainers/bamaddrg", "aliases": {"bamaddrg": "/usr/local/bin/bamaddrg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamaddrg.
shpc-registry automated BioContainers addition for bamaddrg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamaddrg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamaddrg:9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamaddrg/9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2
$ module help quay.io/biocontainers/bamaddrg/9baba65f88228e55639689a3cea38dd150e6284f--h4dc6686_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamaddrg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamaddrg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamaddrg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamaddrg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamaddrg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamaddrg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamaddrg

```bash
$ singularity exec <container> /usr/local/bin/bamaddrg
$ podman run --it --rm --entrypoint /usr/local/bin/bamaddrg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamaddrg   -v ${PWD} -w ${PWD} <container> -c " $@"
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