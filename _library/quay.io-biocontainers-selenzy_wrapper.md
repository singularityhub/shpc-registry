---
layout: container
name:  "quay.io/biocontainers/selenzy_wrapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/selenzy_wrapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/selenzy_wrapper/container.yaml"
updated_at: "2024-04-29 03:05:35.711583"
latest: "0.3.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/selenzy_wrapper"
aliases:
 - "depinfo"
 - "filetype"
 - "httpx"
 - "pint-convert"
 - "search_zenodo"
 - "search_zenodo.py"
 - "slugify"
 - "upload_zenodo"
 - "upload_zenodo.py"
 - "isympy"
 - "obfitall"
 - "obmm"
 - "xmlget"
 - "xmltext"
 - "unidecode"
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
 - "obrms"
 - "obrotamer"
 - "obrotate"
 - "obspectrophore"
 - "obsym"
 - "obtautomer"
 - "obthermo"
 - "aaindexextract"
 - "abiview"
versions:
 - "0.3.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_1"
description: "singularity registry hpc automated addition for selenzy_wrapper"
config: {"url": "https://biocontainers.pro/tools/selenzy_wrapper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for selenzy_wrapper", "latest": {"0.3.0--pyhdfd78af_1": "sha256:5715d388d9648b5668a4b7a7636c41a5eac5018dc1895a15f972d4a8525b1306"}, "tags": {"0.3.0--pyhdfd78af_0": "sha256:05f798f89781420eefdb7e46b69b0fcd263c4e49d3b8294221d7c2bbeb306f4a", "0.3.0--pyhdfd78af_1": "sha256:5715d388d9648b5668a4b7a7636c41a5eac5018dc1895a15f972d4a8525b1306"}, "docker": "quay.io/biocontainers/selenzy_wrapper", "aliases": {"depinfo": "/usr/local/bin/depinfo", "filetype": "/usr/local/bin/filetype", "httpx": "/usr/local/bin/httpx", "pint-convert": "/usr/local/bin/pint-convert", "search_zenodo": "/usr/local/bin/search_zenodo", "search_zenodo.py": "/usr/local/bin/search_zenodo.py", "slugify": "/usr/local/bin/slugify", "upload_zenodo": "/usr/local/bin/upload_zenodo", "upload_zenodo.py": "/usr/local/bin/upload_zenodo.py", "isympy": "/usr/local/bin/isympy", "obfitall": "/usr/local/bin/obfitall", "obmm": "/usr/local/bin/obmm", "xmlget": "/usr/local/bin/xmlget", "xmltext": "/usr/local/bin/xmltext", "unidecode": "/usr/local/bin/unidecode", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop", "obrms": "/usr/local/bin/obrms", "obrotamer": "/usr/local/bin/obrotamer", "obrotate": "/usr/local/bin/obrotate", "obspectrophore": "/usr/local/bin/obspectrophore", "obsym": "/usr/local/bin/obsym", "obtautomer": "/usr/local/bin/obtautomer", "obthermo": "/usr/local/bin/obthermo", "aaindexextract": "/usr/local/bin/aaindexextract", "abiview": "/usr/local/bin/abiview"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/selenzy_wrapper.
singularity registry hpc automated addition for selenzy_wrapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/selenzy_wrapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/selenzy_wrapper:0.3.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/selenzy_wrapper/0.3.0--pyhdfd78af_1
$ module help quay.io/biocontainers/selenzy_wrapper/0.3.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### selenzy_wrapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### selenzy_wrapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### selenzy_wrapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### selenzy_wrapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### selenzy_wrapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### selenzy_wrapper-inspect-deffile:

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


#### xmlget

```bash
$ singularity exec <container> /usr/local/bin/xmlget
$ podman run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmltext

```bash
$ singularity exec <container> /usr/local/bin/xmltext
$ podman run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### obrms

```bash
$ singularity exec <container> /usr/local/bin/obrms
$ podman run --it --rm --entrypoint /usr/local/bin/obrms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obrms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrotamer

```bash
$ singularity exec <container> /usr/local/bin/obrotamer
$ podman run --it --rm --entrypoint /usr/local/bin/obrotamer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obrotamer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrotate

```bash
$ singularity exec <container> /usr/local/bin/obrotate
$ podman run --it --rm --entrypoint /usr/local/bin/obrotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obrotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obspectrophore

```bash
$ singularity exec <container> /usr/local/bin/obspectrophore
$ podman run --it --rm --entrypoint /usr/local/bin/obspectrophore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obspectrophore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obsym

```bash
$ singularity exec <container> /usr/local/bin/obsym
$ podman run --it --rm --entrypoint /usr/local/bin/obsym   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obsym   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obtautomer

```bash
$ singularity exec <container> /usr/local/bin/obtautomer
$ podman run --it --rm --entrypoint /usr/local/bin/obtautomer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obtautomer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obthermo

```bash
$ singularity exec <container> /usr/local/bin/obthermo
$ podman run --it --rm --entrypoint /usr/local/bin/obthermo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obthermo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abiview

```bash
$ singularity exec <container> /usr/local/bin/abiview
$ podman run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
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