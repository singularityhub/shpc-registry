---
layout: container
name:  "quay.io/biocontainers/dodge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dodge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dodge/container.yaml"
updated_at: "2026-01-17 04:17:40.765876"
latest: "1.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dodge"
aliases:
 - "dodge"
 - "dodgedists"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.0--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for dodge"
config: {"url": "https://biocontainers.pro/tools/dodge", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dodge", "latest": {"1.0.1--pyhdfd78af_0": "sha256:87bf47c195f459c61632b6bffc6cb43250d3ce8c3e33faf776db10a621495eef"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:123b8137a9dd4f34682d0c243ed210152226c56236a13cacef13011a16c5d9f6", "1.0.1--pyhdfd78af_0": "sha256:87bf47c195f459c61632b6bffc6cb43250d3ce8c3e33faf776db10a621495eef"}, "docker": "quay.io/biocontainers/dodge", "aliases": {"dodge": "/usr/local/bin/dodge", "dodgedists": "/usr/local/bin/dodgedists", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dodge.
singularity registry hpc automated addition for dodge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dodge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dodge:1.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dodge/1.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/dodge/1.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dodge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dodge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dodge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dodge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dodge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dodge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dodge

```bash
$ singularity exec <container> /usr/local/bin/dodge
$ podman run --it --rm --entrypoint /usr/local/bin/dodge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dodge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dodgedists

```bash
$ singularity exec <container> /usr/local/bin/dodgedists
$ podman run --it --rm --entrypoint /usr/local/bin/dodgedists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dodgedists   -v ${PWD} -w ${PWD} <container> -c " $@"
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