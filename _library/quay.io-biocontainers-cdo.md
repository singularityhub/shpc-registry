---
layout: container
name:  "quay.io/biocontainers/cdo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cdo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cdo/container.yaml"
updated_at: "2023-03-20 03:33:16.503165"
latest: "2.0.0"
container_url: "https://biocontainers.pro/tools/cdo"
aliases:
 - "bufr_compare"
 - "bufr_compare_dir"
 - "bufr_copy"
 - "bufr_count"
 - "bufr_dump"
 - "bufr_filter"
 - "bufr_get"
 - "bufr_index_build"
 - "bufr_ls"
 - "bufr_set"
 - "cdo"
 - "codes_bufr_filter"
 - "codes_count"
 - "codes_info"
 - "codes_parser"
 - "codes_split_file"
 - "grib2ppm"
 - "grib_compare"
 - "grib_copy"
 - "grib_count"
 - "grib_dump"
 - "grib_filter"
 - "grib_get"
 - "grib_get_data"
 - "grib_histogram"
 - "grib_index_build"
 - "grib_ls"
 - "grib_merge"
 - "grib_set"
 - "grib_to_netcdf"
 - "gts_compare"
 - "gts_copy"
 - "gts_count"
 - "gts_dump"
 - "gts_filter"
 - "gts_get"
 - "gts_ls"
 - "imgcmp"
 - "imginfo"
 - "jasper"
 - "jiv"
 - "metar_compare"
 - "metar_copy"
 - "metar_dump"
 - "metar_filter"
 - "metar_get"
 - "metar_ls"
 - "tigge_check"
 - "aec"
 - "uuid"
 - "uuid-config"
 - "projsync"
 - "udunits2"
 - "invgeod"
 - "invproj"
 - "projinfo"
 - "cct"
 - "gie"
versions:
 - "2.0.0"
