---
layout: container
name:  "quay.io/biocontainers/nordic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nordic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nordic/container.yaml"
updated_at: "2024-10-16 03:14:52.133181"
latest: "2.4.4--py38hc387825_0"
container_url: "https://biocontainers.pro/tools/nordic"
aliases:
 - "bonesis-attractors"
 - "bonesis-reprogramming"
 - "bonesis-utils"
 - "clasp"
 - "clingo"
 - "concat"
 - "gct2gctx"
 - "gctx2gct"
 - "gringo"
 - "lpconvert"
 - "mpbn"
 - "mpbn-sim"
 - "qnorm"
 - "reify"
 - "subset"
 - "h5fuse.sh"
 - "h5delete"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "numba"
 - "hb-info"
 - "diffimg"
 - "delaunay"
 - "gts-config"
 - "gts2dxf"
 - "gts2oogl"
 - "gts2stl"
 - "gtscheck"
 - "gtscompare"
 - "gtstemplate"
 - "stl2gts"
 - "transform"
 - "rsvg-convert"
 - "gtk-builder-convert"
 - "gtk-demo"
 - "gtk-query-immodules-2.0"
 - "gtk-update-icon-cache"
 - "acyclic"
 - "bcomps"
versions:
 - "2.4.4--py38hc387825_0"
 - "2.4.4--py39he5231b2_0"
