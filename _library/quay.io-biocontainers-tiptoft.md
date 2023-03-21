---
layout: container
name:  "quay.io/biocontainers/tiptoft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tiptoft/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tiptoft/container.yaml"
updated_at: "2023-03-21 03:17:45.666946"
latest: "1.0.2--py37h8902056_3"
container_url: "https://biocontainers.pro/tools/tiptoft"
aliases:
 - "tiptoft"
 - "tiptoft_database_downloader"
 - "fastaq"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
versions:
 - "1.0.2--py37h8902056_3"
description: "shpc-registry automated BioContainers addition for tiptoft"
config: {"url": "https://biocontainers.pro/tools/tiptoft", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tiptoft", "latest": {"1.0.2--py37h8902056_3": "sha256:11dc1f20f4f59a31285ab7380b91c1eb286ba31bed5d3cdc9fdf18f51a7e81f5"}, "tags": {"1.0.2--py37h8902056_3": "sha256:11dc1f20f4f59a31285ab7380b91c1eb286ba31bed5d3cdc9fdf18f51a7e81f5"}, "docker": "quay.io/biocontainers/tiptoft", "aliases": {"tiptoft": "/usr/local/bin/tiptoft", "tiptoft_database_downloader": "/usr/local/bin/tiptoft_database_downloader", "fastaq": "/usr/local/bin/fastaq", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tiptoft.
shpc-registry automated BioContainers addition for tiptoft
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tiptoft
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tiptoft:1.0.2--py37h8902056_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tiptoft/1.0.2--py37h8902056_3
$ module help quay.io/biocontainers/tiptoft/1.0.2--py37h8902056_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tiptoft-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tiptoft-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tiptoft-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tiptoft-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tiptoft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tiptoft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tiptoft

```bash
$ singularity exec <container> /usr/local/bin/tiptoft
$ podman run --it --rm --entrypoint /usr/local/bin/tiptoft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiptoft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiptoft_database_downloader

```bash
$ singularity exec <container> /usr/local/bin/tiptoft_database_downloader
$ podman run --it --rm --entrypoint /usr/local/bin/tiptoft_database_downloader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiptoft_database_downloader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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