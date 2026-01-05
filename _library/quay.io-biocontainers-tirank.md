---
layout: container
name:  "quay.io/biocontainers/tirank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tirank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tirank/container.yaml"
updated_at: "2026-01-05 04:13:56.012696"
latest: "0.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tirank"
aliases:
 - "crc32c"
 - "dash-update-components"
 - "gseapy"
 - "hf"
 - "optuna"
 - "tiny-agents"
 - "zarr"
 - "dec265"
 - "plotly_get_chrome"
 - "alembic"
 - "renderer"
 - "dash-generate-components"
 - "protoc-31.1.0"
 - "protoc-gen-upb-31.1.0"
 - "protoc-gen-upbdefs-31.1.0"
 - "torchfrtrace"
 - "x265"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "httpx"
 - "pybind11-config"
 - "mako-render"
 - "torch_shm_manager"
 - "SvtAv1EncApp"
 - "dav1d"
 - "aomdec"
 - "aomenc"
 - "flask"
 - "h5fuse"
 - "isympy"
 - "torchrun"
 - "scanpy"
versions:
 - "0.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for tirank"
config: {"url": "https://biocontainers.pro/tools/tirank", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tirank", "latest": {"0.1.3--pyhdfd78af_0": "sha256:6cc1bba0d3371079cd75a2e98206f2dcb541bffe578f76c17418e0b7399f66c7"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:6cc1bba0d3371079cd75a2e98206f2dcb541bffe578f76c17418e0b7399f66c7"}, "docker": "quay.io/biocontainers/tirank", "aliases": {"crc32c": "/usr/local/bin/crc32c", "dash-update-components": "/usr/local/bin/dash-update-components", "gseapy": "/usr/local/bin/gseapy", "hf": "/usr/local/bin/hf", "optuna": "/usr/local/bin/optuna", "tiny-agents": "/usr/local/bin/tiny-agents", "zarr": "/usr/local/bin/zarr", "dec265": "/usr/local/bin/dec265", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "alembic": "/usr/local/bin/alembic", "renderer": "/usr/local/bin/renderer", "dash-generate-components": "/usr/local/bin/dash-generate-components", "protoc-31.1.0": "/usr/local/bin/protoc-31.1.0", "protoc-gen-upb-31.1.0": "/usr/local/bin/protoc-gen-upb-31.1.0", "protoc-gen-upbdefs-31.1.0": "/usr/local/bin/protoc-gen-upbdefs-31.1.0", "torchfrtrace": "/usr/local/bin/torchfrtrace", "x265": "/usr/local/bin/x265", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "httpx": "/usr/local/bin/httpx", "pybind11-config": "/usr/local/bin/pybind11-config", "mako-render": "/usr/local/bin/mako-render", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "SvtAv1EncApp": "/usr/local/bin/SvtAv1EncApp", "dav1d": "/usr/local/bin/dav1d", "aomdec": "/usr/local/bin/aomdec", "aomenc": "/usr/local/bin/aomenc", "flask": "/usr/local/bin/flask", "h5fuse": "/usr/local/bin/h5fuse", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "scanpy": "/usr/local/bin/scanpy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tirank.
singularity registry hpc automated addition for tirank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tirank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tirank:0.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tirank/0.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/tirank/0.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tirank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tirank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tirank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tirank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tirank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tirank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32c

```bash
$ singularity exec <container> /usr/local/bin/crc32c
$ podman run --it --rm --entrypoint /usr/local/bin/crc32c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-update-components

```bash
$ singularity exec <container> /usr/local/bin/dash-update-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gseapy

```bash
$ singularity exec <container> /usr/local/bin/gseapy
$ podman run --it --rm --entrypoint /usr/local/bin/gseapy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gseapy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf

```bash
$ singularity exec <container> /usr/local/bin/hf
$ podman run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optuna

```bash
$ singularity exec <container> /usr/local/bin/optuna
$ podman run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zarr

```bash
$ singularity exec <container> /usr/local/bin/zarr
$ podman run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dec265

```bash
$ singularity exec <container> /usr/local/bin/dec265
$ podman run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x265

```bash
$ singularity exec <container> /usr/local/bin/x265
$ podman run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SvtAv1EncApp

```bash
$ singularity exec <container> /usr/local/bin/SvtAv1EncApp
$ podman run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dav1d

```bash
$ singularity exec <container> /usr/local/bin/dav1d
$ podman run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomdec

```bash
$ singularity exec <container> /usr/local/bin/aomdec
$ podman run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomenc

```bash
$ singularity exec <container> /usr/local/bin/aomenc
$ podman run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
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