description: "singularity registry hpc automated addition for nordic"
config: {"url": "https://biocontainers.pro/tools/nordic", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nordic", "latest": {"2.4.4--py38hc387825_0": "sha256:3d8d2196e200e6dca8c0f6230e61c5a717384f4bb1669a16cf201cf9e2b61032"}, "tags": {"2.4.4--py38hc387825_0": "sha256:3d8d2196e200e6dca8c0f6230e61c5a717384f4bb1669a16cf201cf9e2b61032", "2.4.4--py39he5231b2_0": "sha256:9e6c5d889a9938a45b08d9040ad2078cb933157c594d9d27db889f77bf51bf3b"}, "docker": "quay.io/biocontainers/nordic", "aliases": {"bonesis-attractors": "/usr/local/bin/bonesis-attractors", "bonesis-reprogramming": "/usr/local/bin/bonesis-reprogramming", "bonesis-utils": "/usr/local/bin/bonesis-utils", "clasp": "/usr/local/bin/clasp", "clingo": "/usr/local/bin/clingo", "concat": "/usr/local/bin/concat", "gct2gctx": "/usr/local/bin/gct2gctx", "gctx2gct": "/usr/local/bin/gctx2gct", "gringo": "/usr/local/bin/gringo", "lpconvert": "/usr/local/bin/lpconvert", "mpbn": "/usr/local/bin/mpbn", "mpbn-sim": "/usr/local/bin/mpbn-sim", "qnorm": "/usr/local/bin/qnorm", "reify": "/usr/local/bin/reify", "subset": "/usr/local/bin/subset", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "h5delete": "/usr/local/bin/h5delete", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "numba": "/usr/local/bin/numba", "hb-info": "/usr/local/bin/hb-info", "diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay", "gts-config": "/usr/local/bin/gts-config", "gts2dxf": "/usr/local/bin/gts2dxf", "gts2oogl": "/usr/local/bin/gts2oogl", "gts2stl": "/usr/local/bin/gts2stl", "gtscheck": "/usr/local/bin/gtscheck", "gtscompare": "/usr/local/bin/gtscompare", "gtstemplate": "/usr/local/bin/gtstemplate", "stl2gts": "/usr/local/bin/stl2gts", "transform": "/usr/local/bin/transform", "rsvg-convert": "/usr/local/bin/rsvg-convert", "gtk-builder-convert": "/usr/local/bin/gtk-builder-convert", "gtk-demo": "/usr/local/bin/gtk-demo", "gtk-query-immodules-2.0": "/usr/local/bin/gtk-query-immodules-2.0", "gtk-update-icon-cache": "/usr/local/bin/gtk-update-icon-cache", "acyclic": "/usr/local/bin/acyclic", "bcomps": "/usr/local/bin/bcomps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nordic.
singularity registry hpc automated addition for nordic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nordic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nordic:2.4.4--py38hc387825_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nordic/2.4.4--py38hc387825_0
$ module help quay.io/biocontainers/nordic/2.4.4--py38hc387825_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nordic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nordic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nordic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nordic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nordic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nordic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bonesis-attractors

```bash
$ singularity exec <container> /usr/local/bin/bonesis-attractors
$ podman run --it --rm --entrypoint /usr/local/bin/bonesis-attractors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bonesis-attractors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bonesis-reprogramming

```bash
$ singularity exec <container> /usr/local/bin/bonesis-reprogramming
$ podman run --it --rm --entrypoint /usr/local/bin/bonesis-reprogramming   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bonesis-reprogramming   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bonesis-utils

```bash
$ singularity exec <container> /usr/local/bin/bonesis-utils
$ podman run --it --rm --entrypoint /usr/local/bin/bonesis-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bonesis-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clasp

```bash
$ singularity exec <container> /usr/local/bin/clasp
$ podman run --it --rm --entrypoint /usr/local/bin/clasp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clasp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clingo

```bash
$ singularity exec <container> /usr/local/bin/clingo
$ podman run --it --rm --entrypoint /usr/local/bin/clingo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clingo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concat

```bash
$ singularity exec <container> /usr/local/bin/concat
$ podman run --it --rm --entrypoint /usr/local/bin/concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gct2gctx

```bash
$ singularity exec <container> /usr/local/bin/gct2gctx
$ podman run --it --rm --entrypoint /usr/local/bin/gct2gctx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gct2gctx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gctx2gct

```bash
$ singularity exec <container> /usr/local/bin/gctx2gct
$ podman run --it --rm --entrypoint /usr/local/bin/gctx2gct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gctx2gct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gringo

```bash
$ singularity exec <container> /usr/local/bin/gringo
$ podman run --it --rm --entrypoint /usr/local/bin/gringo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gringo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lpconvert

```bash
$ singularity exec <container> /usr/local/bin/lpconvert
$ podman run --it --rm --entrypoint /usr/local/bin/lpconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lpconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpbn

```bash
$ singularity exec <container> /usr/local/bin/mpbn
$ podman run --it --rm --entrypoint /usr/local/bin/mpbn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpbn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpbn-sim

```bash
$ singularity exec <container> /usr/local/bin/mpbn-sim
$ podman run --it --rm --entrypoint /usr/local/bin/mpbn-sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpbn-sim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qnorm

```bash
$ singularity exec <container> /usr/local/bin/qnorm
$ podman run --it --rm --entrypoint /usr/local/bin/qnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reify

```bash
$ singularity exec <container> /usr/local/bin/reify
$ podman run --it --rm --entrypoint /usr/local/bin/reify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subset

```bash
$ singularity exec <container> /usr/local/bin/subset
$ podman run --it --rm --entrypoint /usr/local/bin/subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diffimg

```bash
$ singularity exec <container> /usr/local/bin/diffimg
$ podman run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts-config

```bash
$ singularity exec <container> /usr/local/bin/gts-config
$ podman run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2dxf

```bash
$ singularity exec <container> /usr/local/bin/gts2dxf
$ podman run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2oogl

```bash
$ singularity exec <container> /usr/local/bin/gts2oogl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2stl

```bash
$ singularity exec <container> /usr/local/bin/gts2stl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscheck

```bash
$ singularity exec <container> /usr/local/bin/gtscheck
$ podman run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscompare

```bash
$ singularity exec <container> /usr/local/bin/gtscompare
$ podman run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtstemplate

```bash
$ singularity exec <container> /usr/local/bin/gtstemplate
$ podman run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stl2gts

```bash
$ singularity exec <container> /usr/local/bin/stl2gts
$ podman run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transform

```bash
$ singularity exec <container> /usr/local/bin/transform
$ podman run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsvg-convert

```bash
$ singularity exec <container> /usr/local/bin/rsvg-convert
$ podman run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-convert

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-demo

```bash
$ singularity exec <container> /usr/local/bin/gtk-demo
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-2.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-2.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-update-icon-cache

```bash
$ singularity exec <container> /usr/local/bin/gtk-update-icon-cache
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
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