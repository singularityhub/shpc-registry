---
layout: container
name:  "quay.io/biocontainers/rptools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rptools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rptools/container.yaml"
updated_at: "2022-10-27 00:21:50.790443"
latest: "5.12.3"
container_url: "https://biocontainers.pro/tools/rptools"
aliases:
 - "filetype"
 - "httpx"
 - "pint-convert"
 - "search_zenodo"
 - "search_zenodo.py"
 - "slugify"
 - "upload_zenodo"
 - "upload_zenodo.py"
versions:
 - "5.12.3"
description: "shpc-registry automated BioContainers addition for rptools"
config: {"url": "https://biocontainers.pro/tools/rptools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rptools", "latest": {"5.12.3": "sha256:0577c0905fe77bdd385413292e06b0d650357b12f3fdff01960bf085bf9df7d6"}, "tags": {"5.12.3": "sha256:0577c0905fe77bdd385413292e06b0d650357b12f3fdff01960bf085bf9df7d6"}, "docker": "quay.io/biocontainers/rptools", "aliases": {"filetype": "/usr/local/bin/filetype", "httpx": "/usr/local/bin/httpx", "pint-convert": "/usr/local/bin/pint-convert", "search_zenodo": "/usr/local/bin/search_zenodo", "search_zenodo.py": "/usr/local/bin/search_zenodo.py", "slugify": "/usr/local/bin/slugify", "upload_zenodo": "/usr/local/bin/upload_zenodo", "upload_zenodo.py": "/usr/local/bin/upload_zenodo.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rptools.
shpc-registry automated BioContainers addition for rptools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rptools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rptools:5.12.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rptools/5.12.3
$ module help quay.io/biocontainers/rptools/5.12.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rptools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rptools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rptools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rptools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rptools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rptools-inspect-deffile:

```bash
$ singularity inspect -d <container>
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