---
layout: container
name:  "quay.io/biocontainers/spatialsnake"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spatialsnake/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spatialsnake/container.yaml"
updated_at: "2026-10-10 19:28:27.897886"
latest: "0.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/spatialsnake"
aliases:
 - "jupyter-builder"
 - "mistune"
 - "ome-zarr-models"
 - "ome_zarr"
 - "pint-convert"
 - "spatialsnake"
 - "jlpm"
 - "jupyter-lab"
 - "jupyter-labextension"
 - "jupyter-labhub"
 - "jupyter-events"
 - "pyjson5"
 - "ojph_compress"
 - "ojph_expand"
 - "jupyter-server"
 - "session-info2"
 - "debugpy-adapter"
 - "session-info"
 - "jupyter-console"
 - "debugpy"
 - "cffi-gen-src"
 - "zarr"
 - "send2trash"
 - "wsdump"
 - "jsonpointer"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "dotenv"
 - "jupyter-notebook"
 - "tiff2fsspec"
 - "tiffcomment"
versions:
 - "0.0.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for spatialsnake"
config: {"url": "https://biocontainers.pro/tools/spatialsnake", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spatialsnake", "latest": {"0.0.4--pyhdfd78af_0": "sha256:9dd3e726b9aae59ad4539782e5bdfdb380bd329d3e615e9a30852696151a9eb5"}, "tags": {"0.0.4--pyhdfd78af_0": "sha256:9dd3e726b9aae59ad4539782e5bdfdb380bd329d3e615e9a30852696151a9eb5"}, "docker": "quay.io/biocontainers/spatialsnake", "aliases": {"jupyter-builder": "/usr/local/bin/jupyter-builder", "mistune": "/usr/local/bin/mistune", "ome-zarr-models": "/usr/local/bin/ome-zarr-models", "ome_zarr": "/usr/local/bin/ome_zarr", "pint-convert": "/usr/local/bin/pint-convert", "spatialsnake": "/usr/local/bin/spatialsnake", "jlpm": "/usr/local/bin/jlpm", "jupyter-lab": "/usr/local/bin/jupyter-lab", "jupyter-labextension": "/usr/local/bin/jupyter-labextension", "jupyter-labhub": "/usr/local/bin/jupyter-labhub", "jupyter-events": "/usr/local/bin/jupyter-events", "pyjson5": "/usr/local/bin/pyjson5", "ojph_compress": "/usr/local/bin/ojph_compress", "ojph_expand": "/usr/local/bin/ojph_expand", "jupyter-server": "/usr/local/bin/jupyter-server", "session-info2": "/usr/local/bin/session-info2", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "session-info": "/usr/local/bin/session-info", "jupyter-console": "/usr/local/bin/jupyter-console", "debugpy": "/usr/local/bin/debugpy", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "zarr": "/usr/local/bin/zarr", "send2trash": "/usr/local/bin/send2trash", "wsdump": "/usr/local/bin/wsdump", "jsonpointer": "/usr/local/bin/jsonpointer", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "dotenv": "/usr/local/bin/dotenv", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "tiffcomment": "/usr/local/bin/tiffcomment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spatialsnake.
singularity registry hpc automated addition for spatialsnake
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spatialsnake
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spatialsnake:0.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spatialsnake/0.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/spatialsnake/0.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spatialsnake-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spatialsnake-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spatialsnake-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spatialsnake-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spatialsnake-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spatialsnake-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jupyter-builder

```bash
$ singularity exec <container> /usr/local/bin/jupyter-builder
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mistune

```bash
$ singularity exec <container> /usr/local/bin/mistune
$ podman run --it --rm --entrypoint /usr/local/bin/mistune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mistune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ome-zarr-models

```bash
$ singularity exec <container> /usr/local/bin/ome-zarr-models
$ podman run --it --rm --entrypoint /usr/local/bin/ome-zarr-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ome-zarr-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ome_zarr

```bash
$ singularity exec <container> /usr/local/bin/ome_zarr
$ podman run --it --rm --entrypoint /usr/local/bin/ome_zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ome_zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pint-convert

```bash
$ singularity exec <container> /usr/local/bin/pint-convert
$ podman run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spatialsnake

```bash
$ singularity exec <container> /usr/local/bin/spatialsnake
$ podman run --it --rm --entrypoint /usr/local/bin/spatialsnake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spatialsnake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlpm

```bash
$ singularity exec <container> /usr/local/bin/jlpm
$ podman run --it --rm --entrypoint /usr/local/bin/jlpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-lab

```bash
$ singularity exec <container> /usr/local/bin/jupyter-lab
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-lab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-lab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-labextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-labextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-labextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-labextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-labhub

```bash
$ singularity exec <container> /usr/local/bin/jupyter-labhub
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-labhub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-labhub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-events

```bash
$ singularity exec <container> /usr/local/bin/jupyter-events
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_compress

```bash
$ singularity exec <container> /usr/local/bin/ojph_compress
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_expand

```bash
$ singularity exec <container> /usr/local/bin/ojph_expand
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info2

```bash
$ singularity exec <container> /usr/local/bin/session-info2
$ podman run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info

```bash
$ singularity exec <container> /usr/local/bin/session-info
$ podman run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zarr

```bash
$ singularity exec <container> /usr/local/bin/zarr
$ podman run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcomment

```bash
$ singularity exec <container> /usr/local/bin/tiffcomment
$ podman run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
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