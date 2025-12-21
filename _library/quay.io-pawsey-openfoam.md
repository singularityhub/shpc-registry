---
layout: container
name:  "quay.io/pawsey/openfoam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/openfoam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/openfoam/container.yaml"
updated_at: "2025-12-21 03:42:34.177840"
latest: "v2412"
container_url: "https://quay.io/repository/pawsey/openfoam"

versions:
 - "v2412"
 - "v2212"
 - "v2206"
 - "v2012"
 - "v2006"
 - "v1912"
 - "v2312-rocm573-gcc"
 - "v2312-rocm5.4-gcc"
description: "OpenFOAM (openfoam.com) images built on top of MPICH."
config: {"docker": "quay.io/pawsey/openfoam", "url": "https://quay.io/repository/pawsey/openfoam", "maintainer": "@alexisespinosa", "description": "OpenFOAM (openfoam.com) images built on top of MPICH.", "latest": {"v2412": "sha256:2cb2483c0c55691cb4ba60054fee2d57ece3259f33d927971b4843858cf8ef70"}, "tags": {"v2412": "sha256:2cb2483c0c55691cb4ba60054fee2d57ece3259f33d927971b4843858cf8ef70", "v2212": "sha256:e32b955c1daa6a55563cb0712069fb4ff8c5c5105170cd86d990baff688e6077", "v2206": "sha256:280ac49a6cbb55b95582fa23156a30ed85097bc3c44551ffe1c82d376143f557", "v2012": "sha256:efdb5fe0c9868992dcf361884414d71f8a79ed44113f0df279058a33a18bc455", "v2006": "sha256:36c9bdfe806242d7ccb993731631faec06d3a3c316d37729e57397f94f104e09", "v1912": "sha256:f053492bd5b7aa96e1d958715ed62f0072dcfdab6fbff3c307092776ea7fa742", "v2312-rocm573-gcc": "sha256:1f36c091ab61245a31d691911e393c2c1f961fe7b61912ce8a8a8a0dfd973457", "v2312-rocm5.4-gcc": "sha256:30259d9ee933fd4a82d418c893d8a7fab26b7da9b53a43eb4242ef34fb278bb4"}, "overrides": {"v2412": "aliases/v2412.yaml", "v2212": "aliases/v2212.yaml", "v2206": "aliases/v2206.yaml", "v2012": "aliases/v2012.yaml", "v2006": "aliases/v2006.yaml", "v1912": "aliases/v1912.yaml"}}
---

This module is a singularity container wrapper for quay.io/pawsey/openfoam.
OpenFOAM (openfoam.com) images built on top of MPICH.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/openfoam
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/openfoam:v2412
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/openfoam/v2412
$ module help quay.io/pawsey/openfoam/v2412
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