---
layout: container
name:  "quay.io/biocontainers/rpbasicdesign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rpbasicdesign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rpbasicdesign/container.yaml"
updated_at: "2025-04-08 03:14:12.434017"
latest: "1.2.2"
container_url: "https://biocontainers.pro/tools/rpbasicdesign"
aliases:
 - "depinfo"
 - "filetype"
 - "httpx"
 - "isympy"
 - "obfitall"
 - "obmm"
 - "pint-convert"
 - "search_zenodo"
 - "search_zenodo.py"
 - "slugify"
 - "upload_zenodo"
 - "upload_zenodo.py"
 - "obabel"
 - "obconformer"
 - "obdistgen"
 - "obenergy"
 - "obfit"
 - "obgen"
 - "obgrep"
 - "obminimize"
 - "obprobe"
 - "obprop"
versions:
 - "1.1.1"
 - "1.2.2"
description: "shpc-registry automated BioContainers addition for rpbasicdesign"
config: {"url": "https://biocontainers.pro/tools/rpbasicdesign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rpbasicdesign", "latest": {"1.2.2": "sha256:f59d1c386b9a480db60ce2de15181a56ae8c88027219c361c3f954e16d2f0afa"}, "tags": {"1.1.1": "sha256:aaf1679ea79d30e824d51409e44152116c5c93fad9091c254932551171dab8e5", "1.2.2": "sha256:f59d1c386b9a480db60ce2de15181a56ae8c88027219c361c3f954e16d2f0afa"}, "docker": "quay.io/biocontainers/rpbasicdesign", "aliases": {"depinfo": "/usr/local/bin/depinfo", "filetype": "/usr/local/bin/filetype", "httpx": "/usr/local/bin/httpx", "isympy": "/usr/local/bin/isympy", "obfitall": "/usr/local/bin/obfitall", "obmm": "/usr/local/bin/obmm", "pint-convert": "/usr/local/bin/pint-convert", "search_zenodo": "/usr/local/bin/search_zenodo", "search_zenodo.py": "/usr/local/bin/search_zenodo.py", "slugify": "/usr/local/bin/slugify", "upload_zenodo": "/usr/local/bin/upload_zenodo", "upload_zenodo.py": "/usr/local/bin/upload_zenodo.py", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rpbasicdesign.
shpc-registry automated BioContainers addition for rpbasicdesign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rpbasicdesign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rpbasicdesign:1.2.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rpbasicdesign/1.2.2
$ module help quay.io/biocontainers/rpbasicdesign/1.2.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rpbasicdesign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rpbasicdesign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rpbasicdesign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rpbasicdesign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rpbasicdesign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rpbasicdesign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### depinfo

```bash
$ singularity exec <container> /usr/local/bin/depinfo
$ podman run --it --rm --entrypoint /usr/local/bin/depinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/depinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filetype

```bash
$ singularity exec <container> /usr/local/bin/filetype
$ podman run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfitall

```bash
$ singularity exec <container> /usr/local/bin/obfitall
$ podman run --it --rm --entrypoint /usr/local/bin/obfitall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfitall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obmm

```bash
$ singularity exec <container> /usr/local/bin/obmm
$ podman run --it --rm --entrypoint /usr/local/bin/obmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pint-convert

```bash
$ singularity exec <container> /usr/local/bin/pint-convert
$ podman run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### search_zenodo

```bash
$ singularity exec <container> /usr/local/bin/search_zenodo
$ podman run --it --rm --entrypoint /usr/local/bin/search_zenodo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/search_zenodo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### search_zenodo.py

```bash
$ singularity exec <container> /usr/local/bin/search_zenodo.py
$ podman run --it --rm --entrypoint /usr/local/bin/search_zenodo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/search_zenodo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upload_zenodo

```bash
$ singularity exec <container> /usr/local/bin/upload_zenodo
$ podman run --it --rm --entrypoint /usr/local/bin/upload_zenodo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upload_zenodo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upload_zenodo.py

```bash
$ singularity exec <container> /usr/local/bin/upload_zenodo.py
$ podman run --it --rm --entrypoint /usr/local/bin/upload_zenodo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upload_zenodo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obabel

```bash
$ singularity exec <container> /usr/local/bin/obabel
$ podman run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obconformer

```bash
$ singularity exec <container> /usr/local/bin/obconformer
$ podman run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obdistgen

```bash
$ singularity exec <container> /usr/local/bin/obdistgen
$ podman run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obenergy

```bash
$ singularity exec <container> /usr/local/bin/obenergy
$ podman run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfit

```bash
$ singularity exec <container> /usr/local/bin/obfit
$ podman run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgen

```bash
$ singularity exec <container> /usr/local/bin/obgen
$ podman run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgrep

```bash
$ singularity exec <container> /usr/local/bin/obgrep
$ podman run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obminimize

```bash
$ singularity exec <container> /usr/local/bin/obminimize
$ podman run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprobe

```bash
$ singularity exec <container> /usr/local/bin/obprobe
$ podman run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprop

```bash
$ singularity exec <container> /usr/local/bin/obprop
$ podman run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
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