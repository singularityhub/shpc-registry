---
layout: container
name:  "quay.io/biocontainers/geopandas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/geopandas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/geopandas/container.yaml"
updated_at: "2026-01-20 04:38:37.866423"
latest: "1.1.1"
container_url: "https://biocontainers.pro/tools/geopandas"
aliases:
 - "gdal_footprint"
 - "minigzip"
 - "minizip"
 - "pyproj"
 - "sozip"
 - "bsdunzip"
 - "gdal_create"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "applygeo"
 - "geotifcp"
 - "gnmanalyse"
 - "gnmmanage"
 - "listgeo"
 - "makegeo"
 - "gdal-config"
 - "gdal_contour"
 - "gdal_grid"
 - "gdal_rasterize"
 - "gdal_translate"
 - "gdaladdo"
 - "gdalbuildvrt"
 - "gdaldem"
 - "gdalenhance"
 - "gdalinfo"
 - "gdallocationinfo"
 - "gdalmanage"
 - "gdalsrsinfo"
 - "gdaltindex"
versions:
 - "1.0.1"
 - "1.1.1"
description: "singularity registry hpc automated addition for geopandas"
config: {"url": "https://biocontainers.pro/tools/geopandas", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for geopandas", "latest": {"1.1.1": "sha256:a22822669876c538c32c3e9b1d5eae3dc921ca75892d0f81611adda510af780f"}, "tags": {"1.0.1": "sha256:6c9877f08b72dbb1052281213333da095e88f6fba105405ad61b8ccc59d6a0dc", "1.1.1": "sha256:a22822669876c538c32c3e9b1d5eae3dc921ca75892d0f81611adda510af780f"}, "docker": "quay.io/biocontainers/geopandas", "aliases": {"gdal_footprint": "/usr/local/bin/gdal_footprint", "minigzip": "/usr/local/bin/minigzip", "minizip": "/usr/local/bin/minizip", "pyproj": "/usr/local/bin/pyproj", "sozip": "/usr/local/bin/sozip", "bsdunzip": "/usr/local/bin/bsdunzip", "gdal_create": "/usr/local/bin/gdal_create", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "applygeo": "/usr/local/bin/applygeo", "geotifcp": "/usr/local/bin/geotifcp", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage", "listgeo": "/usr/local/bin/listgeo", "makegeo": "/usr/local/bin/makegeo", "gdal-config": "/usr/local/bin/gdal-config", "gdal_contour": "/usr/local/bin/gdal_contour", "gdal_grid": "/usr/local/bin/gdal_grid", "gdal_rasterize": "/usr/local/bin/gdal_rasterize", "gdal_translate": "/usr/local/bin/gdal_translate", "gdaladdo": "/usr/local/bin/gdaladdo", "gdalbuildvrt": "/usr/local/bin/gdalbuildvrt", "gdaldem": "/usr/local/bin/gdaldem", "gdalenhance": "/usr/local/bin/gdalenhance", "gdalinfo": "/usr/local/bin/gdalinfo", "gdallocationinfo": "/usr/local/bin/gdallocationinfo", "gdalmanage": "/usr/local/bin/gdalmanage", "gdalsrsinfo": "/usr/local/bin/gdalsrsinfo", "gdaltindex": "/usr/local/bin/gdaltindex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/geopandas.
singularity registry hpc automated addition for geopandas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/geopandas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/geopandas:1.1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/geopandas/1.1.1
$ module help quay.io/biocontainers/geopandas/1.1.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geopandas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geopandas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geopandas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geopandas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geopandas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geopandas-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### pyproj

```bash
$ singularity exec <container> /usr/local/bin/pyproj
$ podman run --it --rm --entrypoint /usr/local/bin/pyproj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyproj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sozip

```bash
$ singularity exec <container> /usr/local/bin/sozip
$ podman run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### applygeo

```bash
$ singularity exec <container> /usr/local/bin/applygeo
$ podman run --it --rm --entrypoint /usr/local/bin/applygeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applygeo   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gdal_translate

```bash
$ singularity exec <container> /usr/local/bin/gdal_translate
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaladdo

```bash
$ singularity exec <container> /usr/local/bin/gdaladdo
$ podman run --it --rm --entrypoint /usr/local/bin/gdaladdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdaladdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalbuildvrt

```bash
$ singularity exec <container> /usr/local/bin/gdalbuildvrt
$ podman run --it --rm --entrypoint /usr/local/bin/gdalbuildvrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalbuildvrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaldem

```bash
$ singularity exec <container> /usr/local/bin/gdaldem
$ podman run --it --rm --entrypoint /usr/local/bin/gdaldem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdaldem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalenhance

```bash
$ singularity exec <container> /usr/local/bin/gdalenhance
$ podman run --it --rm --entrypoint /usr/local/bin/gdalenhance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalenhance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalinfo

```bash
$ singularity exec <container> /usr/local/bin/gdalinfo
$ podman run --it --rm --entrypoint /usr/local/bin/gdalinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdallocationinfo

```bash
$ singularity exec <container> /usr/local/bin/gdallocationinfo
$ podman run --it --rm --entrypoint /usr/local/bin/gdallocationinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdallocationinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmanage

```bash
$ singularity exec <container> /usr/local/bin/gdalmanage
$ podman run --it --rm --entrypoint /usr/local/bin/gdalmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalsrsinfo

```bash
$ singularity exec <container> /usr/local/bin/gdalsrsinfo
$ podman run --it --rm --entrypoint /usr/local/bin/gdalsrsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalsrsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaltindex

```bash
$ singularity exec <container> /usr/local/bin/gdaltindex
$ podman run --it --rm --entrypoint /usr/local/bin/gdaltindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdaltindex   -v ${PWD} -w ${PWD} <container> -c " $@"
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