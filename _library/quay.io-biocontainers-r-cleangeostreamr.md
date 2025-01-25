---
layout: container
name:  "quay.io/biocontainers/r-cleangeostreamr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cleangeostreamr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cleangeostreamr/container.yaml"
updated_at: "2025-01-25 03:11:05.769392"
latest: "1.0.0--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-cleangeostreamr"
aliases:
 - "bsdunzip"
 - "curate_chemical_data"
 - "curate_spatial_data"
 - "fitsverify"
 - "gdal_footprint"
 - "minigzip"
 - "minizip"
 - "pandoc-lua"
 - "protoc-25.3.0"
 - "sozip"
 - "git2"
 - "pg_amcheck"
 - "h5tools_test_utils"
 - "gdal_create"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "pdfsig"
 - "pandoc-server"
 - "applygeo"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "geotifcp"
 - "gnmanalyse"
 - "gnmmanage"
 - "kea-config"
 - "listgeo"
 - "makegeo"
 - "pg_verifybackup"
 - "projsync"
 - "gdal-config"
 - "gdal_contour"
 - "gdal_grid"
 - "gdal_rasterize"
versions:
 - "1.0.0--r43hdfd78af_0"
 - "1.0.0--r44hdfd78af_1"
description: "singularity registry hpc automated addition for r-cleangeostreamr"
config: {"url": "https://biocontainers.pro/tools/r-cleangeostreamr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-cleangeostreamr", "latest": {"1.0.0--r44hdfd78af_1": "sha256:cc073d89ec828b75bcfa2c727209a5847eb22ea9ff45c7d4f8b173117854db6a"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:f7490a7d0dbba3746327c781ca879c22c1b684eccaa9b4411261f0def183e08e", "1.0.0--r44hdfd78af_1": "sha256:cc073d89ec828b75bcfa2c727209a5847eb22ea9ff45c7d4f8b173117854db6a"}, "docker": "quay.io/biocontainers/r-cleangeostreamr", "aliases": {"bsdunzip": "/usr/local/bin/bsdunzip", "curate_chemical_data": "/usr/local/bin/curate_chemical_data", "curate_spatial_data": "/usr/local/bin/curate_spatial_data", "fitsverify": "/usr/local/bin/fitsverify", "gdal_footprint": "/usr/local/bin/gdal_footprint", "minigzip": "/usr/local/bin/minigzip", "minizip": "/usr/local/bin/minizip", "pandoc-lua": "/usr/local/bin/pandoc-lua", "protoc-25.3.0": "/usr/local/bin/protoc-25.3.0", "sozip": "/usr/local/bin/sozip", "git2": "/usr/local/bin/git2", "pg_amcheck": "/usr/local/bin/pg_amcheck", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "gdal_create": "/usr/local/bin/gdal_create", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "pdfsig": "/usr/local/bin/pdfsig", "pandoc-server": "/usr/local/bin/pandoc-server", "applygeo": "/usr/local/bin/applygeo", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "geotifcp": "/usr/local/bin/geotifcp", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage", "kea-config": "/usr/local/bin/kea-config", "listgeo": "/usr/local/bin/listgeo", "makegeo": "/usr/local/bin/makegeo", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "projsync": "/usr/local/bin/projsync", "gdal-config": "/usr/local/bin/gdal-config", "gdal_contour": "/usr/local/bin/gdal_contour", "gdal_grid": "/usr/local/bin/gdal_grid", "gdal_rasterize": "/usr/local/bin/gdal_rasterize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cleangeostreamr.
singularity registry hpc automated addition for r-cleangeostreamr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cleangeostreamr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cleangeostreamr:1.0.0--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cleangeostreamr/1.0.0--r44hdfd78af_1
$ module help quay.io/biocontainers/r-cleangeostreamr/1.0.0--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cleangeostreamr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cleangeostreamr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cleangeostreamr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cleangeostreamr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cleangeostreamr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cleangeostreamr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curate_chemical_data

```bash
$ singularity exec <container> /usr/local/bin/curate_chemical_data
$ podman run --it --rm --entrypoint /usr/local/bin/curate_chemical_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curate_chemical_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curate_spatial_data

```bash
$ singularity exec <container> /usr/local/bin/curate_spatial_data
$ podman run --it --rm --entrypoint /usr/local/bin/curate_spatial_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curate_spatial_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsverify

```bash
$ singularity exec <container> /usr/local/bin/fitsverify
$ podman run --it --rm --entrypoint /usr/local/bin/fitsverify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsverify   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-25.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-25.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sozip

```bash
$ singularity exec <container> /usr/local/bin/sozip
$ podman run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_amcheck

```bash
$ singularity exec <container> /usr/local/bin/pg_amcheck
$ podman run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applygeo

```bash
$ singularity exec <container> /usr/local/bin/applygeo
$ podman run --it --rm --entrypoint /usr/local/bin/applygeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applygeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geotifcp

```bash
$ singularity exec <container> /usr/local/bin/geotifcp
$ podman run --it --rm --entrypoint /usr/local/bin/geotifcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geotifcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnmanalyse

```bash
$ singularity exec <container> /usr/local/bin/gnmanalyse
$ podman run --it --rm --entrypoint /usr/local/bin/gnmanalyse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnmanalyse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnmmanage

```bash
$ singularity exec <container> /usr/local/bin/gnmmanage
$ podman run --it --rm --entrypoint /usr/local/bin/gnmmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnmmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kea-config

```bash
$ singularity exec <container> /usr/local/bin/kea-config
$ podman run --it --rm --entrypoint /usr/local/bin/kea-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kea-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### listgeo

```bash
$ singularity exec <container> /usr/local/bin/listgeo
$ podman run --it --rm --entrypoint /usr/local/bin/listgeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/listgeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makegeo

```bash
$ singularity exec <container> /usr/local/bin/makegeo
$ podman run --it --rm --entrypoint /usr/local/bin/makegeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makegeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_verifybackup

```bash
$ singularity exec <container> /usr/local/bin/pg_verifybackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projsync

```bash
$ singularity exec <container> /usr/local/bin/projsync
$ podman run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal-config

```bash
$ singularity exec <container> /usr/local/bin/gdal-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdal-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_contour

```bash
$ singularity exec <container> /usr/local/bin/gdal_contour
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_contour   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_contour   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_grid

```bash
$ singularity exec <container> /usr/local/bin/gdal_grid
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_grid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_grid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_rasterize

```bash
$ singularity exec <container> /usr/local/bin/gdal_rasterize
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_rasterize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_rasterize   -v ${PWD} -w ${PWD} <container> -c " $@"
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