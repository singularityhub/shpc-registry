---
layout: container
name:  "quay.io/biocontainers/borf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/borf/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/borf/container.yaml"
updated_at: "2022-10-29 05:47:31.863923"
latest: "1.2--py_0"
container_url: "https://biocontainers.pro/tools/borf"
aliases:
 - "borf"
 - "2to3-3.7"
 - "assistant"
 - "canbusutil"
 - "certutil"
 - "chardetect"
 - "compile-et.pl"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "dbus-cleanup-sockets"
versions:
 - "1.2--py_0"
description: "shpc-registry automated BioContainers addition for borf"
config: {"url": "https://biocontainers.pro/tools/borf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for borf", "latest": {"1.2--py_0": "sha256:a5f946e2897c7d3e813673b93cb0c15811b2e5d8472af24c4a1798b8930ed593"}, "tags": {"1.2--py_0": "sha256:a5f946e2897c7d3e813673b93cb0c15811b2e5d8472af24c4a1798b8930ed593"}, "docker": "quay.io/biocontainers/borf", "aliases": {"borf": "/usr/local/bin/borf", "2to3-3.7": "/usr/local/bin/2to3-3.7", "assistant": "/usr/local/bin/assistant", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "chardetect": "/usr/local/bin/chardetect", "compile-et.pl": "/usr/local/bin/compile-et.pl", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/borf.
shpc-registry automated BioContainers addition for borf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/borf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/borf:1.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/borf/1.2--py_0
$ module help quay.io/biocontainers/borf/1.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### borf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### borf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### borf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### borf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### borf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### borf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### borf

```bash
$ singularity exec <container> /usr/local/bin/borf
$ podman run --it --rm --entrypoint /usr/local/bin/borf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/borf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dbus-cleanup-sockets

```bash
$ singularity exec <container> /usr/local/bin/dbus-cleanup-sockets
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
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