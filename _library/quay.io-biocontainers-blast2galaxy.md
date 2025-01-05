---
layout: container
name:  "quay.io/biocontainers/blast2galaxy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blast2galaxy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blast2galaxy/container.yaml"
updated_at: "2025-01-05 03:27:35.501530"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/blast2galaxy"
aliases:
 - "bioblend-galaxy-tests"
 - "blast2galaxy"
 - "markdown-it"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "pygmentize"
 - "normalizer"
versions:
 - "0.1.0a1--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for blast2galaxy"
config: {"url": "https://biocontainers.pro/tools/blast2galaxy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for blast2galaxy", "latest": {"1.0.0--pyhdfd78af_0": "sha256:6bfc4eb9d45ebe5cc69c0106d0bed96fd2c1946d8b31a39c1e39db1db50a5fc0"}, "tags": {"0.1.0a1--pyhdfd78af_0": "sha256:35886b2a9f40073cb723be70395bca03a396cfa9e59cc025af9f8d970a55e207", "1.0.0--pyhdfd78af_0": "sha256:6bfc4eb9d45ebe5cc69c0106d0bed96fd2c1946d8b31a39c1e39db1db50a5fc0"}, "docker": "quay.io/biocontainers/blast2galaxy", "aliases": {"bioblend-galaxy-tests": "/usr/local/bin/bioblend-galaxy-tests", "blast2galaxy": "/usr/local/bin/blast2galaxy", "markdown-it": "/usr/local/bin/markdown-it", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "pygmentize": "/usr/local/bin/pygmentize", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blast2galaxy.
singularity registry hpc automated addition for blast2galaxy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blast2galaxy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blast2galaxy:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blast2galaxy/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/blast2galaxy/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blast2galaxy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blast2galaxy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blast2galaxy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blast2galaxy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blast2galaxy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blast2galaxy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioblend-galaxy-tests

```bash
$ singularity exec <container> /usr/local/bin/bioblend-galaxy-tests
$ podman run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2galaxy

```bash
$ singularity exec <container> /usr/local/bin/blast2galaxy
$ podman run --it --rm --entrypoint /usr/local/bin/blast2galaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2galaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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