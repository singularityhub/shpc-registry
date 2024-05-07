---
layout: container
name:  "ghcr.io/autamus/geos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/geos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/geos/container.yaml"
updated_at: "2024-05-07 03:18:39.963340"
latest: "3.9.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/geos"
aliases:
 - "geos-config"
versions:
 - "3.8.1"
 - "3.9.1"
 - "latest"
description: "GEOS is a C++11 library for performing operations on two-dimensional vector geometries."
config: {"docker": "ghcr.io/autamus/geos", "url": "https://github.com/orgs/autamus/packages/container/package/geos", "maintainer": "@vsoch", "description": "GEOS is a C++11 library for performing operations on two-dimensional vector geometries.", "latest": {"3.9.1": "sha256:302ad36c2c85918e96c8898c06eedede098c2e6d18e86c00b268dfb1295a467f"}, "tags": {"3.8.1": "sha256:731b5a546569eabad6aa69e43a01b507184379a04f5071d55d96a213bf22a121", "3.9.1": "sha256:302ad36c2c85918e96c8898c06eedede098c2e6d18e86c00b268dfb1295a467f", "latest": "sha256:302ad36c2c85918e96c8898c06eedede098c2e6d18e86c00b268dfb1295a467f"}, "aliases": {"geos-config": "/opt/view/bin/geos-config"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/geos.
GEOS is a C++11 library for performing operations on two-dimensional vector geometries.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/geos
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/geos:3.9.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/geos/3.9.1
$ module help ghcr.io/autamus/geos/3.9.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geos-config

```bash
$ singularity exec <container> /opt/view/bin/geos-config
$ podman run --it --rm --entrypoint /opt/view/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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