---
layout: container
name:  "ghcr.io/autamus/migrate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/migrate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/migrate/container.yaml"
updated_at: "2025-03-06 03:45:30.468649"
latest: "3.7.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/migrate"
aliases:
 - "migrate-n"
versions:
 - "3.7.2"
 - "latest"
description: "Migrate estimates effective population sizes and past migration rates between n population assuming a migration matrix model with asymmetric migration rates and different subpopulation sizes"
config: {"docker": "ghcr.io/autamus/migrate", "url": "https://github.com/orgs/autamus/packages/container/package/migrate", "maintainer": "@vsoch", "description": "Migrate estimates effective population sizes and past migration rates between n population assuming a migration matrix model with asymmetric migration rates and different subpopulation sizes", "latest": {"3.7.2": "sha256:9c5928d4a3654f84f88748c25cb4718c5f3bc397bf2ca40318b15c6ab6fcf939"}, "tags": {"3.7.2": "sha256:9c5928d4a3654f84f88748c25cb4718c5f3bc397bf2ca40318b15c6ab6fcf939", "latest": "sha256:9c5928d4a3654f84f88748c25cb4718c5f3bc397bf2ca40318b15c6ab6fcf939"}, "aliases": {"migrate-n": "/opt/view/bin/migrate-n"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/migrate.
Migrate estimates effective population sizes and past migration rates between n population assuming a migration matrix model with asymmetric migration rates and different subpopulation sizes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/migrate
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/migrate:3.7.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/migrate/3.7.2
$ module help ghcr.io/autamus/migrate/3.7.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### migrate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### migrate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### migrate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### migrate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### migrate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### migrate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### migrate-n

```bash
$ singularity exec <container> /opt/view/bin/migrate-n
$ podman run --it --rm --entrypoint /opt/view/bin/migrate-n   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/migrate-n   -v ${PWD} -w ${PWD} <container> -c " $@"
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