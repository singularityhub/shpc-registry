---
layout: container
name:  "quay.io/biocontainers/dysgu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dysgu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dysgu/container.yaml"
updated_at: "2025-04-09 03:51:27.480497"
latest: "1.8.2--py39he88f293_0"
container_url: "https://biocontainers.pro/tools/dysgu"
aliases:
 - "dysgu"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "normalizer"
 - "f2py3.10"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.3.16--py310h0de0465_0"
 - "1.4.0--py310h770aed0_0"
 - "1.5.0--py310h770aed0_1"
 - "1.4.2--py310h770aed0_0"
 - "1.6.0--py310h770aed0_0"
 - "1.6.1--py310h770aed0_0"
 - "1.6.2--py310h770aed0_0"
 - "1.6.5--py311h0395e44_1"
 - "1.6.6--py39h0c37024_0"
 - "1.6.7--py38hbf64fdb_0"
 - "1.7.0--py310h0b8f69d_1"
 - "1.8.0--py311h72a6ae7_0"
 - "1.8.2--py39he88f293_0"
description: "singularity registry hpc automated addition for dysgu"
config: {"url": "https://biocontainers.pro/tools/dysgu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dysgu", "latest": {"1.8.2--py39he88f293_0": "sha256:0421911fa6e97fe8c141ced122901e09e509bb24af7a94c771a6f3de8635f353"}, "tags": {"1.3.16--py310h0de0465_0": "sha256:d5b234ea95b6e111d944c889022654eac052b585c89ba1831e1c481f96517894", "1.4.0--py310h770aed0_0": "sha256:e85a4699fc442ab367689e5e07f396c86720eac0d7167e81541b392072b8da0c", "1.5.0--py310h770aed0_1": "sha256:64c659cee47ed1066e6cb5c3bd250232578d9523e3f2c4db29831616007e6bec", "1.4.2--py310h770aed0_0": "sha256:f732349bdef8c79e4ff553babe86ed3506cf9318f7f092db4941be0d43850e18", "1.6.0--py310h770aed0_0": "sha256:3c31f3674c0b7b94f75a511275ba59bb18c434aac798001983ff6722cb73c014", "1.6.1--py310h770aed0_0": "sha256:60e17cb0471120ee0b72d854e421108b69a7b3015d797670d0609ec124be7161", "1.6.2--py310h770aed0_0": "sha256:68e7414538c175ceddab05c5a8e402ca5e5cacb545a3d7f4ba4a67146a4d6ac5", "1.6.5--py311h0395e44_1": "sha256:0f67e81e14af9215d418af5d0de94eca8dedcdfd51d11b676e0d96e2241f940e", "1.6.6--py39h0c37024_0": "sha256:d7b99232d18fdab51bf37fc85bbfa4ca49ca6f4651b045483af99374815bb8bd", "1.6.7--py38hbf64fdb_0": "sha256:29a6f39018a6933fb1352a55ec1eafcd3ff4bdae85e2823d624645d46c1b2a75", "1.7.0--py310h0b8f69d_1": "sha256:52963a73f9a0b2a73936bfa609b659c023b9fc92b662c8afd94ef4adfb8ff7d1", "1.8.0--py311h72a6ae7_0": "sha256:4da6ae29afef762bbd3276ec8f1f3d328d2a73e5590e1ed8a6e9707712f93fab", "1.8.2--py39he88f293_0": "sha256:0421911fa6e97fe8c141ced122901e09e509bb24af7a94c771a6f3de8635f353"}, "docker": "quay.io/biocontainers/dysgu", "aliases": {"dysgu": "/usr/local/bin/dysgu", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dysgu.
singularity registry hpc automated addition for dysgu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dysgu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dysgu:1.8.2--py39he88f293_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dysgu/1.8.2--py39he88f293_0
$ module help quay.io/biocontainers/dysgu/1.8.2--py39he88f293_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dysgu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dysgu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dysgu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dysgu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dysgu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dysgu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dysgu

```bash
$ singularity exec <container> /usr/local/bin/dysgu
$ podman run --it --rm --entrypoint /usr/local/bin/dysgu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dysgu   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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