description: "shpc-registry automated BioContainers addition for cdo"
config: {"url": "https://biocontainers.pro/tools/cdo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cdo", "latest": {"2.0.0": "sha256:4912d32e1d1559ea840bf333c58cecd595a4ee50891ce71a1cbd7d45a778d2ca"}, "tags": {"2.0.0": "sha256:4912d32e1d1559ea840bf333c58cecd595a4ee50891ce71a1cbd7d45a778d2ca"}, "docker": "quay.io/biocontainers/cdo", "aliases": {"bufr_compare": "/usr/local/bin/bufr_compare", "bufr_compare_dir": "/usr/local/bin/bufr_compare_dir", "bufr_copy": "/usr/local/bin/bufr_copy", "bufr_count": "/usr/local/bin/bufr_count", "bufr_dump": "/usr/local/bin/bufr_dump", "bufr_filter": "/usr/local/bin/bufr_filter", "bufr_get": "/usr/local/bin/bufr_get", "bufr_index_build": "/usr/local/bin/bufr_index_build", "bufr_ls": "/usr/local/bin/bufr_ls", "bufr_set": "/usr/local/bin/bufr_set", "cdo": "/usr/local/bin/cdo", "codes_bufr_filter": "/usr/local/bin/codes_bufr_filter", "codes_count": "/usr/local/bin/codes_count", "codes_info": "/usr/local/bin/codes_info", "codes_parser": "/usr/local/bin/codes_parser", "codes_split_file": "/usr/local/bin/codes_split_file", "grib2ppm": "/usr/local/bin/grib2ppm", "grib_compare": "/usr/local/bin/grib_compare", "grib_copy": "/usr/local/bin/grib_copy", "grib_count": "/usr/local/bin/grib_count", "grib_dump": "/usr/local/bin/grib_dump", "grib_filter": "/usr/local/bin/grib_filter", "grib_get": "/usr/local/bin/grib_get", "grib_get_data": "/usr/local/bin/grib_get_data", "grib_histogram": "/usr/local/bin/grib_histogram", "grib_index_build": "/usr/local/bin/grib_index_build", "grib_ls": "/usr/local/bin/grib_ls", "grib_merge": "/usr/local/bin/grib_merge", "grib_set": "/usr/local/bin/grib_set", "grib_to_netcdf": "/usr/local/bin/grib_to_netcdf", "gts_compare": "/usr/local/bin/gts_compare", "gts_copy": "/usr/local/bin/gts_copy", "gts_count": "/usr/local/bin/gts_count", "gts_dump": "/usr/local/bin/gts_dump", "gts_filter": "/usr/local/bin/gts_filter", "gts_get": "/usr/local/bin/gts_get", "gts_ls": "/usr/local/bin/gts_ls", "imgcmp": "/usr/local/bin/imgcmp", "imginfo": "/usr/local/bin/imginfo", "jasper": "/usr/local/bin/jasper", "jiv": "/usr/local/bin/jiv", "metar_compare": "/usr/local/bin/metar_compare", "metar_copy": "/usr/local/bin/metar_copy", "metar_dump": "/usr/local/bin/metar_dump", "metar_filter": "/usr/local/bin/metar_filter", "metar_get": "/usr/local/bin/metar_get", "metar_ls": "/usr/local/bin/metar_ls", "tigge_check": "/usr/local/bin/tigge_check", "aec": "/usr/local/bin/aec", "uuid": "/usr/local/bin/uuid", "uuid-config": "/usr/local/bin/uuid-config", "projsync": "/usr/local/bin/projsync", "udunits2": "/usr/local/bin/udunits2", "invgeod": "/usr/local/bin/invgeod", "invproj": "/usr/local/bin/invproj", "projinfo": "/usr/local/bin/projinfo", "cct": "/usr/local/bin/cct", "gie": "/usr/local/bin/gie"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cdo.
shpc-registry automated BioContainers addition for cdo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cdo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cdo:2.0.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cdo/2.0.0
$ module help quay.io/biocontainers/cdo/2.0.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cdo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cdo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cdo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cdo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cdo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cdo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bufr_compare

```bash
$ singularity exec <container> /usr/local/bin/bufr_compare
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_compare_dir

```bash
$ singularity exec <container> /usr/local/bin/bufr_compare_dir
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_compare_dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_compare_dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_copy

```bash
$ singularity exec <container> /usr/local/bin/bufr_copy
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_count

```bash
$ singularity exec <container> /usr/local/bin/bufr_count
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_dump

```bash
$ singularity exec <container> /usr/local/bin/bufr_dump
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_filter

```bash
$ singularity exec <container> /usr/local/bin/bufr_filter
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_get

```bash
$ singularity exec <container> /usr/local/bin/bufr_get
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_index_build

```bash
$ singularity exec <container> /usr/local/bin/bufr_index_build
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_index_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_index_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_ls

```bash
$ singularity exec <container> /usr/local/bin/bufr_ls
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bufr_set

```bash
$ singularity exec <container> /usr/local/bin/bufr_set
$ podman run --it --rm --entrypoint /usr/local/bin/bufr_set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bufr_set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdo

```bash
$ singularity exec <container> /usr/local/bin/cdo
$ podman run --it --rm --entrypoint /usr/local/bin/cdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codes_bufr_filter

```bash
$ singularity exec <container> /usr/local/bin/codes_bufr_filter
$ podman run --it --rm --entrypoint /usr/local/bin/codes_bufr_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codes_bufr_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codes_count

```bash
$ singularity exec <container> /usr/local/bin/codes_count
$ podman run --it --rm --entrypoint /usr/local/bin/codes_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codes_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codes_info

```bash
$ singularity exec <container> /usr/local/bin/codes_info
$ podman run --it --rm --entrypoint /usr/local/bin/codes_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codes_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codes_parser

```bash
$ singularity exec <container> /usr/local/bin/codes_parser
$ podman run --it --rm --entrypoint /usr/local/bin/codes_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codes_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codes_split_file

```bash
$ singularity exec <container> /usr/local/bin/codes_split_file
$ podman run --it --rm --entrypoint /usr/local/bin/codes_split_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codes_split_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib2ppm

```bash
$ singularity exec <container> /usr/local/bin/grib2ppm
$ podman run --it --rm --entrypoint /usr/local/bin/grib2ppm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib2ppm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_compare

```bash
$ singularity exec <container> /usr/local/bin/grib_compare
$ podman run --it --rm --entrypoint /usr/local/bin/grib_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_copy

```bash
$ singularity exec <container> /usr/local/bin/grib_copy
$ podman run --it --rm --entrypoint /usr/local/bin/grib_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_count

```bash
$ singularity exec <container> /usr/local/bin/grib_count
$ podman run --it --rm --entrypoint /usr/local/bin/grib_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_dump

```bash
$ singularity exec <container> /usr/local/bin/grib_dump
$ podman run --it --rm --entrypoint /usr/local/bin/grib_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_filter

```bash
$ singularity exec <container> /usr/local/bin/grib_filter
$ podman run --it --rm --entrypoint /usr/local/bin/grib_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_get

```bash
$ singularity exec <container> /usr/local/bin/grib_get
$ podman run --it --rm --entrypoint /usr/local/bin/grib_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_get_data

```bash
$ singularity exec <container> /usr/local/bin/grib_get_data
$ podman run --it --rm --entrypoint /usr/local/bin/grib_get_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_get_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_histogram

```bash
$ singularity exec <container> /usr/local/bin/grib_histogram
$ podman run --it --rm --entrypoint /usr/local/bin/grib_histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_index_build

```bash
$ singularity exec <container> /usr/local/bin/grib_index_build
$ podman run --it --rm --entrypoint /usr/local/bin/grib_index_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_index_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_ls

```bash
$ singularity exec <container> /usr/local/bin/grib_ls
$ podman run --it --rm --entrypoint /usr/local/bin/grib_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_merge

```bash
$ singularity exec <container> /usr/local/bin/grib_merge
$ podman run --it --rm --entrypoint /usr/local/bin/grib_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_set

```bash
$ singularity exec <container> /usr/local/bin/grib_set
$ podman run --it --rm --entrypoint /usr/local/bin/grib_set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grib_to_netcdf

```bash
$ singularity exec <container> /usr/local/bin/grib_to_netcdf
$ podman run --it --rm --entrypoint /usr/local/bin/grib_to_netcdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grib_to_netcdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_compare

```bash
$ singularity exec <container> /usr/local/bin/gts_compare
$ podman run --it --rm --entrypoint /usr/local/bin/gts_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_copy

```bash
$ singularity exec <container> /usr/local/bin/gts_copy
$ podman run --it --rm --entrypoint /usr/local/bin/gts_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_count

```bash
$ singularity exec <container> /usr/local/bin/gts_count
$ podman run --it --rm --entrypoint /usr/local/bin/gts_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_dump

```bash
$ singularity exec <container> /usr/local/bin/gts_dump
$ podman run --it --rm --entrypoint /usr/local/bin/gts_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_filter

```bash
$ singularity exec <container> /usr/local/bin/gts_filter
$ podman run --it --rm --entrypoint /usr/local/bin/gts_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_get

```bash
$ singularity exec <container> /usr/local/bin/gts_get
$ podman run --it --rm --entrypoint /usr/local/bin/gts_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts_ls

```bash
$ singularity exec <container> /usr/local/bin/gts_ls
$ podman run --it --rm --entrypoint /usr/local/bin/gts_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imgcmp

```bash
$ singularity exec <container> /usr/local/bin/imgcmp
$ podman run --it --rm --entrypoint /usr/local/bin/imgcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imginfo

```bash
$ singularity exec <container> /usr/local/bin/imginfo
$ podman run --it --rm --entrypoint /usr/local/bin/imginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasper

```bash
$ singularity exec <container> /usr/local/bin/jasper
$ podman run --it --rm --entrypoint /usr/local/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jiv

```bash
$ singularity exec <container> /usr/local/bin/jiv
$ podman run --it --rm --entrypoint /usr/local/bin/jiv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jiv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metar_compare

```bash
$ singularity exec <container> /usr/local/bin/metar_compare
$ podman run --it --rm --entrypoint /usr/local/bin/metar_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metar_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metar_copy

```bash
$ singularity exec <container> /usr/local/bin/metar_copy
$ podman run --it --rm --entrypoint /usr/local/bin/metar_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metar_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metar_dump

```bash
$ singularity exec <container> /usr/local/bin/metar_dump
$ podman run --it --rm --entrypoint /usr/local/bin/metar_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metar_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metar_filter

```bash
$ singularity exec <container> /usr/local/bin/metar_filter
$ podman run --it --rm --entrypoint /usr/local/bin/metar_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metar_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metar_get

```bash
$ singularity exec <container> /usr/local/bin/metar_get
$ podman run --it --rm --entrypoint /usr/local/bin/metar_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metar_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metar_ls

```bash
$ singularity exec <container> /usr/local/bin/metar_ls
$ podman run --it --rm --entrypoint /usr/local/bin/metar_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metar_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigge_check

```bash
$ singularity exec <container> /usr/local/bin/tigge_check
$ podman run --it --rm --entrypoint /usr/local/bin/tigge_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigge_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aec

```bash
$ singularity exec <container> /usr/local/bin/aec
$ podman run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid

```bash
$ singularity exec <container> /usr/local/bin/uuid
$ podman run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid-config

```bash
$ singularity exec <container> /usr/local/bin/uuid-config
$ podman run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projsync

```bash
$ singularity exec <container> /usr/local/bin/projsync
$ podman run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### udunits2

```bash
$ singularity exec <container> /usr/local/bin/udunits2
$ podman run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invgeod

```bash
$ singularity exec <container> /usr/local/bin/invgeod
$ podman run --it --rm --entrypoint /usr/local/bin/invgeod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invgeod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invproj

```bash
$ singularity exec <container> /usr/local/bin/invproj
$ podman run --it --rm --entrypoint /usr/local/bin/invproj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invproj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projinfo

```bash
$ singularity exec <container> /usr/local/bin/projinfo
$ podman run --it --rm --entrypoint /usr/local/bin/projinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cct

```bash
$ singularity exec <container> /usr/local/bin/cct
$ podman run --it --rm --entrypoint /usr/local/bin/cct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gie

```bash
$ singularity exec <container> /usr/local/bin/gie
$ podman run --it --rm --entrypoint /usr/local/bin/gie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gie   -v ${PWD} -w ${PWD} <container> -c " $@"
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