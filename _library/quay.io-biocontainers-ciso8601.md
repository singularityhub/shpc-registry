---
layout: container
name:  "quay.io/biocontainers/ciso8601"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ciso8601/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ciso8601/container.yaml"
updated_at: "2023-12-14 03:13:00.171534"
latest: "1.0.5--py35_0"
container_url: "https://biocontainers.pro/tools/ciso8601"
aliases:
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
 - "tclsh8.5"
 - "wish8.5"
versions:
 - "1.0.5--py35_0"
description: "shpc-registry automated BioContainers addition for ciso8601"
config: {"url": "https://biocontainers.pro/tools/ciso8601", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ciso8601", "latest": {"1.0.5--py35_0": "sha256:3f9849f1a289d8eba60a8acb12feb6a157202c1834e326f4928112a7918e2435"}, "tags": {"1.0.5--py35_0": "sha256:3f9849f1a289d8eba60a8acb12feb6a157202c1834e326f4928112a7918e2435"}, "docker": "quay.io/biocontainers/ciso8601", "aliases": {"2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ciso8601.
shpc-registry automated BioContainers addition for ciso8601
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ciso8601
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ciso8601:1.0.5--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ciso8601/1.0.5--py35_0
$ module help quay.io/biocontainers/ciso8601/1.0.5--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ciso8601-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ciso8601-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ciso8601-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ciso8601-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ciso8601-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ciso8601-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m

```bash
$ singularity exec <container> /usr/local/bin/python3.5m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.5

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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