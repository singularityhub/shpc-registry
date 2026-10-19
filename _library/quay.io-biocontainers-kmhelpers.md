---
layout: container
name:  "quay.io/biocontainers/kmhelpers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmhelpers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmhelpers/container.yaml"
updated_at: "2026-10-19 08:12:06.282488"
latest: "0.7.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/kmhelpers"
aliases:
 - "kh"
 - "kmhelpers"
 - "kmindex"
 - "kmindex-server"
 - "kmtricks"
 - "ntcard"
 - "nthll"
 - "cffi-gen-src"
 - "fc-genconf"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
versions:
 - "0.7.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for kmhelpers"
config: {"url": "https://biocontainers.pro/tools/kmhelpers", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmhelpers", "latest": {"0.7.1--pyhdfd78af_0": "sha256:cad0220a3267277979e6d97106b1ca22be4b4f06d6ae21764d717dbc91d936e0"}, "tags": {"0.7.1--pyhdfd78af_0": "sha256:cad0220a3267277979e6d97106b1ca22be4b4f06d6ae21764d717dbc91d936e0"}, "docker": "quay.io/biocontainers/kmhelpers", "aliases": {"kh": "/usr/local/bin/kh", "kmhelpers": "/usr/local/bin/kmhelpers", "kmindex": "/usr/local/bin/kmindex", "kmindex-server": "/usr/local/bin/kmindex-server", "kmtricks": "/usr/local/bin/kmtricks", "ntcard": "/usr/local/bin/ntcard", "nthll": "/usr/local/bin/nthll", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "fc-genconf": "/usr/local/bin/fc-genconf", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmhelpers.
singularity registry hpc automated addition for kmhelpers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmhelpers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmhelpers:0.7.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmhelpers/0.7.1--pyhdfd78af_0
$ module help quay.io/biocontainers/kmhelpers/0.7.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmhelpers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmhelpers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmhelpers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmhelpers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmhelpers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmhelpers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kh

```bash
$ singularity exec <container> /usr/local/bin/kh
$ podman run --it --rm --entrypoint /usr/local/bin/kh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmhelpers

```bash
$ singularity exec <container> /usr/local/bin/kmhelpers
$ podman run --it --rm --entrypoint /usr/local/bin/kmhelpers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmhelpers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmindex

```bash
$ singularity exec <container> /usr/local/bin/kmindex
$ podman run --it --rm --entrypoint /usr/local/bin/kmindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmindex-server

```bash
$ singularity exec <container> /usr/local/bin/kmindex-server
$ podman run --it --rm --entrypoint /usr/local/bin/kmindex-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmindex-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmtricks

```bash
$ singularity exec <container> /usr/local/bin/kmtricks
$ podman run --it --rm --entrypoint /usr/local/bin/kmtricks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmtricks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntcard

```bash
$ singularity exec <container> /usr/local/bin/ntcard
$ podman run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nthll

```bash
$ singularity exec <container> /usr/local/bin/nthll
$ podman run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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