---
layout: container
name:  "quay.io/biocontainers/sqlalchemy-datatables"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sqlalchemy-datatables/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sqlalchemy-datatables/container.yaml"
updated_at: "2023-11-11 03:00:01.536797"
latest: "2.0.1--py_0"
container_url: "https://biocontainers.pro/tools/sqlalchemy-datatables"
aliases:
 - "2to3-3.4"
 - "easy_install-3.4"
 - "idle3.4"
 - "pydoc3.4"
 - "python3.4"
 - "python3.4-config"
 - "python3.4m"
 - "python3.4m-config"
 - "pyvenv-3.4"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
 - "pyvenv"
versions:
 - "2.0.1--py_0"
description: "shpc-registry automated BioContainers addition for sqlalchemy-datatables"
config: {"url": "https://biocontainers.pro/tools/sqlalchemy-datatables", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sqlalchemy-datatables", "latest": {"2.0.1--py_0": "sha256:a14aff673c597f6457946731f8a6acc336e9ba247d9d23fc01804f13e26abfa6"}, "tags": {"2.0.1--py_0": "sha256:a14aff673c597f6457946731f8a6acc336e9ba247d9d23fc01804f13e26abfa6"}, "docker": "quay.io/biocontainers/sqlalchemy-datatables", "aliases": {"2to3-3.4": "/usr/local/bin/2to3-3.4", "easy_install-3.4": "/usr/local/bin/easy_install-3.4", "idle3.4": "/usr/local/bin/idle3.4", "pydoc3.4": "/usr/local/bin/pydoc3.4", "python3.4": "/usr/local/bin/python3.4", "python3.4-config": "/usr/local/bin/python3.4-config", "python3.4m": "/usr/local/bin/python3.4m", "python3.4m-config": "/usr/local/bin/python3.4m-config", "pyvenv-3.4": "/usr/local/bin/pyvenv-3.4", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sqlalchemy-datatables.
shpc-registry automated BioContainers addition for sqlalchemy-datatables
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sqlalchemy-datatables
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sqlalchemy-datatables:2.0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sqlalchemy-datatables/2.0.1--py_0
$ module help quay.io/biocontainers/sqlalchemy-datatables/2.0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sqlalchemy-datatables-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sqlalchemy-datatables-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sqlalchemy-datatables-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sqlalchemy-datatables-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sqlalchemy-datatables-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sqlalchemy-datatables-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.4

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.4

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.4

```bash
$ singularity exec <container> /usr/local/bin/idle3.4
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.4

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.4
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4

```bash
$ singularity exec <container> /usr/local/bin/python3.4
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4-config

```bash
$ singularity exec <container> /usr/local/bin/python3.4-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4m

```bash
$ singularity exec <container> /usr/local/bin/python3.4m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.4m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.4

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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