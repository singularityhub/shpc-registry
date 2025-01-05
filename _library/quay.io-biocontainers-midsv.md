---
layout: container
name:  "quay.io/biocontainers/midsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/midsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/midsv/container.yaml"
updated_at: "2025-01-05 03:33:38.838214"
latest: "0.11.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/midsv"
aliases:
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.8.2--pyhdfd78af_0"
 - "0.8.4--pyhdfd78af_0"
 - "0.9.5--pyhdfd78af_0"
 - "0.10.0--pyhdfd78af_0"
 - "0.10.2--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_0"
 - "0.11.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for midsv"
config: {"url": "https://biocontainers.pro/tools/midsv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for midsv", "latest": {"0.11.1--pyhdfd78af_0": "sha256:755d92a3e284b6f68e0eed128977f146d4f46acaf10a7482464c55f9e1a85f2f"}, "tags": {"0.8.2--pyhdfd78af_0": "sha256:b6afdfda084882fadf693f739c637d37d1e7d7786b4027905ce157b449079dd1", "0.8.4--pyhdfd78af_0": "sha256:700be1a0eb628a9a5f08f75fb4698e500b583cae07ca3f12c45df1c9140a63c1", "0.9.5--pyhdfd78af_0": "sha256:fc610e95999d710e0e7a27c7e534c21eadc2b35ceaa9ae076a3f87b737a904da", "0.10.0--pyhdfd78af_0": "sha256:577db0e7e914722f26de4dfd9557947e5f59d9be8e249c5bf5479f4aed48ba33", "0.10.2--pyhdfd78af_0": "sha256:26adcd118562d72860e82b250e3f3d621fbf7dfcdb0e81beca95d0569fc9e795", "0.11.0--pyhdfd78af_0": "sha256:01f1d20988ec5572937a2d76f02eda1a27e29160bd281dbd4d36665f3895cee3", "0.11.1--pyhdfd78af_0": "sha256:755d92a3e284b6f68e0eed128977f146d4f46acaf10a7482464c55f9e1a85f2f"}, "docker": "quay.io/biocontainers/midsv", "aliases": {"2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/midsv.
singularity registry hpc automated addition for midsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/midsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/midsv:0.11.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/midsv/0.11.1--pyhdfd78af_0
$ module help quay.io/biocontainers/midsv/0.11.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### midsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### midsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### midsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### midsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### midsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### midsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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