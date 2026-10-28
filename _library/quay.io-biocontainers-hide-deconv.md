---
layout: container
name:  "quay.io/biocontainers/hide-deconv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hide-deconv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hide-deconv/container.yaml"
updated_at: "2026-10-28 08:14:33.056401"
latest: "0.4.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hide-deconv"
aliases:
 - "hide-deconv"
 - "jupyter-builder"
 - "mistune"
 - "scikit-build"
 - "scikit-build-core"
 - "jlpm"
 - "jupyter-lab"
 - "jupyter-labextension"
 - "jupyter-labhub"
 - "jupyter-events"
 - "pyjson5"
 - "jupyter-server"
 - "session-info2"
 - "debugpy-adapter"
 - "jupyter-console"
 - "session-info"
 - "debugpy"
 - "cffi-gen-src"
 - "zarr"
 - "send2trash"
 - "wsdump"
 - "jupyter-dejavu"
 - "jsonpointer"
 - "jupyter-execute"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "dotenv"
 - "jupyter-notebook"
versions:
 - "0.4.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for hide-deconv"
config: {"url": "https://biocontainers.pro/tools/hide-deconv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hide-deconv", "latest": {"0.4.2--pyhdfd78af_0": "sha256:a5d7b2d31f034d2f8c0809e3a62715dfaad57a4080edd54b90b72f25c90a4fb5"}, "tags": {"0.4.2--pyhdfd78af_0": "sha256:a5d7b2d31f034d2f8c0809e3a62715dfaad57a4080edd54b90b72f25c90a4fb5"}, "docker": "quay.io/biocontainers/hide-deconv", "aliases": {"hide-deconv": "/usr/local/bin/hide-deconv", "jupyter-builder": "/usr/local/bin/jupyter-builder", "mistune": "/usr/local/bin/mistune", "scikit-build": "/usr/local/bin/scikit-build", "scikit-build-core": "/usr/local/bin/scikit-build-core", "jlpm": "/usr/local/bin/jlpm", "jupyter-lab": "/usr/local/bin/jupyter-lab", "jupyter-labextension": "/usr/local/bin/jupyter-labextension", "jupyter-labhub": "/usr/local/bin/jupyter-labhub", "jupyter-events": "/usr/local/bin/jupyter-events", "pyjson5": "/usr/local/bin/pyjson5", "jupyter-server": "/usr/local/bin/jupyter-server", "session-info2": "/usr/local/bin/session-info2", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "jupyter-console": "/usr/local/bin/jupyter-console", "session-info": "/usr/local/bin/session-info", "debugpy": "/usr/local/bin/debugpy", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "zarr": "/usr/local/bin/zarr", "send2trash": "/usr/local/bin/send2trash", "wsdump": "/usr/local/bin/wsdump", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jsonpointer": "/usr/local/bin/jsonpointer", "jupyter-execute": "/usr/local/bin/jupyter-execute", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "dotenv": "/usr/local/bin/dotenv", "jupyter-notebook": "/usr/local/bin/jupyter-notebook"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hide-deconv.
singularity registry hpc automated addition for hide-deconv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hide-deconv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hide-deconv:0.4.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hide-deconv/0.4.2--pyhdfd78af_0
$ module help quay.io/biocontainers/hide-deconv/0.4.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hide-deconv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hide-deconv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hide-deconv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hide-deconv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hide-deconv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hide-deconv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hide-deconv

```bash
$ singularity exec <container> /usr/local/bin/hide-deconv
$ podman run --it --rm --entrypoint /usr/local/bin/hide-deconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hide-deconv   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### scikit-build

```bash
$ singularity exec <container> /usr/local/bin/scikit-build
$ podman run --it --rm --entrypoint /usr/local/bin/scikit-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scikit-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scikit-build-core

```bash
$ singularity exec <container> /usr/local/bin/scikit-build-core
$ podman run --it --rm --entrypoint /usr/local/bin/scikit-build-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scikit-build-core   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info

```bash
$ singularity exec <container> /usr/local/bin/session-info
$ podman run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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