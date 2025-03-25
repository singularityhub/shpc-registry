---
layout: container
name:  "quay.io/biocontainers/pyabpoa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyabpoa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyabpoa/container.yaml"
updated_at: "2025-03-25 03:39:57.689013"
latest: "1.5.3--py312h4711d71_1"
container_url: "https://biocontainers.pro/tools/pyabpoa"
aliases:
 - "cygdb"
 - "cython"
 - "cythonize"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.4.0--py39hbf8eff0_0"
 - "1.4.1--py38h7cf9df2_0"
 - "1.5.0--py310h83093d7_0"
 - "1.4.2--py310h83093d7_0"
 - "1.5.1--py38h7cf9df2_0"
 - "1.5.1--py310h83093d7_1"
 - "1.4.2--py39h3d4b85c_0"
 - "1.5.1--py310h1af8fb7_2"
 - "1.5.2--py312he57d009_1"
 - "1.5.3--py310h1af8fb7_0"
 - "1.5.3--py312h4711d71_1"
description: "singularity registry hpc automated addition for pyabpoa"
config: {"url": "https://biocontainers.pro/tools/pyabpoa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyabpoa", "latest": {"1.5.3--py312h4711d71_1": "sha256:60f40df46a37061e99e3a288a9930e0a4d772175338a24a0b30f33fdf5d22061"}, "tags": {"1.4.0--py39hbf8eff0_0": "sha256:d62835fbc0ec3bb797e14c2245cc0e6a135128299f4ba0127951476e552d4325", "1.4.1--py38h7cf9df2_0": "sha256:0739e74763048468f1696574f387cbf8a3625900af4bb0cd49ab1fa69f696b70", "1.5.0--py310h83093d7_0": "sha256:c618856a3ebcf9d15af9ecbca8267c1eee4cc7cb40be0dac6bca2357b2cbba07", "1.4.2--py310h83093d7_0": "sha256:79fe01c85587b6f0dfeae67bafd35963a0744aab7e7a27c329584daed71b0c30", "1.5.1--py38h7cf9df2_0": "sha256:d8ab1afbfece313a6e78b727f91ab18a349cdc3ed895cd55e8a6fb7bbd3c80a0", "1.5.1--py310h83093d7_1": "sha256:de3cc611de664dda2363155b7ad0b92ee060d28976807884a921f27db9b55448", "1.4.2--py39h3d4b85c_0": "sha256:29b9ebbde6a17055f5e31b49b1f4b9921cecd89028e734f4cf70011dd6fadc07", "1.5.1--py310h1af8fb7_2": "sha256:cd025b161e9acc940e39c2286e48ab071e00395f914b9e3b8968c7315eaac1be", "1.5.2--py312he57d009_1": "sha256:e02f25954798d67b47106a919f0e824aafb01b491c9292fedfb03ee89544a057", "1.5.3--py310h1af8fb7_0": "sha256:810d6801fabfff281607344fc5202c9c570e27931555760ba570967c638421b4", "1.5.3--py312h4711d71_1": "sha256:60f40df46a37061e99e3a288a9930e0a4d772175338a24a0b30f33fdf5d22061"}, "docker": "quay.io/biocontainers/pyabpoa", "aliases": {"cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyabpoa.
singularity registry hpc automated addition for pyabpoa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyabpoa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyabpoa:1.5.3--py312h4711d71_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyabpoa/1.5.3--py312h4711d71_1
$ module help quay.io/biocontainers/pyabpoa/1.5.3--py312h4711d71_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyabpoa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyabpoa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyabpoa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyabpoa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyabpoa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyabpoa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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