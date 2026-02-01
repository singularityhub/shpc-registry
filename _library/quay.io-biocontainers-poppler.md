---
layout: container
name:  "quay.io/biocontainers/poppler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poppler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poppler/container.yaml"
updated_at: "2026-02-01 05:17:01.510627"
latest: "25.07.0"
container_url: "https://biocontainers.pro/tools/poppler"
aliases:
 - "pdfsig"
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
 - "tjbench"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
versions:
 - "25.07.0"
description: "singularity registry hpc automated addition for poppler"
config: {"url": "https://biocontainers.pro/tools/poppler", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for poppler", "latest": {"25.07.0": "sha256:7e2c2a14ff8dac2ba5abec10ce1239fb99371513a42a6f1e645c9045002a2042"}, "tags": {"25.07.0": "sha256:7e2c2a14ff8dac2ba5abec10ce1239fb99371513a42a6f1e645c9045002a2042"}, "docker": "quay.io/biocontainers/poppler", "aliases": {"pdfsig": "/usr/local/bin/pdfsig", "pdfattach": "/usr/local/bin/pdfattach", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages", "pdfinfo": "/usr/local/bin/pdfinfo", "pdfseparate": "/usr/local/bin/pdfseparate", "pdftocairo": "/usr/local/bin/pdftocairo", "pdftohtml": "/usr/local/bin/pdftohtml", "pdftoppm": "/usr/local/bin/pdftoppm", "pdftops": "/usr/local/bin/pdftops", "pdftotext": "/usr/local/bin/pdftotext", "pdfunite": "/usr/local/bin/pdfunite", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util", "tjbench": "/usr/local/bin/tjbench", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/poppler.
singularity registry hpc automated addition for poppler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poppler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poppler:25.07.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poppler/25.07.0
$ module help quay.io/biocontainers/poppler/25.07.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poppler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poppler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poppler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poppler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poppler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poppler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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