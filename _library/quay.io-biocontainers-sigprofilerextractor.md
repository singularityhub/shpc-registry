---
layout: container
name:  "quay.io/biocontainers/sigprofilerextractor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sigprofilerextractor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sigprofilerextractor/container.yaml"
updated_at: "2025-11-07 03:59:45.619947"
latest: "1.2.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sigprofilerextractor"
aliases:
 - "SigProfilerAssignment"
 - "SigProfilerExtractor"
 - "SigProfilerMatrixGenerator"
 - "SigProfilerPlotting"
 - "protoc-29.3.0"
 - "protoc-gen-upb"
 - "protoc-gen-upb-29.3.0"
 - "protoc-gen-upb_minitable"
 - "protoc-gen-upb_minitable-29.3.0"
 - "protoc-gen-upbdefs"
 - "protoc-gen-upbdefs-29.3.0"
 - "torchfrtrace"
 - "pybind11-config"
 - "torch_shm_manager"
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
 - "isympy"
 - "torchrun"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "idle3.13"
versions:
 - "1.2.1--pyhdfd78af_0"
 - "1.2.2--pyhdfd78af_0"
 - "1.2.3--pyhdfd78af_0"
 - "1.2.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sigprofilerextractor"
config: {"url": "https://biocontainers.pro/tools/sigprofilerextractor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sigprofilerextractor", "latest": {"1.2.4--pyhdfd78af_0": "sha256:c33c7c3c300e66986ad4894c7f065be7a67fe6c466a1a2a95869c444063f7d12"}, "tags": {"1.2.1--pyhdfd78af_0": "sha256:4645554aef7f52c03fd17ec204f03522616caf365ec859b31a0ec12281c1db52", "1.2.2--pyhdfd78af_0": "sha256:62b92f3cbe2a16f3f3590cc3acaca7c89860adf7fa1e42d1897edb2219721923", "1.2.3--pyhdfd78af_0": "sha256:24b772bf3b7a6038a8a2e33471904edaecd6049278b7cb3623aaed2513087f93", "1.2.4--pyhdfd78af_0": "sha256:c33c7c3c300e66986ad4894c7f065be7a67fe6c466a1a2a95869c444063f7d12"}, "docker": "quay.io/biocontainers/sigprofilerextractor", "aliases": {"SigProfilerAssignment": "/usr/local/bin/SigProfilerAssignment", "SigProfilerExtractor": "/usr/local/bin/SigProfilerExtractor", "SigProfilerMatrixGenerator": "/usr/local/bin/SigProfilerMatrixGenerator", "SigProfilerPlotting": "/usr/local/bin/SigProfilerPlotting", "protoc-29.3.0": "/usr/local/bin/protoc-29.3.0", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upb-29.3.0": "/usr/local/bin/protoc-gen-upb-29.3.0", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "protoc-gen-upb_minitable-29.3.0": "/usr/local/bin/protoc-gen-upb_minitable-29.3.0", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "protoc-gen-upbdefs-29.3.0": "/usr/local/bin/protoc-gen-upbdefs-29.3.0", "torchfrtrace": "/usr/local/bin/torchfrtrace", "pybind11-config": "/usr/local/bin/pybind11-config", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "pdfsig": "/usr/local/bin/pdfsig", "pdfattach": "/usr/local/bin/pdfattach", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages", "pdfinfo": "/usr/local/bin/pdfinfo", "pdfseparate": "/usr/local/bin/pdfseparate", "pdftocairo": "/usr/local/bin/pdftocairo", "pdftohtml": "/usr/local/bin/pdftohtml", "pdftoppm": "/usr/local/bin/pdftoppm", "pdftops": "/usr/local/bin/pdftops", "pdftotext": "/usr/local/bin/pdftotext", "pdfunite": "/usr/local/bin/pdfunite", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "idle3.13": "/usr/local/bin/idle3.13"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sigprofilerextractor.
singularity registry hpc automated addition for sigprofilerextractor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sigprofilerextractor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sigprofilerextractor:1.2.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sigprofilerextractor/1.2.4--pyhdfd78af_0
$ module help quay.io/biocontainers/sigprofilerextractor/1.2.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sigprofilerextractor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sigprofilerextractor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sigprofilerextractor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sigprofilerextractor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sigprofilerextractor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sigprofilerextractor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SigProfilerAssignment

```bash
$ singularity exec <container> /usr/local/bin/SigProfilerAssignment
$ podman run --it --rm --entrypoint /usr/local/bin/SigProfilerAssignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SigProfilerAssignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SigProfilerExtractor

```bash
$ singularity exec <container> /usr/local/bin/SigProfilerExtractor
$ podman run --it --rm --entrypoint /usr/local/bin/SigProfilerExtractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SigProfilerExtractor   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### protoc-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
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