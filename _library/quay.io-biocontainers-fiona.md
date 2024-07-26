---
layout: container
name:  "quay.io/biocontainers/fiona"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fiona/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fiona/container.yaml"
updated_at: "2024-07-26 02:53:38.509441"
latest: "1.8.6"
container_url: "https://biocontainers.pro/tools/fiona"
aliases:
 - "epsg_tr.py"
 - "esri2wkt.py"
 - "fio"
 - "gcps2vec.py"
 - "gcps2wld.py"
 - "gdal2tiles.py"
 - "gdal2xyz.py"
 - "gdal_auth.py"
 - "gdal_calc.py"
 - "gdal_edit.py"
 - "gdal_fillnodata.py"
 - "gdal_merge.py"
 - "gdal_pansharpen.py"
 - "gdal_polygonize.py"
 - "gdal_proximity.py"
 - "gdal_retile.py"
 - "gdal_sieve.py"
 - "gdalchksum.py"
 - "gdalcompare.py"
 - "gdalident.py"
 - "gdalimport.py"
 - "gdalmove.py"
 - "gdalserver"
 - "mkgraticule.py"
 - "ogrmerge.py"
 - "pct2rgb.py"
 - "rgb2pct.py"
 - "testepsg"
 - "pg_standby"
 - "applygeo"
 - "geotifcp"
 - "gnmanalyse"
 - "gnmmanage"
 - "kea-config"
 - "listgeo"
 - "makegeo"
 - "pg_checksums"
versions:
 - "1.8.6"
