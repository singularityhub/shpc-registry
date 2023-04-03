---
layout: container
name:  "quay.io/biocontainers/bioconductor-voyager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-voyager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-voyager/container.yaml"
updated_at: "2023-04-03 03:14:01.500641"
latest: "1.0.3--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-voyager"
aliases:
 - "pg_amcheck"
 - "gdal_create"
 - "pdfsig"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "pg_verifybackup"
 - "pdfattach"
 - "udunits2"
 - "applygeo"
 - "geotifcp"
 - "gnmanalyse"
 - "gnmmanage"
 - "kea-config"
 - "listgeo"
 - "makegeo"
 - "pg_checksums"
 - "projsync"
 - "dap-config"
 - "dap-config-pkgconfig"
 - "gdal-config"
 - "gdal_contour"
 - "gdal_grid"
 - "gdal_rasterize"
 - "gdal_translate"
versions:
 - "1.0.3--r42hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-voyager"
config: {"url": "https://biocontainers.pro/tools/bioconductor-voyager", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-voyager", "latest": {"1.0.3--r42hdfd78af_0": "sha256:75d362cdc99858d11607d5ece6d23a1cbfbec355d2cfd98a2dbe4e87fc7858e7"}, "tags": {"1.0.3--r42hdfd78af_0": "sha256:75d362cdc99858d11607d5ece6d23a1cbfbec355d2cfd98a2dbe4e87fc7858e7"}, "docker": "quay.io/biocontainers/bioconductor-voyager", "aliases": {"pg_amcheck": "/usr/local/bin/pg_amcheck", "gdal_create": "/usr/local/bin/gdal_create", "pdfsig": "/usr/local/bin/pdfsig", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "pdfattach": "/usr/local/bin/pdfattach", "udunits2": "/usr/local/bin/udunits2", "applygeo": "/usr/local/bin/applygeo", "geotifcp": "/usr/local/bin/geotifcp", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage", "kea-config": "/usr/local/bin/kea-config", "listgeo": "/usr/local/bin/listgeo", "makegeo": "/usr/local/bin/makegeo", "pg_checksums": "/usr/local/bin/pg_checksums", "projsync": "/usr/local/bin/projsync", "dap-config": "/usr/local/bin/dap-config", "dap-config-pkgconfig": "/usr/local/bin/dap-config-pkgconfig", "gdal-config": "/usr/local/bin/gdal-config", "gdal_contour": "/usr/local/bin/gdal_contour", "gdal_grid": "/usr/local/bin/gdal_grid", "gdal_rasterize": "/usr/local/bin/gdal_rasterize", "gdal_translate": "/usr/local/bin/gdal_translate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-voyager.
singularity registry hpc automated addition for bioconductor-voyager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-voyager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-voyager:1.0.3--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-voyager/1.0.3--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-voyager/1.0.3--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-voyager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-voyager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-voyager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-voyager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-voyager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-voyager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pg_amcheck

```bash
$ singularity exec <container> /usr/local/bin/pg_amcheck
$ podman run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_create

```bash
$ singularity exec <container> /usr/local/bin/gdal_create
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pg_verifybackup

```bash
$ singularity exec <container> /usr/local/bin/pg_verifybackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfattach

```bash
$ singularity exec <container> /usr/local/bin/pdfattach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### udunits2

```bash
$ singularity exec <container> /usr/local/bin/udunits2
$ podman run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pg_checksums

```bash
$ singularity exec <container> /usr/local/bin/pg_checksums
$ podman run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projsync

```bash
$ singularity exec <container> /usr/local/bin/projsync
$ podman run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dap-config

```bash
$ singularity exec <container> /usr/local/bin/dap-config
$ podman run --it --rm --entrypoint /usr/local/bin/dap-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dap-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dap-config-pkgconfig

```bash
$ singularity exec <container> /usr/local/bin/dap-config-pkgconfig
$ podman run --it --rm --entrypoint /usr/local/bin/dap-config-pkgconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dap-config-pkgconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
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