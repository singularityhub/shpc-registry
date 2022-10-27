---
layout: container
name:  "quay.io/biocontainers/duet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/duet/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/duet/container.yaml"
updated_at: "2022-10-27 00:53:27.535818"
latest: "0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/duet"
aliases:
 - "clair3.py"
 - "cuteSV"
 - "duet"
 - "libclair3.c"
 - "libclair3.cpython-36m-x86_64-linux-gnu.so"
 - "libclair3.o"
 - "libclair3.so"
 - "libpypy3-c.so.debug"
 - "longphase"
 - "ngmlr"
 - "pypy"
 - "pypy3"
 - "pypy3.6"
 - "run_clair3.sh"
 - "svim"
versions:
 - "0.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for duet"
config: {"url": "https://biocontainers.pro/tools/duet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for duet", "latest": {"0.5--pyhdfd78af_0": "sha256:ea0c1b422b8a9d812bc429e77ed8c45724e1a13fd51f981eaf1224be4e583920"}, "tags": {"0.5--pyhdfd78af_0": "sha256:ea0c1b422b8a9d812bc429e77ed8c45724e1a13fd51f981eaf1224be4e583920"}, "docker": "quay.io/biocontainers/duet", "aliases": {"clair3.py": "/usr/local/bin/clair3.py", "cuteSV": "/usr/local/bin/cuteSV", "duet": "/usr/local/bin/duet", "libclair3.c": "/usr/local/bin/libclair3.c", "libclair3.cpython-36m-x86_64-linux-gnu.so": "/usr/local/bin/libclair3.cpython-36m-x86_64-linux-gnu.so", "libclair3.o": "/usr/local/bin/libclair3.o", "libclair3.so": "/usr/local/bin/libclair3.so", "libpypy3-c.so.debug": "/usr/local/bin/libpypy3-c.so.debug", "longphase": "/usr/local/bin/longphase", "ngmlr": "/usr/local/bin/ngmlr", "pypy": "/usr/local/bin/pypy", "pypy3": "/usr/local/bin/pypy3", "pypy3.6": "/usr/local/bin/pypy3.6", "run_clair3.sh": "/usr/local/bin/run_clair3.sh", "svim": "/usr/local/bin/svim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/duet.
shpc-registry automated BioContainers addition for duet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/duet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/duet:0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/duet/0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/duet/0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### duet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### duet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### duet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### duet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### duet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### duet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clair3.py

```bash
$ singularity exec <container> /usr/local/bin/clair3.py
$ podman run --it --rm --entrypoint /usr/local/bin/clair3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clair3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuteSV

```bash
$ singularity exec <container> /usr/local/bin/cuteSV
$ podman run --it --rm --entrypoint /usr/local/bin/cuteSV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuteSV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duet

```bash
$ singularity exec <container> /usr/local/bin/duet
$ podman run --it --rm --entrypoint /usr/local/bin/duet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libclair3.c

```bash
$ singularity exec <container> /usr/local/bin/libclair3.c
$ podman run --it --rm --entrypoint /usr/local/bin/libclair3.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libclair3.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libclair3.cpython-36m-x86_64-linux-gnu.so

```bash
$ singularity exec <container> /usr/local/bin/libclair3.cpython-36m-x86_64-linux-gnu.so
$ podman run --it --rm --entrypoint /usr/local/bin/libclair3.cpython-36m-x86_64-linux-gnu.so   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libclair3.cpython-36m-x86_64-linux-gnu.so   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libclair3.o

```bash
$ singularity exec <container> /usr/local/bin/libclair3.o
$ podman run --it --rm --entrypoint /usr/local/bin/libclair3.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libclair3.o   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libclair3.so

```bash
$ singularity exec <container> /usr/local/bin/libclair3.so
$ podman run --it --rm --entrypoint /usr/local/bin/libclair3.so   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libclair3.so   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libpypy3-c.so.debug

```bash
$ singularity exec <container> /usr/local/bin/libpypy3-c.so.debug
$ podman run --it --rm --entrypoint /usr/local/bin/libpypy3-c.so.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libpypy3-c.so.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### longphase

```bash
$ singularity exec <container> /usr/local/bin/longphase
$ podman run --it --rm --entrypoint /usr/local/bin/longphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longphase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngmlr

```bash
$ singularity exec <container> /usr/local/bin/ngmlr
$ podman run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy

```bash
$ singularity exec <container> /usr/local/bin/pypy
$ podman run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3

```bash
$ singularity exec <container> /usr/local/bin/pypy3
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3.6

```bash
$ singularity exec <container> /usr/local/bin/pypy3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_clair3.sh

```bash
$ singularity exec <container> /usr/local/bin/run_clair3.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_clair3.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_clair3.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svim

```bash
$ singularity exec <container> /usr/local/bin/svim
$ podman run --it --rm --entrypoint /usr/local/bin/svim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svim   -v ${PWD} -w ${PWD} <container> -c " $@"
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