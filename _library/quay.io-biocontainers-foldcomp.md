---
layout: container
name:  "quay.io/biocontainers/foldcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/foldcomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/foldcomp/container.yaml"
updated_at: "2025-06-23 03:39:41.288485"
latest: "0.0.7--h5ca1c30_2"
container_url: "https://biocontainers.pro/tools/foldcomp"
aliases:
 - "foldcomp"
versions:
 - "0.0.2--h5b5514e_0"
 - "0.0.4--h5b5514e_0"
 - "0.0.5--h5b5514e_1"
 - "0.0.5--h43eeafb_2"
 - "0.0.7--h43eeafb_0"
 - "0.0.7--h43eeafb_1"
 - "0.0.7--h5ca1c30_2"
description: "singularity registry hpc automated addition for foldcomp"
config: {"url": "https://biocontainers.pro/tools/foldcomp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for foldcomp", "latest": {"0.0.7--h5ca1c30_2": "sha256:abbd6d5e2fd49ac3b2a74230d4a7add48b8c0e1cc1336060694df637cb5d8be8"}, "tags": {"0.0.2--h5b5514e_0": "sha256:584a4c9cc9bcdb5c75f23d8621f827e6ac48013d4b00b16afc20815828cb7608", "0.0.4--h5b5514e_0": "sha256:e567e5da15a5e3d90327613333984776dfba0b8e9eb396d036fecf9b241563c2", "0.0.5--h5b5514e_1": "sha256:dc9ab574d458895584f0de06100323a5551f2cea3d60a4c55b7b89f95e4a6349", "0.0.5--h43eeafb_2": "sha256:8aaaadb0bc0b494311cd64e648ee5e1e7516e1d9d893e5fb2cceaa11e6db3564", "0.0.7--h43eeafb_0": "sha256:5c20e958e6d66b37edb40efe5a0c5ae6174f754f5af19721fb08e97e296c9c8c", "0.0.7--h43eeafb_1": "sha256:9f1155f3ff3e059a51d31bdc6eabf93636b15ba0c370422f03989cf085298f2d", "0.0.7--h5ca1c30_2": "sha256:abbd6d5e2fd49ac3b2a74230d4a7add48b8c0e1cc1336060694df637cb5d8be8"}, "docker": "quay.io/biocontainers/foldcomp", "aliases": {"foldcomp": "/usr/local/bin/foldcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/foldcomp.
singularity registry hpc automated addition for foldcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/foldcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/foldcomp:0.0.7--h5ca1c30_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/foldcomp/0.0.7--h5ca1c30_2
$ module help quay.io/biocontainers/foldcomp/0.0.7--h5ca1c30_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### foldcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### foldcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### foldcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### foldcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### foldcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### foldcomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### foldcomp

```bash
$ singularity exec <container> /usr/local/bin/foldcomp
$ podman run --it --rm --entrypoint /usr/local/bin/foldcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
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