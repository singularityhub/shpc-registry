---
layout: container
name:  "quay.io/biocontainers/testfixtures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/testfixtures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/testfixtures/container.yaml"
updated_at: "2023-06-12 03:41:54.275307"
latest: "4.8.0--py35_0"
container_url: "https://biocontainers.pro/tools/testfixtures"
aliases:
 - "easy_install-3.5"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
 - "tclsh8.5"
versions:
 - "4.8.0--py35_0"
description: "shpc-registry automated BioContainers addition for testfixtures"
config: {"url": "https://biocontainers.pro/tools/testfixtures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for testfixtures", "latest": {"4.8.0--py35_0": "sha256:d1ff3b57055a3c07f35e0ac9739ccc8564ca656e0c81b29a6f027de78fcf192a"}, "tags": {"4.8.0--py35_0": "sha256:d1ff3b57055a3c07f35e0ac9739ccc8564ca656e0c81b29a6f027de78fcf192a"}, "docker": "quay.io/biocontainers/testfixtures", "aliases": {"easy_install-3.5": "/usr/local/bin/easy_install-3.5", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "tclsh8.5": "/usr/local/bin/tclsh8.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/testfixtures.
shpc-registry automated BioContainers addition for testfixtures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/testfixtures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/testfixtures:4.8.0--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/testfixtures/4.8.0--py35_0
$ module help quay.io/biocontainers/testfixtures/4.8.0--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### testfixtures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### testfixtures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### testfixtures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### testfixtures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### testfixtures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### testfixtures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### easy_install-3.5

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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