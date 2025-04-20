---
layout: container
name:  "quay.io/biocontainers/pybedlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pybedlite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pybedlite/container.yaml"
updated_at: "2025-04-20 03:36:05.568642"
latest: "1.0.0--py310h1fe012e_3"
container_url: "https://biocontainers.pro/tools/pybedlite"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.0.2--pyhdfd78af_0"
 - "0.0.3--pyhdfd78af_0"
 - "0.0.4--py38he5da3d1_0"
 - "0.0.4--py39hf95cd2a_0"
 - "0.1.0--py38he5da3d1_0"
 - "0.1.0--py39hff71179_1"
 - "1.0.0--py311hdad781d_1"
 - "1.0.0--py310h1fe012e_2"
 - "1.0.0--py310h1fe012e_3"
description: "singularity registry hpc automated addition for pybedlite"
config: {"url": "https://biocontainers.pro/tools/pybedlite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pybedlite", "latest": {"1.0.0--py310h1fe012e_3": "sha256:c47e7a41b4c41cd49e7b9942d88d62b1e5d0eb9af74fd7a6e0290362d4d8a92d"}, "tags": {"0.0.2--pyhdfd78af_0": "sha256:500efc9947d7803c722c39c20aceb840154ddbce2eed46a95050584343a0ec06", "0.0.3--pyhdfd78af_0": "sha256:55f09d10d9490ac54400883b3a322a00df5046e78a30c43ee7e7f9ed66ae6ddd", "0.0.4--py38he5da3d1_0": "sha256:b66f2812958e8c9383d983d288166b114eab9cfb0722724bc74bf829a2bf54cb", "0.0.4--py39hf95cd2a_0": "sha256:59879ccc4dbf0b0405d24dd2865aba71114ea9ff5ccd63d0847185819f9517a3", "0.1.0--py38he5da3d1_0": "sha256:aab591ef8b23934bc419ca88a87ef05c9461321c46c1229d00cda46b6486d0ad", "0.1.0--py39hff71179_1": "sha256:9c01093a77aca4a8098f6f746d1d9dd9c0182d8a303e2c4f9ff3501c9aed09e6", "1.0.0--py311hdad781d_1": "sha256:55e8b72b678462c362f526cd8d60b508513d58ca7564885f9ffb6da69cbf001e", "1.0.0--py310h1fe012e_2": "sha256:cb3f79661160dad8e57200698b0ceb49680daa4d83711b10a74840cbd220e55c", "1.0.0--py310h1fe012e_3": "sha256:c47e7a41b4c41cd49e7b9942d88d62b1e5d0eb9af74fd7a6e0290362d4d8a92d"}, "docker": "quay.io/biocontainers/pybedlite", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pybedlite.
singularity registry hpc automated addition for pybedlite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pybedlite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pybedlite:1.0.0--py310h1fe012e_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pybedlite/1.0.0--py310h1fe012e_3
$ module help quay.io/biocontainers/pybedlite/1.0.0--py310h1fe012e_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pybedlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pybedlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pybedlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pybedlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pybedlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pybedlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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