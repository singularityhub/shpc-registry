---
layout: container
name:  "ghcr.io/autamus/mummer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/mummer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/mummer/container.yaml"
updated_at: "2025-07-29 03:52:00.325038"
latest: "3.23"
container_url: "https://github.com/orgs/autamus/packages/container/package/mummer"
aliases:
 - "mummer"
 - "mummerplot"
versions:
 - "3.23"
 - "latest"
description: "MUMmer is a system for rapidly aligning entire genomes."
config: {"docker": "ghcr.io/autamus/mummer", "url": "https://github.com/orgs/autamus/packages/container/package/mummer", "maintainer": "@vsoch", "description": "MUMmer is a system for rapidly aligning entire genomes.", "latest": {"3.23": "sha256:0538b2e38b93ee87045ada01b8ec967fcda8d744f4cb045d339bd8feb04c96b1"}, "tags": {"3.23": "sha256:0538b2e38b93ee87045ada01b8ec967fcda8d744f4cb045d339bd8feb04c96b1", "latest": "sha256:0538b2e38b93ee87045ada01b8ec967fcda8d744f4cb045d339bd8feb04c96b1"}, "aliases": {"mummer": "/opt/view/bin/mummer", "mummerplot": "/opt/view/bin/mummerplot"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/mummer.
MUMmer is a system for rapidly aligning entire genomes.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/mummer
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mummer:3.23
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mummer/3.23
$ module help ghcr.io/autamus/mummer/3.23
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mummer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mummer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mummer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mummer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mummer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mummer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mummer

```bash
$ singularity exec <container> /opt/view/bin/mummer
$ podman run --it --rm --entrypoint /opt/view/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /opt/view/bin/mummerplot
$ podman run --it --rm --entrypoint /opt/view/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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