---
layout: container
name:  "quay.io/pawsey/openfoam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/openfoam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/openfoam/container.yaml"
updated_at: "2024-07-02 03:20:12.170101"
latest: "v2312-rocm573-gcc"
container_url: "https://quay.io/repository/pawsey/openfoam"

versions:
 - "v2212"
 - "v2206"
 - "v2012"
 - "v2006"
 - "v1912"
 - "v2212-aocc"
 - "v2312-rocm573-gcc"
description: "OpenFOAM (openfoam.com) images built on top of MPICH."
config: {"docker": "quay.io/pawsey/openfoam", "url": "https://quay.io/repository/pawsey/openfoam", "maintainer": "@alexisespinosa", "description": "OpenFOAM (openfoam.com) images built on top of MPICH.", "latest": {"v2312-rocm573-gcc": "sha256:1f36c091ab61245a31d691911e393c2c1f961fe7b61912ce8a8a8a0dfd973457"}, "tags": {"v2212": "sha256:993e7a71ccc34e23771165b805b9e2990f4969ebb7f5fde5aa26682635ef1699", "v2206": "sha256:eb1166003db57a4bae6de89d174425ec09009d65ffa5e1c89966e8cc42700be3", "v2012": "sha256:412a76a50084e80cc781ac8f53385c5cfe5f80d6e9917236b128c73c856ee269", "v2006": "sha256:c04e6d3df9051777c06b73e4fbcc404be75c721e9f0def0eda3598c031ecb766", "v1912": "sha256:69c1fe483dd44a8797620a5132492aadab3dba5ce322af8c1605fd23965676e1", "v2212-aocc": "sha256:3815e9eaa2584ec803fa64038b26587fc53a32d3d7aee30b6cd70c5ad928d0de", "v2312-rocm573-gcc": "sha256:1f36c091ab61245a31d691911e393c2c1f961fe7b61912ce8a8a8a0dfd973457"}, "overrides": {"v2212": "aliases/v2212.yaml", "v2206": "aliases/v2206.yaml", "v2012": "aliases/v2012.yaml", "v2006": "aliases/v2006.yaml", "v1912": "aliases/v1912.yaml"}}
---

This module is a singularity container wrapper for quay.io/pawsey/openfoam.
OpenFOAM (openfoam.com) images built on top of MPICH.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/openfoam
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/openfoam:v2312-rocm573-gcc
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/openfoam/v2312-rocm573-gcc
$ module help quay.io/pawsey/openfoam/v2312-rocm573-gcc
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openfoam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openfoam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openfoam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openfoam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openfoam

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