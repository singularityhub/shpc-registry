---
layout: container
name:  "quay.io/biocontainers/sigprofilerassignment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sigprofilerassignment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sigprofilerassignment/container.yaml"
updated_at: "2025-01-02 03:05:28.917351"
latest: "0.1.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sigprofilerassignment"
aliases:
 - "SigProfilerAssignment"
 - "SigProfilerMatrixGenerator"
 - "SigProfilerPlotting"
 - "bsdunzip"
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
 - "mupdf-x11"
 - "mupdf-x11-curl"
 - "muraster"
 - "mutool"
 - "pymupdf"
 - "tesseract"
 - "xtractprotos"
 - "pdfsig"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "pdfattach"
 - "pdfdetach"
 - "pdffonts"
 - "pdfimages"
 - "pdfinfo"
 - "pdfseparate"
 - "pdftocairo"
 - "pdftohtml"
 - "pdftoppm"
 - "pdftops"
 - "pdftotext"
 - "pdfunite"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
versions:
 - "0.1.6--pyhdfd78af_0"
 - "0.1.7--pyhdfd78af_0"
 - "0.1.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sigprofilerassignment"
config: {"url": "https://biocontainers.pro/tools/sigprofilerassignment", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sigprofilerassignment", "latest": {"0.1.8--pyhdfd78af_0": "sha256:478f3926eb845ddfea1060ec74fb77bd3d4c329fbc517d5d8aaccca678916f48"}, "tags": {"0.1.6--pyhdfd78af_0": "sha256:62a0a947a34cc109e472cffb74840f0303995aaaa784a24ca38321b278034f4a", "0.1.7--pyhdfd78af_0": "sha256:ad1ff72282ca377b5cd3260e76e2437c0af6ae7c8f46e1026e8db51c6944866b", "0.1.8--pyhdfd78af_0": "sha256:478f3926eb845ddfea1060ec74fb77bd3d4c329fbc517d5d8aaccca678916f48"}, "docker": "quay.io/biocontainers/sigprofilerassignment", "aliases": {"SigProfilerAssignment": "/usr/local/bin/SigProfilerAssignment", "SigProfilerMatrixGenerator": "/usr/local/bin/SigProfilerMatrixGenerator", "SigProfilerPlotting": "/usr/local/bin/SigProfilerPlotting", "bsdunzip": "/usr/local/bin/bsdunzip", "convertfilestopdf": "/usr/local/bin/convertfilestopdf", "convertfilestops": "/usr/local/bin/convertfilestops", "convertformat": "/usr/local/bin/convertformat", "convertsegfilestopdf": "/usr/local/bin/convertsegfilestopdf", "convertsegfilestops": "/usr/local/bin/convertsegfilestops", "converttopdf": "/usr/local/bin/converttopdf", "converttops": "/usr/local/bin/converttops", "fileinfo": "/usr/local/bin/fileinfo", "imagetops": "/usr/local/bin/imagetops", "jbig2dec": "/usr/local/bin/jbig2dec", "mupdf-gl": "/usr/local/bin/mupdf-gl", "mupdf-x11": "/usr/local/bin/mupdf-x11", "mupdf-x11-curl": "/usr/local/bin/mupdf-x11-curl", "muraster": "/usr/local/bin/muraster", "mutool": "/usr/local/bin/mutool", "pymupdf": "/usr/local/bin/pymupdf", "tesseract": "/usr/local/bin/tesseract", "xtractprotos": "/usr/local/bin/xtractprotos", "pdfsig": "/usr/local/bin/pdfsig", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "pdfattach": "/usr/local/bin/pdfattach", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages", "pdfinfo": "/usr/local/bin/pdfinfo", "pdfseparate": "/usr/local/bin/pdfseparate", "pdftocairo": "/usr/local/bin/pdftocairo", "pdftohtml": "/usr/local/bin/pdftohtml", "pdftoppm": "/usr/local/bin/pdftoppm", "pdftops": "/usr/local/bin/pdftops", "pdftotext": "/usr/local/bin/pdftotext", "pdfunite": "/usr/local/bin/pdfunite", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sigprofilerassignment.
singularity registry hpc automated addition for sigprofilerassignment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sigprofilerassignment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sigprofilerassignment:0.1.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sigprofilerassignment/0.1.8--pyhdfd78af_0
$ module help quay.io/biocontainers/sigprofilerassignment/0.1.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sigprofilerassignment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sigprofilerassignment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sigprofilerassignment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sigprofilerassignment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sigprofilerassignment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sigprofilerassignment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SigProfilerAssignment

```bash
$ singularity exec <container> /usr/local/bin/SigProfilerAssignment
$ podman run --it --rm --entrypoint /usr/local/bin/SigProfilerAssignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SigProfilerAssignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SigProfilerMatrixGenerator

```bash
$ singularity exec <container> /usr/local/bin/SigProfilerMatrixGenerator
$ podman run --it --rm --entrypoint /usr/local/bin/SigProfilerMatrixGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SigProfilerMatrixGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SigProfilerPlotting

```bash
$ singularity exec <container> /usr/local/bin/SigProfilerPlotting
$ podman run --it --rm --entrypoint /usr/local/bin/SigProfilerPlotting   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SigProfilerPlotting   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mupdf-x11

```bash
$ singularity exec <container> /usr/local/bin/mupdf-x11
$ podman run --it --rm --entrypoint /usr/local/bin/mupdf-x11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mupdf-x11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mupdf-x11-curl

```bash
$ singularity exec <container> /usr/local/bin/mupdf-x11-curl
$ podman run --it --rm --entrypoint /usr/local/bin/mupdf-x11-curl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mupdf-x11-curl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pdfattach

```bash
$ singularity exec <container> /usr/local/bin/pdfattach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pdftops

```bash
$ singularity exec <container> /usr/local/bin/pdftops
$ podman run --it --rm --entrypoint /usr/local/bin/pdftops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftotext

```bash
$ singularity exec <container> /usr/local/bin/pdftotext
$ podman run --it --rm --entrypoint /usr/local/bin/pdftotext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftotext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfunite

```bash
$ singularity exec <container> /usr/local/bin/pdfunite
$ podman run --it --rm --entrypoint /usr/local/bin/pdfunite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfunite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nspr-config

```bash
$ singularity exec <container> /usr/local/bin/nspr-config
$ podman run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nss-config

```bash
$ singularity exec <container> /usr/local/bin/nss-config
$ podman run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pk12util

```bash
$ singularity exec <container> /usr/local/bin/pk12util
$ podman run --it --rm --entrypoint /usr/local/bin/pk12util   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pk12util   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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