---
layout: container
name:  "quay.io/pawsey/openfoam-org"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/openfoam-org/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/openfoam-org/container.yaml"
updated_at: "2025-08-28 12:44:29.656104"
latest: "12"
container_url: "https://quay.io/repository/pawsey/openfoam-org"

versions:
 - "12"
 - "10"
 - "9"
 - "8"
 - "7"
description: "OpenFOAM (openfoam.org) images built on top of MPICH."
config: {"docker": "quay.io/pawsey/openfoam-org", "url": "https://quay.io/repository/pawsey/openfoam-org", "maintainer": "@alexisespinosa", "description": "OpenFOAM (openfoam.org) images built on top of MPICH.", "latest": {"12": "sha256:09f54e09369bfd212a4c11334a13a18ca6aed5d4a7452ecac11cd2d145152753"}, "tags": {"12": "sha256:09f54e09369bfd212a4c11334a13a18ca6aed5d4a7452ecac11cd2d145152753", "10": "sha256:7b923a567b7792a7da827a09d60aedb90d2f324f69892ab86b2f8d970ecf8fb1", "9": "sha256:7df46fc4cc0844c66ddfb897f47bf79b3e4c33c3a9d9bf8169d2ac6ea896841f", "8": "sha256:a552ba767634ae7e87a8db9585476348ccbebdc3ae1d264f7af87384c291d4aa", "7": "sha256:c55d41ae5249c33a413a5fccd28053d1544d11deb46f01dd0411bd8493c89b2b"}, "overrides": {"12": "aliases/12.yaml", "10": "aliases/10.yaml", "9": "aliases/9.yaml", "8": "aliases/8.yaml", "7": "aliases/7.yaml"}}
---

This module is a singularity container wrapper for quay.io/pawsey/openfoam-org.
OpenFOAM (openfoam.org) images built on top of MPICH.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/openfoam-org
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/openfoam-org:12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/openfoam-org/12
$ module help quay.io/pawsey/openfoam-org/12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openfoam-org-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-org-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-org-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openfoam-org-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openfoam-org-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openfoam-org-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openfoam-org

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