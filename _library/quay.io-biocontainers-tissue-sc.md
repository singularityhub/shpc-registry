---
layout: container
name:  "quay.io/biocontainers/tissue-sc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tissue-sc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tissue-sc/container.yaml"
updated_at: "2026-10-26 00:23:01.138448"
latest: "1.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tissue-sc"
aliases:
 - "ome-zarr-models"
 - "ome_zarr"
 - "pyct"
 - "scikit-build"
 - "scikit-build-core"
 - "xrspatial"
 - "pyproj"
 - "gdal"
 - "session-info2"
 - "session-info"
 - "gdal_footprint"
 - "minigzip"
 - "minizip"
 - "sozip"
 - "cffi-gen-src"
 - "zarr"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "dotenv"
 - "bsdunzip"
 - "tiff2fsspec"
 - "gdal_create"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "tiffcomment"
 - "cbrunsli"
 - "dask"
 - "dbrunsli"
versions:
 - "1.0.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for tissue-sc"
config: {"url": "https://biocontainers.pro/tools/tissue-sc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tissue-sc", "latest": {"1.0.1--pyhdfd78af_0": "sha256:dbb7786081d5edf0b89c0078bf12832a567c2b57469f595a65bc52ef8952c615"}, "tags": {"1.0.1--pyhdfd78af_0": "sha256:dbb7786081d5edf0b89c0078bf12832a567c2b57469f595a65bc52ef8952c615"}, "docker": "quay.io/biocontainers/tissue-sc", "aliases": {"ome-zarr-models": "/usr/local/bin/ome-zarr-models", "ome_zarr": "/usr/local/bin/ome_zarr", "pyct": "/usr/local/bin/pyct", "scikit-build": "/usr/local/bin/scikit-build", "scikit-build-core": "/usr/local/bin/scikit-build-core", "xrspatial": "/usr/local/bin/xrspatial", "pyproj": "/usr/local/bin/pyproj", "gdal": "/usr/local/bin/gdal", "session-info2": "/usr/local/bin/session-info2", "session-info": "/usr/local/bin/session-info", "gdal_footprint": "/usr/local/bin/gdal_footprint", "minigzip": "/usr/local/bin/minigzip", "minizip": "/usr/local/bin/minizip", "sozip": "/usr/local/bin/sozip", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "zarr": "/usr/local/bin/zarr", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "dotenv": "/usr/local/bin/dotenv", "bsdunzip": "/usr/local/bin/bsdunzip", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "gdal_create": "/usr/local/bin/gdal_create", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "tiffcomment": "/usr/local/bin/tiffcomment", "cbrunsli": "/usr/local/bin/cbrunsli", "dask": "/usr/local/bin/dask", "dbrunsli": "/usr/local/bin/dbrunsli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tissue-sc.
singularity registry hpc automated addition for tissue-sc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tissue-sc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tissue-sc:1.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tissue-sc/1.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/tissue-sc/1.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tissue-sc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tissue-sc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tissue-sc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tissue-sc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tissue-sc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tissue-sc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ome-zarr-models

```bash
$ singularity exec <container> /usr/local/bin/ome-zarr-models
$ podman run --it --rm --entrypoint /usr/local/bin/ome-zarr-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ome-zarr-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ome_zarr

```bash
$ singularity exec <container> /usr/local/bin/ome_zarr
$ podman run --it --rm --entrypoint /usr/local/bin/ome_zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ome_zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyct

```bash
$ singularity exec <container> /usr/local/bin/pyct
$ podman run --it --rm --entrypoint /usr/local/bin/pyct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scikit-build

```bash
$ singularity exec <container> /usr/local/bin/scikit-build
$ podman run --it --rm --entrypoint /usr/local/bin/scikit-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scikit-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scikit-build-core

```bash
$ singularity exec <container> /usr/local/bin/scikit-build-core
$ podman run --it --rm --entrypoint /usr/local/bin/scikit-build-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scikit-build-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrspatial

```bash
$ singularity exec <container> /usr/local/bin/xrspatial
$ podman run --it --rm --entrypoint /usr/local/bin/xrspatial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xrspatial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyproj

```bash
$ singularity exec <container> /usr/local/bin/pyproj
$ podman run --it --rm --entrypoint /usr/local/bin/pyproj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyproj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal

```bash
$ singularity exec <container> /usr/local/bin/gdal
$ podman run --it --rm --entrypoint /usr/local/bin/gdal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info2

```bash
$ singularity exec <container> /usr/local/bin/session-info2
$ podman run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info

```bash
$ singularity exec <container> /usr/local/bin/session-info
$ podman run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_footprint

```bash
$ singularity exec <container> /usr/local/bin/gdal_footprint
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_footprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_footprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minigzip

```bash
$ singularity exec <container> /usr/local/bin/minigzip
$ podman run --it --rm --entrypoint /usr/local/bin/minigzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minigzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minizip

```bash
$ singularity exec <container> /usr/local/bin/minizip
$ podman run --it --rm --entrypoint /usr/local/bin/minizip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minizip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sozip

```bash
$ singularity exec <container> /usr/local/bin/sozip
$ podman run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zarr

```bash
$ singularity exec <container> /usr/local/bin/zarr
$ podman run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_create

```bash
$ singularity exec <container> /usr/local/bin/gdal_create
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_viewshed

```bash
$ singularity exec <container> /usr/local/bin/gdal_viewshed
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_viewshed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_viewshed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmdiminfo

```bash
$ singularity exec <container> /usr/local/bin/gdalmdiminfo
$ podman run --it --rm --entrypoint /usr/local/bin/gdalmdiminfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalmdiminfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmdimtranslate

```bash
$ singularity exec <container> /usr/local/bin/gdalmdimtranslate
$ podman run --it --rm --entrypoint /usr/local/bin/gdalmdimtranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalmdimtranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcomment

```bash
$ singularity exec <container> /usr/local/bin/tiffcomment
$ podman run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbrunsli

```bash
$ singularity exec <container> /usr/local/bin/cbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbrunsli

```bash
$ singularity exec <container> /usr/local/bin/dbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
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