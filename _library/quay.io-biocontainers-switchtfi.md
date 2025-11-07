---
layout: container
name:  "quay.io/biocontainers/switchtfi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/switchtfi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/switchtfi/container.yaml"
updated_at: "2025-11-07 04:00:13.214411"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/switchtfi"
aliases:
 - "convertfilestopdf"
 - "convertfilestops"
 - "convertformat"
 - "convertsegfilestopdf"
 - "convertsegfilestops"
 - "converttopdf"
 - "converttops"
 - "fileinfo"
 - "imagetops"
 - "jbig2dec"
 - "mupdf-gl"
 - "muraster"
 - "mutool"
 - "pymupdf"
 - "tesseract"
 - "xtractprotos"
 - "zarr"
 - "gtk-builder-tool"
 - "gtk-encode-symbolic-svg"
 - "gtk-launch"
 - "gtk-query-immodules-3.0"
 - "gtk-query-settings"
 - "bsdunzip"
 - "wayland-scanner"
 - "h5fuse"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "igraph"
 - "scanpy"
 - "xkbcli"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for switchtfi"
config: {"url": "https://biocontainers.pro/tools/switchtfi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for switchtfi", "latest": {"0.1.0--pyhdfd78af_0": "sha256:439b7e3f54a51995491a79ebe3840bc256013fe5b990c32716163baabb193c38"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:439b7e3f54a51995491a79ebe3840bc256013fe5b990c32716163baabb193c38"}, "docker": "quay.io/biocontainers/switchtfi", "aliases": {"convertfilestopdf": "/usr/local/bin/convertfilestopdf", "convertfilestops": "/usr/local/bin/convertfilestops", "convertformat": "/usr/local/bin/convertformat", "convertsegfilestopdf": "/usr/local/bin/convertsegfilestopdf", "convertsegfilestops": "/usr/local/bin/convertsegfilestops", "converttopdf": "/usr/local/bin/converttopdf", "converttops": "/usr/local/bin/converttops", "fileinfo": "/usr/local/bin/fileinfo", "imagetops": "/usr/local/bin/imagetops", "jbig2dec": "/usr/local/bin/jbig2dec", "mupdf-gl": "/usr/local/bin/mupdf-gl", "muraster": "/usr/local/bin/muraster", "mutool": "/usr/local/bin/mutool", "pymupdf": "/usr/local/bin/pymupdf", "tesseract": "/usr/local/bin/tesseract", "xtractprotos": "/usr/local/bin/xtractprotos", "zarr": "/usr/local/bin/zarr", "gtk-builder-tool": "/usr/local/bin/gtk-builder-tool", "gtk-encode-symbolic-svg": "/usr/local/bin/gtk-encode-symbolic-svg", "gtk-launch": "/usr/local/bin/gtk-launch", "gtk-query-immodules-3.0": "/usr/local/bin/gtk-query-immodules-3.0", "gtk-query-settings": "/usr/local/bin/gtk-query-settings", "bsdunzip": "/usr/local/bin/bsdunzip", "wayland-scanner": "/usr/local/bin/wayland-scanner", "h5fuse": "/usr/local/bin/h5fuse", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "igraph": "/usr/local/bin/igraph", "scanpy": "/usr/local/bin/scanpy", "xkbcli": "/usr/local/bin/xkbcli", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/switchtfi.
singularity registry hpc automated addition for switchtfi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/switchtfi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/switchtfi:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/switchtfi/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/switchtfi/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### switchtfi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### switchtfi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### switchtfi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### switchtfi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### switchtfi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### switchtfi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertfilestopdf

```bash
$ singularity exec <container> /usr/local/bin/convertfilestopdf
$ podman run --it --rm --entrypoint /usr/local/bin/convertfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertfilestops

```bash
$ singularity exec <container> /usr/local/bin/convertfilestops
$ podman run --it --rm --entrypoint /usr/local/bin/convertfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertformat

```bash
$ singularity exec <container> /usr/local/bin/convertformat
$ podman run --it --rm --entrypoint /usr/local/bin/convertformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertsegfilestopdf

```bash
$ singularity exec <container> /usr/local/bin/convertsegfilestopdf
$ podman run --it --rm --entrypoint /usr/local/bin/convertsegfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertsegfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertsegfilestops

```bash
$ singularity exec <container> /usr/local/bin/convertsegfilestops
$ podman run --it --rm --entrypoint /usr/local/bin/convertsegfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertsegfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converttopdf

```bash
$ singularity exec <container> /usr/local/bin/converttopdf
$ podman run --it --rm --entrypoint /usr/local/bin/converttopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converttopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converttops

```bash
$ singularity exec <container> /usr/local/bin/converttops
$ podman run --it --rm --entrypoint /usr/local/bin/converttops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converttops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fileinfo

```bash
$ singularity exec <container> /usr/local/bin/fileinfo
$ podman run --it --rm --entrypoint /usr/local/bin/fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagetops

```bash
$ singularity exec <container> /usr/local/bin/imagetops
$ podman run --it --rm --entrypoint /usr/local/bin/imagetops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagetops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jbig2dec

```bash
$ singularity exec <container> /usr/local/bin/jbig2dec
$ podman run --it --rm --entrypoint /usr/local/bin/jbig2dec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jbig2dec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mupdf-gl

```bash
$ singularity exec <container> /usr/local/bin/mupdf-gl
$ podman run --it --rm --entrypoint /usr/local/bin/mupdf-gl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mupdf-gl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muraster

```bash
$ singularity exec <container> /usr/local/bin/muraster
$ podman run --it --rm --entrypoint /usr/local/bin/muraster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muraster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutool

```bash
$ singularity exec <container> /usr/local/bin/mutool
$ podman run --it --rm --entrypoint /usr/local/bin/mutool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pymupdf

```bash
$ singularity exec <container> /usr/local/bin/pymupdf
$ podman run --it --rm --entrypoint /usr/local/bin/pymupdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pymupdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tesseract

```bash
$ singularity exec <container> /usr/local/bin/tesseract
$ podman run --it --rm --entrypoint /usr/local/bin/tesseract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tesseract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractprotos

```bash
$ singularity exec <container> /usr/local/bin/xtractprotos
$ podman run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zarr

```bash
$ singularity exec <container> /usr/local/bin/zarr
$ podman run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-encode-symbolic-svg

```bash
$ singularity exec <container> /usr/local/bin/gtk-encode-symbolic-svg
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-launch

```bash
$ singularity exec <container> /usr/local/bin/gtk-launch
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-3.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-settings

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-settings
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
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