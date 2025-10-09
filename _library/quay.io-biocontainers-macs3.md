---
layout: container
name:  "quay.io/biocontainers/macs3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/macs3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/macs3/container.yaml"
updated_at: "2025-10-09 04:44:04.215684"
latest: "3.0.3--py39h0699b22_0"
container_url: "https://biocontainers.pro/tools/macs3"
aliases:
 - "macs3"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "3.0.1--py312he4a0461_0"
 - "3.0.1--py39h3d4b85c_2"
 - "3.0.1--py310h83093d7_2"
 - "3.0.1--py312he57d009_3"
 - "3.0.2--py311h0152c62_1"
 - "3.0.2--py310h397c9d8_2"
 - "3.0.3--py39h0699b22_0"
description: "singularity registry hpc automated addition for macs3"
config: {"url": "https://biocontainers.pro/tools/macs3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for macs3", "latest": {"3.0.3--py39h0699b22_0": "sha256:fe20a3fa6b6a00d0d2f2bf7464e4e732367d00ea6f4f699abbd6fcfee2f12627"}, "tags": {"3.0.1--py312he4a0461_0": "sha256:8afe27c70bf2c3bcebd06f8819e014aba71565066d69e188817006df1e46f022", "3.0.1--py39h3d4b85c_2": "sha256:d470b75937959cf328b182eef2675d3323af120549890f50de4697535f30b115", "3.0.1--py310h83093d7_2": "sha256:30f06ce881286e805d466eb93db7c0257eb25bf4a6001e6a1b2c0078f9eae1d0", "3.0.1--py312he57d009_3": "sha256:27518d25b581f0a9d2144aa4109c5f0e90bd3cb5b6eea14912ef0fcfe5ab8311", "3.0.2--py311h0152c62_1": "sha256:f0c947e5436392a981b3b08194d908abc3475e3b1e460fdef0ca5a26dc49c9f5", "3.0.2--py310h397c9d8_2": "sha256:a0c053426263b8788df7d43c5d07fd43b5f121b209fb8ee52d67e71273e2fa69", "3.0.3--py39h0699b22_0": "sha256:fe20a3fa6b6a00d0d2f2bf7464e4e732367d00ea6f4f699abbd6fcfee2f12627"}, "docker": "quay.io/biocontainers/macs3", "aliases": {"macs3": "/usr/local/bin/macs3", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/macs3.
singularity registry hpc automated addition for macs3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/macs3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/macs3:3.0.3--py39h0699b22_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/macs3/3.0.3--py39h0699b22_0
$ module help quay.io/biocontainers/macs3/3.0.3--py39h0699b22_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### macs3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### macs3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### macs3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### macs3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### macs3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### macs3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### macs3

```bash
$ singularity exec <container> /usr/local/bin/macs3
$ podman run --it --rm --entrypoint /usr/local/bin/macs3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macs3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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