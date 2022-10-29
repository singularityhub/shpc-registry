---
layout: container
name:  "quay.io/biocontainers/rpbasicdesign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rpbasicdesign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rpbasicdesign/container.yaml"
updated_at: "2022-10-29 05:49:00.936862"
latest: "1.1.1"
container_url: "https://biocontainers.pro/tools/rpbasicdesign"
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
 - "2to3-3.9"
 - "brotli"
 - "cmark"
 - "csv2rdf"
 - "f2py3.9"
 - "fonttools"
 - "futurize"
 - "gif2h5"
 - "glpsol"
 - "h52gif"
versions:
 - "1.1.1"
description: "shpc-registry automated BioContainers addition for rpbasicdesign"
config: {"url": "https://biocontainers.pro/tools/rpbasicdesign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rpbasicdesign", "latest": {"1.1.1": "sha256:aaf1679ea79d30e824d51409e44152116c5c93fad9091c254932551171dab8e5"}, "tags": {"1.1.1": "sha256:aaf1679ea79d30e824d51409e44152116c5c93fad9091c254932551171dab8e5"}, "docker": "quay.io/biocontainers/rpbasicdesign", "aliases": {"depinfo": "/usr/local/bin/depinfo", "filetype": "/usr/local/bin/filetype", "httpx": "/usr/local/bin/httpx", "pint-convert": "/usr/local/bin/pint-convert", "search_zenodo": "/usr/local/bin/search_zenodo", "search_zenodo.py": "/usr/local/bin/search_zenodo.py", "slugify": "/usr/local/bin/slugify", "upload_zenodo": "/usr/local/bin/upload_zenodo", "upload_zenodo.py": "/usr/local/bin/upload_zenodo.py", "2to3-3.9": "/usr/local/bin/2to3-3.9", "brotli": "/usr/local/bin/brotli", "cmark": "/usr/local/bin/cmark", "csv2rdf": "/usr/local/bin/csv2rdf", "f2py3.9": "/usr/local/bin/f2py3.9", "fonttools": "/usr/local/bin/fonttools", "futurize": "/usr/local/bin/futurize", "gif2h5": "/usr/local/bin/gif2h5", "glpsol": "/usr/local/bin/glpsol", "h52gif": "/usr/local/bin/h52gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rpbasicdesign.
shpc-registry automated BioContainers addition for rpbasicdesign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rpbasicdesign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rpbasicdesign:1.1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rpbasicdesign/1.1.1
$ module help quay.io/biocontainers/rpbasicdesign/1.1.1
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


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
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