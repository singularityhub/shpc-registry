---
layout: container
name:  "quay.io/biocontainers/bioconductor-imagetcga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-imagetcga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-imagetcga/container.yaml"
updated_at: "2026-04-01 05:28:53.754024"
latest: "1.2.0--r45hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-imagetcga"
aliases:
 - "gdal"
 - "gdal_footprint"
 - "minigzip"
 - "minizip"
 - "sozip"
 - "bsdunzip"
 - "gdal_create"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "gnmanalyse"
 - "gnmmanage"
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
 - "1.2.0--r45hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-imagetcga"
config: {"url": "https://biocontainers.pro/tools/bioconductor-imagetcga", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-imagetcga", "latest": {"1.2.0--r45hdfd78af_0": "sha256:18ce4f03bc3f2b5360e50e3df07dded3672368260414dc715aab0570c6d65c10"}, "tags": {"1.2.0--r45hdfd78af_0": "sha256:18ce4f03bc3f2b5360e50e3df07dded3672368260414dc715aab0570c6d65c10"}, "docker": "quay.io/biocontainers/bioconductor-imagetcga", "aliases": {"gdal": "/usr/local/bin/gdal", "gdal_footprint": "/usr/local/bin/gdal_footprint", "minigzip": "/usr/local/bin/minigzip", "minizip": "/usr/local/bin/minizip", "sozip": "/usr/local/bin/sozip", "bsdunzip": "/usr/local/bin/bsdunzip", "gdal_create": "/usr/local/bin/gdal_create", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage", "gdal-config": "/usr/local/bin/gdal-config", "gdal_contour": "/usr/local/bin/gdal_contour", "gdal_grid": "/usr/local/bin/gdal_grid", "gdal_rasterize": "/usr/local/bin/gdal_rasterize", "gdal_translate": "/usr/local/bin/gdal_translate", "gdaladdo": "/usr/local/bin/gdaladdo", "gdalbuildvrt": "/usr/local/bin/gdalbuildvrt", "gdaldem": "/usr/local/bin/gdaldem", "gdalenhance": "/usr/local/bin/gdalenhance", "gdalinfo": "/usr/local/bin/gdalinfo", "gdallocationinfo": "/usr/local/bin/gdallocationinfo", "gdalmanage": "/usr/local/bin/gdalmanage", "gdalsrsinfo": "/usr/local/bin/gdalsrsinfo", "gdaltindex": "/usr/local/bin/gdaltindex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-imagetcga.
singularity registry hpc automated addition for bioconductor-imagetcga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-imagetcga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-imagetcga:1.2.0--r45hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-imagetcga/1.2.0--r45hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-imagetcga/1.2.0--r45hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-imagetcga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-imagetcga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-imagetcga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-imagetcga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-imagetcga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-imagetcga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gdal

```bash
$ singularity exec <container> /usr/local/bin/gdal
$ podman run --it --rm --entrypoint /usr/local/bin/gdal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal   -v ${PWD} -w ${PWD} <container> -c " $@"
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