---
layout: container
name:  "quay.io/biocontainers/osra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/osra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/osra/container.yaml"
updated_at: "2025-12-31 04:10:25.305966"
latest: "2.1.0--0"
container_url: "https://biocontainers.pro/tools/osra"
aliases:
 - "GraphicsMagick++-config"
 - "GraphicsMagick-config"
 - "GraphicsMagickWand-config"
 - "babel"
 - "convertfilestopdf"
 - "convertfilestops"
 - "convertformat"
 - "convertsegfilestopdf"
 - "convertsegfilestops"
 - "converttopdf"
 - "converttops"
 - "fileinfo"
 - "font2c"
 - "gm"
 - "gocr"
 - "gocr.tcl"
 - "mkbitmap"
 - "ocrad"
 - "osra"
 - "potrace"
 - "printimage"
 - "printsplitimage"
 - "printtiff"
 - "splitimage2pdf"
 - "tesseract"
 - "wftopfa"
 - "xtractprotos"
 - "roundtrip"
 - "gnuplot"
 - "pdfdetach"
 - "pdffonts"
 - "pdfimages"
 - "pdfinfo"
 - "pdfseparate"
 - "pdftocairo"
 - "pdftohtml"
 - "pdftoppm"
versions:
 - "2.1.0--0"
description: "shpc-registry automated BioContainers addition for osra"
config: {"url": "https://biocontainers.pro/tools/osra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for osra", "latest": {"2.1.0--0": "sha256:625eead26506e20b4645c94249b554f1a81bb7bccaa90732ff3f20989279b754"}, "tags": {"2.1.0--0": "sha256:625eead26506e20b4645c94249b554f1a81bb7bccaa90732ff3f20989279b754"}, "docker": "quay.io/biocontainers/osra", "aliases": {"GraphicsMagick++-config": "/usr/local/bin/GraphicsMagick++-config", "GraphicsMagick-config": "/usr/local/bin/GraphicsMagick-config", "GraphicsMagickWand-config": "/usr/local/bin/GraphicsMagickWand-config", "babel": "/usr/local/bin/babel", "convertfilestopdf": "/usr/local/bin/convertfilestopdf", "convertfilestops": "/usr/local/bin/convertfilestops", "convertformat": "/usr/local/bin/convertformat", "convertsegfilestopdf": "/usr/local/bin/convertsegfilestopdf", "convertsegfilestops": "/usr/local/bin/convertsegfilestops", "converttopdf": "/usr/local/bin/converttopdf", "converttops": "/usr/local/bin/converttops", "fileinfo": "/usr/local/bin/fileinfo", "font2c": "/usr/local/bin/font2c", "gm": "/usr/local/bin/gm", "gocr": "/usr/local/bin/gocr", "gocr.tcl": "/usr/local/bin/gocr.tcl", "mkbitmap": "/usr/local/bin/mkbitmap", "ocrad": "/usr/local/bin/ocrad", "osra": "/usr/local/bin/osra", "potrace": "/usr/local/bin/potrace", "printimage": "/usr/local/bin/printimage", "printsplitimage": "/usr/local/bin/printsplitimage", "printtiff": "/usr/local/bin/printtiff", "splitimage2pdf": "/usr/local/bin/splitimage2pdf", "tesseract": "/usr/local/bin/tesseract", "wftopfa": "/usr/local/bin/wftopfa", "xtractprotos": "/usr/local/bin/xtractprotos", "roundtrip": "/usr/local/bin/roundtrip", "gnuplot": "/usr/local/bin/gnuplot", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages", "pdfinfo": "/usr/local/bin/pdfinfo", "pdfseparate": "/usr/local/bin/pdfseparate", "pdftocairo": "/usr/local/bin/pdftocairo", "pdftohtml": "/usr/local/bin/pdftohtml", "pdftoppm": "/usr/local/bin/pdftoppm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/osra.
shpc-registry automated BioContainers addition for osra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/osra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/osra:2.1.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/osra/2.1.0--0
$ module help quay.io/biocontainers/osra/2.1.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### osra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### osra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### osra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### osra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### osra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### osra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GraphicsMagick++-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GraphicsMagick-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagick-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagick-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagick-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GraphicsMagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### babel

```bash
$ singularity exec <container> /usr/local/bin/babel
$ podman run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### font2c

```bash
$ singularity exec <container> /usr/local/bin/font2c
$ podman run --it --rm --entrypoint /usr/local/bin/font2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/font2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gm

```bash
$ singularity exec <container> /usr/local/bin/gm
$ podman run --it --rm --entrypoint /usr/local/bin/gm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gocr

```bash
$ singularity exec <container> /usr/local/bin/gocr
$ podman run --it --rm --entrypoint /usr/local/bin/gocr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gocr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gocr.tcl

```bash
$ singularity exec <container> /usr/local/bin/gocr.tcl
$ podman run --it --rm --entrypoint /usr/local/bin/gocr.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gocr.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkbitmap

```bash
$ singularity exec <container> /usr/local/bin/mkbitmap
$ podman run --it --rm --entrypoint /usr/local/bin/mkbitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkbitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocrad

```bash
$ singularity exec <container> /usr/local/bin/ocrad
$ podman run --it --rm --entrypoint /usr/local/bin/ocrad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocrad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### osra

```bash
$ singularity exec <container> /usr/local/bin/osra
$ podman run --it --rm --entrypoint /usr/local/bin/osra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/osra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### potrace

```bash
$ singularity exec <container> /usr/local/bin/potrace
$ podman run --it --rm --entrypoint /usr/local/bin/potrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/potrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printimage

```bash
$ singularity exec <container> /usr/local/bin/printimage
$ podman run --it --rm --entrypoint /usr/local/bin/printimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printsplitimage

```bash
$ singularity exec <container> /usr/local/bin/printsplitimage
$ podman run --it --rm --entrypoint /usr/local/bin/printsplitimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printsplitimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printtiff

```bash
$ singularity exec <container> /usr/local/bin/printtiff
$ podman run --it --rm --entrypoint /usr/local/bin/printtiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printtiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitimage2pdf

```bash
$ singularity exec <container> /usr/local/bin/splitimage2pdf
$ podman run --it --rm --entrypoint /usr/local/bin/splitimage2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitimage2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tesseract

```bash
$ singularity exec <container> /usr/local/bin/tesseract
$ podman run --it --rm --entrypoint /usr/local/bin/tesseract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tesseract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wftopfa

```bash
$ singularity exec <container> /usr/local/bin/wftopfa
$ podman run --it --rm --entrypoint /usr/local/bin/wftopfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wftopfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractprotos

```bash
$ singularity exec <container> /usr/local/bin/xtractprotos
$ podman run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roundtrip

```bash
$ singularity exec <container> /usr/local/bin/roundtrip
$ podman run --it --rm --entrypoint /usr/local/bin/roundtrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roundtrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfdetach

```bash
$ singularity exec <container> /usr/local/bin/pdfdetach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdffonts

```bash
$ singularity exec <container> /usr/local/bin/pdffonts
$ podman run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfimages

```bash
$ singularity exec <container> /usr/local/bin/pdfimages
$ podman run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfinfo

```bash
$ singularity exec <container> /usr/local/bin/pdfinfo
$ podman run --it --rm --entrypoint /usr/local/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfseparate

```bash
$ singularity exec <container> /usr/local/bin/pdfseparate
$ podman run --it --rm --entrypoint /usr/local/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftocairo

```bash
$ singularity exec <container> /usr/local/bin/pdftocairo
$ podman run --it --rm --entrypoint /usr/local/bin/pdftocairo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftocairo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftohtml

```bash
$ singularity exec <container> /usr/local/bin/pdftohtml
$ podman run --it --rm --entrypoint /usr/local/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftoppm

```bash
$ singularity exec <container> /usr/local/bin/pdftoppm
$ podman run --it --rm --entrypoint /usr/local/bin/pdftoppm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftoppm   -v ${PWD} -w ${PWD} <container> -c " $@"
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