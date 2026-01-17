---
layout: container
name:  "quay.io/biocontainers/remag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/remag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/remag/container.yaml"
updated_at: "2026-01-17 04:12:26.417837"
latest: "0.2.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/remag"
aliases:
 - "remag"
 - "protoc-28.3.0"
 - "torchfrtrace"
 - "pybind11-config"
 - "rich-click"
 - "torch_shm_manager"
 - "isympy"
 - "torchrun"
 - "markdown-it"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
 - "hwloc-info"
 - "hwloc-ls"
 - "hwloc-patch"
versions:
 - "0.1.2--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.1.5--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.2.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for remag"
config: {"url": "https://biocontainers.pro/tools/remag", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for remag", "latest": {"0.2.4--pyhdfd78af_0": "sha256:abb9a5420830fa7412030a3e0c255b3d8efc123d37d03a1ad16855c1949d7e9e"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:3ea61e2aef6383418a231dd851fc5810eebcdef8de90459a192191834177cf07", "0.2.0--pyhdfd78af_0": "sha256:b8eb60d1c67846177ebb2b068fbfa35ff7295387535ec1bc60b606bbbdf96289", "0.1.5--pyhdfd78af_0": "sha256:b63e1f4f9d42a393f87b433820e222592a4398d2784661feb947d7928bbfb071", "0.2.3--pyhdfd78af_0": "sha256:0d265ad4fce4207388383b67abf5262257c53087a71c00b9fa66cb2b974d71a0", "0.2.4--pyhdfd78af_0": "sha256:abb9a5420830fa7412030a3e0c255b3d8efc123d37d03a1ad16855c1949d7e9e"}, "docker": "quay.io/biocontainers/remag", "aliases": {"remag": "/usr/local/bin/remag", "protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "torchfrtrace": "/usr/local/bin/torchfrtrace", "pybind11-config": "/usr/local/bin/pybind11-config", "rich-click": "/usr/local/bin/rich-click", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "markdown-it": "/usr/local/bin/markdown-it", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/remag.
singularity registry hpc automated addition for remag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/remag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/remag:0.2.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/remag/0.2.4--pyhdfd78af_0
$ module help quay.io/biocontainers/remag/0.2.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### remag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### remag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### remag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### remag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### remag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### remag-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### remag

```bash
$ singularity exec <container> /usr/local/bin/remag
$ podman run --it --rm --entrypoint /usr/local/bin/remag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-diff

```bash
$ singularity exec <container> /usr/local/bin/hwloc-diff
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-topology

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-topology
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-info

```bash
$ singularity exec <container> /usr/local/bin/hwloc-info
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ls

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ls
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-patch

```bash
$ singularity exec <container> /usr/local/bin/hwloc-patch
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
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