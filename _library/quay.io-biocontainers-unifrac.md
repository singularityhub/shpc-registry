---
layout: container
name:  "quay.io/biocontainers/unifrac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unifrac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unifrac/container.yaml"
updated_at: "2024-08-12 03:00:28.059549"
latest: "1.3--py38hbff2b2d_0"
container_url: "https://biocontainers.pro/tools/unifrac"
aliases:
 - "bp"
 - "faithpd"
 - "ssu"
 - "biom"
 - "doesitcache"
 - "ipython3"
 - "ipython"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "py.test"
 - "pytest"
 - "natsort"
versions:
 - "1.1.1--py310h79ef01b_1"
 - "1.2--py39hbf8eff0_0"
 - "1.3--py38hbff2b2d_0"
 - "1.3--py39hbf8eff0_0"
 - "1.2--py310h1425a21_0"
 - "1.1.1--py36h40b2fa4_1"
description: "shpc-registry automated BioContainers addition for unifrac"
config: {"url": "https://biocontainers.pro/tools/unifrac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unifrac", "latest": {"1.3--py38hbff2b2d_0": "sha256:737b60feec4e345a4c43aface359504b77bfddd2bb35a09f3d26e86eae19260e"}, "tags": {"1.1.1--py310h79ef01b_1": "sha256:c5df3127503ce3bad527b4d9316fe4b17edaca6fb7533330d7dcb3c730857b48", "1.2--py39hbf8eff0_0": "sha256:6af66523714f57c20fbfab142c76ce0c05f6a1559030190fa91c4c3268cfaa08", "1.3--py38hbff2b2d_0": "sha256:737b60feec4e345a4c43aface359504b77bfddd2bb35a09f3d26e86eae19260e", "1.3--py39hbf8eff0_0": "sha256:0e34a586b10589f1820dc2d08e6f744da72f3ba72861942b9aff01f9a137ab8b", "1.2--py310h1425a21_0": "sha256:f3f3cd7e598b10483dda64d093982932e51a0a68625c7d42e517a2bb8c61d00c", "1.1.1--py36h40b2fa4_1": "sha256:f7a39d9ffa5d0dd36e796fa8cc52b3c1cc08efe03407342ffce80b4102c128ed"}, "docker": "quay.io/biocontainers/unifrac", "aliases": {"bp": "/usr/local/bin/bp", "faithpd": "/usr/local/bin/faithpd", "ssu": "/usr/local/bin/ssu", "biom": "/usr/local/bin/biom", "doesitcache": "/usr/local/bin/doesitcache", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "natsort": "/usr/local/bin/natsort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unifrac.
shpc-registry automated BioContainers addition for unifrac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unifrac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unifrac:1.3--py38hbff2b2d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unifrac/1.3--py38hbff2b2d_0
$ module help quay.io/biocontainers/unifrac/1.3--py38hbff2b2d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unifrac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unifrac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unifrac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unifrac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unifrac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unifrac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp

```bash
$ singularity exec <container> /usr/local/bin/bp
$ podman run --it --rm --entrypoint /usr/local/bin/bp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faithpd

```bash
$ singularity exec <container> /usr/local/bin/faithpd
$ podman run --it --rm --entrypoint /usr/local/bin/faithpd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faithpd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssu

```bash
$ singularity exec <container> /usr/local/bin/ssu
$ podman run --it --rm --entrypoint /usr/local/bin/ssu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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