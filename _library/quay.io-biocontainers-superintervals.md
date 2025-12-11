---
layout: container
name:  "quay.io/biocontainers/superintervals"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/superintervals/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/superintervals/container.yaml"
updated_at: "2025-12-11 04:44:42.211429"
latest: "0.3.5--py39he88f293_0"
container_url: "https://biocontainers.pro/tools/superintervals"
aliases:
 - "cygdb"
 - "cython"
 - "cythonize"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.5--py310h8ea774a_0"
 - "0.2.5--py312h9c9b0c2_0"
 - "0.2.9--py39he88f293_0"
 - "0.2.10--py311h8ddd9a4_0"
 - "0.2.10--py311h8ddd9a4_1"
 - "0.3.5--py39he88f293_0"
description: "singularity registry hpc automated addition for superintervals"
config: {"url": "https://biocontainers.pro/tools/superintervals", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for superintervals", "latest": {"0.3.5--py39he88f293_0": "sha256:c63858b6d3b6a6a1c6ec2523aadcfcf0eeecd43b903ac1b9db6f45b09d9db407"}, "tags": {"0.2.5--py310h8ea774a_0": "sha256:f13ebd829255882055f089b3e40e13385e2ecac28f5c45dfef809dcbaf56d02a", "0.2.5--py312h9c9b0c2_0": "sha256:fbc1b23256e4e7bc97f54468be1e245a2bcb0aa4a7288396ec0d86005d6a5e60", "0.2.9--py39he88f293_0": "sha256:34b01c9f414f08c5085f31c9d459a23c7ba95ce216c83eb743f54504929ad2c0", "0.2.10--py311h8ddd9a4_0": "sha256:e40210ef9f85587ab662ded3be687c25d2085f732a53e2f38f32a95b380553e4", "0.2.10--py311h8ddd9a4_1": "sha256:d977fe5d136e70e624eb26f48507017a31b6a0c7a00636b3c69687d79ec6bb0b", "0.3.5--py39he88f293_0": "sha256:c63858b6d3b6a6a1c6ec2523aadcfcf0eeecd43b903ac1b9db6f45b09d9db407"}, "docker": "quay.io/biocontainers/superintervals", "aliases": {"cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/superintervals.
singularity registry hpc automated addition for superintervals
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/superintervals
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/superintervals:0.3.5--py39he88f293_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/superintervals/0.3.5--py39he88f293_0
$ module help quay.io/biocontainers/superintervals/0.3.5--py39he88f293_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### superintervals-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### superintervals-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### superintervals-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### superintervals-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### superintervals-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### superintervals-inspect-deffile:

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