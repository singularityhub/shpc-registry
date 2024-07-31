---
layout: container
name:  "quay.io/biocontainers/cogent3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cogent3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cogent3/container.yaml"
updated_at: "2024-07-31 03:04:21.377818"
latest: "2024.7.19a1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cogent3"
aliases:
 - "numba"
 - "pycc"
 - "tqdm"
 - "chardetect"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "2022.8.24a1--pyhdfd78af_0"
 - "2023.7.18a1--pyhdfd78af_0"
 - "2023.9.22a1--pyhdfd78af_0"
 - "2023.12.15a1--pyhdfd78af_0"
 - "2024.2.5a1--pyhdfd78af_0"
 - "2024.5.7a1--pyhdfd78af_0"
 - "2024.7.19a1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cogent3"
config: {"url": "https://biocontainers.pro/tools/cogent3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cogent3", "latest": {"2024.7.19a1--pyhdfd78af_0": "sha256:dfb72c1dd4b13691b90dbf1d1cb844f9ea4863a1cf1c1cf1f665d73cbd73e34c"}, "tags": {"2022.8.24a1--pyhdfd78af_0": "sha256:1b0138ed723f6016e7ecd6f1fd5c459ca5f1aba1383c448d80d5271e8cdd99fd", "2023.7.18a1--pyhdfd78af_0": "sha256:91a8398da9748f6a96f103302338c0e9ea458b49091e374c92de649ac01c02a7", "2023.9.22a1--pyhdfd78af_0": "sha256:0a6e0ad7e0508b05159fee92441b5f21904d79274075c6066d1944c14f821bc0", "2023.12.15a1--pyhdfd78af_0": "sha256:7f6d49fe8136331710d09211d1370806563150ad6b93f58158afa41b1965f4c2", "2024.2.5a1--pyhdfd78af_0": "sha256:43cf4f70135cf212f705dfb035f93fb6c6ed39f7274983d9ee3ea85a00f91338", "2024.5.7a1--pyhdfd78af_0": "sha256:11dba48c768e4b0886e5c7c723ac7280e7121afec36a8db8998b99a7dcdf7885", "2024.7.19a1--pyhdfd78af_0": "sha256:dfb72c1dd4b13691b90dbf1d1cb844f9ea4863a1cf1c1cf1f665d73cbd73e34c"}, "docker": "quay.io/biocontainers/cogent3", "aliases": {"numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "tqdm": "/usr/local/bin/tqdm", "chardetect": "/usr/local/bin/chardetect", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cogent3.
singularity registry hpc automated addition for cogent3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cogent3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cogent3:2024.7.19a1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cogent3/2024.7.19a1--pyhdfd78af_0
$ module help quay.io/biocontainers/cogent3/2024.7.19a1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cogent3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cogent3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cogent3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cogent3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cogent3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cogent3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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