description: "shpc-registry automated BioContainers addition for fiona"
config: {"url": "https://biocontainers.pro/tools/fiona", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fiona", "latest": {"1.8.6": "sha256:0c298931e18e1c093a70598fc6b2c9f5722ac3212a4fcc58a02d834b6b6f5cae"}, "tags": {"1.8.6": "sha256:0c298931e18e1c093a70598fc6b2c9f5722ac3212a4fcc58a02d834b6b6f5cae"}, "docker": "quay.io/biocontainers/fiona", "aliases": {"epsg_tr.py": "/usr/local/bin/epsg_tr.py", "esri2wkt.py": "/usr/local/bin/esri2wkt.py", "fio": "/usr/local/bin/fio", "gcps2vec.py": "/usr/local/bin/gcps2vec.py", "gcps2wld.py": "/usr/local/bin/gcps2wld.py", "gdal2tiles.py": "/usr/local/bin/gdal2tiles.py", "gdal2xyz.py": "/usr/local/bin/gdal2xyz.py", "gdal_auth.py": "/usr/local/bin/gdal_auth.py", "gdal_calc.py": "/usr/local/bin/gdal_calc.py", "gdal_edit.py": "/usr/local/bin/gdal_edit.py", "gdal_fillnodata.py": "/usr/local/bin/gdal_fillnodata.py", "gdal_merge.py": "/usr/local/bin/gdal_merge.py", "gdal_pansharpen.py": "/usr/local/bin/gdal_pansharpen.py", "gdal_polygonize.py": "/usr/local/bin/gdal_polygonize.py", "gdal_proximity.py": "/usr/local/bin/gdal_proximity.py", "gdal_retile.py": "/usr/local/bin/gdal_retile.py", "gdal_sieve.py": "/usr/local/bin/gdal_sieve.py", "gdalchksum.py": "/usr/local/bin/gdalchksum.py", "gdalcompare.py": "/usr/local/bin/gdalcompare.py", "gdalident.py": "/usr/local/bin/gdalident.py", "gdalimport.py": "/usr/local/bin/gdalimport.py", "gdalmove.py": "/usr/local/bin/gdalmove.py", "gdalserver": "/usr/local/bin/gdalserver", "mkgraticule.py": "/usr/local/bin/mkgraticule.py", "ogrmerge.py": "/usr/local/bin/ogrmerge.py", "pct2rgb.py": "/usr/local/bin/pct2rgb.py", "rgb2pct.py": "/usr/local/bin/rgb2pct.py", "testepsg": "/usr/local/bin/testepsg", "pg_standby": "/usr/local/bin/pg_standby", "applygeo": "/usr/local/bin/applygeo", "geotifcp": "/usr/local/bin/geotifcp", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage", "kea-config": "/usr/local/bin/kea-config", "listgeo": "/usr/local/bin/listgeo", "makegeo": "/usr/local/bin/makegeo", "pg_checksums": "/usr/local/bin/pg_checksums"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fiona.
shpc-registry automated BioContainers addition for fiona
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fiona
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fiona:1.8.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fiona/1.8.6
$ module help quay.io/biocontainers/fiona/1.8.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fiona-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fiona-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fiona-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fiona-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fiona-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fiona-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epsg_tr.py

```bash
$ singularity exec <container> /usr/local/bin/epsg_tr.py
$ podman run --it --rm --entrypoint /usr/local/bin/epsg_tr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epsg_tr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esri2wkt.py

```bash
$ singularity exec <container> /usr/local/bin/esri2wkt.py
$ podman run --it --rm --entrypoint /usr/local/bin/esri2wkt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esri2wkt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fio

```bash
$ singularity exec <container> /usr/local/bin/fio
$ podman run --it --rm --entrypoint /usr/local/bin/fio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcps2vec.py

```bash
$ singularity exec <container> /usr/local/bin/gcps2vec.py
$ podman run --it --rm --entrypoint /usr/local/bin/gcps2vec.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcps2vec.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcps2wld.py

```bash
$ singularity exec <container> /usr/local/bin/gcps2wld.py
$ podman run --it --rm --entrypoint /usr/local/bin/gcps2wld.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcps2wld.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal2tiles.py

```bash
$ singularity exec <container> /usr/local/bin/gdal2tiles.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal2tiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal2tiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal2xyz.py

```bash
$ singularity exec <container> /usr/local/bin/gdal2xyz.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal2xyz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal2xyz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_auth.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_auth.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_auth.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_auth.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_calc.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_calc.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_calc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_calc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_edit.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_edit.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_edit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_edit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_fillnodata.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_fillnodata.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_fillnodata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_fillnodata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_merge.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_pansharpen.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_pansharpen.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_pansharpen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_pansharpen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_polygonize.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_polygonize.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_polygonize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_polygonize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_proximity.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_proximity.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_proximity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_proximity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_retile.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_retile.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_retile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_retile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_sieve.py

```bash
$ singularity exec <container> /usr/local/bin/gdal_sieve.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_sieve.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_sieve.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalchksum.py

```bash
$ singularity exec <container> /usr/local/bin/gdalchksum.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdalchksum.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalchksum.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalcompare.py

```bash
$ singularity exec <container> /usr/local/bin/gdalcompare.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdalcompare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalcompare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalident.py

```bash
$ singularity exec <container> /usr/local/bin/gdalident.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdalident.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalident.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalimport.py

```bash
$ singularity exec <container> /usr/local/bin/gdalimport.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdalimport.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalimport.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmove.py

```bash
$ singularity exec <container> /usr/local/bin/gdalmove.py
$ podman run --it --rm --entrypoint /usr/local/bin/gdalmove.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalmove.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalserver

```bash
$ singularity exec <container> /usr/local/bin/gdalserver
$ podman run --it --rm --entrypoint /usr/local/bin/gdalserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkgraticule.py

```bash
$ singularity exec <container> /usr/local/bin/mkgraticule.py
$ podman run --it --rm --entrypoint /usr/local/bin/mkgraticule.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkgraticule.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ogrmerge.py

```bash
$ singularity exec <container> /usr/local/bin/ogrmerge.py
$ podman run --it --rm --entrypoint /usr/local/bin/ogrmerge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ogrmerge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pct2rgb.py

```bash
$ singularity exec <container> /usr/local/bin/pct2rgb.py
$ podman run --it --rm --entrypoint /usr/local/bin/pct2rgb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pct2rgb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgb2pct.py

```bash
$ singularity exec <container> /usr/local/bin/rgb2pct.py
$ podman run --it --rm --entrypoint /usr/local/bin/rgb2pct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgb2pct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testepsg

```bash
$ singularity exec <container> /usr/local/bin/testepsg
$ podman run --it --rm --entrypoint /usr/local/bin/testepsg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testepsg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_standby

```bash
$ singularity exec <container> /usr/local/bin/pg_standby
$ podman run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
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