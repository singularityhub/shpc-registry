---
layout: container
name:  "quay.io/biocontainers/miru-hero"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/miru-hero/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/miru-hero/container.yaml"
updated_at: "2022-10-27 01:07:33.592245"
latest: "0.10.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/miru-hero"
aliases:
 - "MiruHero"
versions:
 - "0.10.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for miru-hero"
config: {"url": "https://biocontainers.pro/tools/miru-hero", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for miru-hero", "latest": {"0.10.0--pyh5e36f6f_0": "sha256:c35f4b9201ed8c15f389e902cac1ac0e4e872031518461c3214deb83e29a8aa5"}, "tags": {"0.10.0--pyh5e36f6f_0": "sha256:c35f4b9201ed8c15f389e902cac1ac0e4e872031518461c3214deb83e29a8aa5"}, "docker": "quay.io/biocontainers/miru-hero", "aliases": {"MiruHero": "/usr/local/bin/MiruHero"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/miru-hero.
shpc-registry automated BioContainers addition for miru-hero
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/miru-hero
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/miru-hero:0.10.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/miru-hero/0.10.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/miru-hero/0.10.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### miru-hero-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### miru-hero-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### miru-hero-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### miru-hero-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### miru-hero-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### miru-hero-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MiruHero

```bash
$ singularity exec <container> /usr/local/bin/MiruHero
$ podman run --it --rm --entrypoint /usr/local/bin/MiruHero   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MiruHero   -v ${PWD} -w ${PWD} <container> -c " $@"
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