---
layout: container
name:  "quay.io/biocontainers/bioconda-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconda-utils/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconda-utils/container.yaml"
updated_at: "2022-10-29 05:56:46.736921"
latest: "1.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconda-utils"
aliases:
 - "anaconda"
 - "binstar"
 - "bioconda-utils"
 - "boa"
 - "celery"
 - "conda-build"
 - "conda-convert"
 - "conda-debug"
 - "conda-develop"
 - "conda-index"
 - "conda-inspect"
 - "conda-mambabuild"
 - "conda-metapackage"
 - "conda-render"
 - "conda-server"
 - "conda-skeleton"
 - "conda-verify"
 - "involucro"
 - "mamba-package"
 - "patchelf"
 - "pkginfo"
 - "pyjson5"
 - "rg"
 - "scalar"
 - "skopeo"
 - "watchgod"
 - "2to3-3.7"
 - "acyclic"
 - "annotate"
 - "bcomps"
 - "bdftogd"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "ccomps"
 - "chardetect"
versions:
 - "1.1.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconda-utils"
config: {"url": "https://biocontainers.pro/tools/bioconda-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconda-utils", "latest": {"1.1.5--pyhdfd78af_0": "sha256:291aa9841d34f183b13b318576edf2a8b01659a96f08c87bc874950fdc05360f"}, "tags": {"1.1.5--pyhdfd78af_0": "sha256:291aa9841d34f183b13b318576edf2a8b01659a96f08c87bc874950fdc05360f"}, "docker": "quay.io/biocontainers/bioconda-utils", "aliases": {"anaconda": "/usr/local/bin/anaconda", "binstar": "/usr/local/bin/binstar", "bioconda-utils": "/usr/local/bin/bioconda-utils", "boa": "/usr/local/bin/boa", "celery": "/usr/local/bin/celery", "conda-build": "/usr/local/bin/conda-build", "conda-convert": "/usr/local/bin/conda-convert", "conda-debug": "/usr/local/bin/conda-debug", "conda-develop": "/usr/local/bin/conda-develop", "conda-index": "/usr/local/bin/conda-index", "conda-inspect": "/usr/local/bin/conda-inspect", "conda-mambabuild": "/usr/local/bin/conda-mambabuild", "conda-metapackage": "/usr/local/bin/conda-metapackage", "conda-render": "/usr/local/bin/conda-render", "conda-server": "/usr/local/bin/conda-server", "conda-skeleton": "/usr/local/bin/conda-skeleton", "conda-verify": "/usr/local/bin/conda-verify", "involucro": "/usr/local/bin/involucro", "mamba-package": "/usr/local/bin/mamba-package", "patchelf": "/usr/local/bin/patchelf", "pkginfo": "/usr/local/bin/pkginfo", "pyjson5": "/usr/local/bin/pyjson5", "rg": "/usr/local/bin/rg", "scalar": "/usr/local/bin/scalar", "skopeo": "/usr/local/bin/skopeo", "watchgod": "/usr/local/bin/watchgod", "2to3-3.7": "/usr/local/bin/2to3-3.7", "acyclic": "/usr/local/bin/acyclic", "annotate": "/usr/local/bin/annotate", "bcomps": "/usr/local/bin/bcomps", "bdftogd": "/usr/local/bin/bdftogd", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "ccomps": "/usr/local/bin/ccomps", "chardetect": "/usr/local/bin/chardetect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconda-utils.
shpc-registry automated BioContainers addition for bioconda-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconda-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconda-utils:1.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconda-utils/1.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/bioconda-utils/1.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconda-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconda-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconda-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconda-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconda-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconda-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anaconda

```bash
$ singularity exec <container> /usr/local/bin/anaconda
$ podman run --it --rm --entrypoint /usr/local/bin/anaconda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anaconda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binstar

```bash
$ singularity exec <container> /usr/local/bin/binstar
$ podman run --it --rm --entrypoint /usr/local/bin/binstar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binstar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconda-utils

```bash
$ singularity exec <container> /usr/local/bin/bioconda-utils
$ podman run --it --rm --entrypoint /usr/local/bin/bioconda-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconda-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### boa

```bash
$ singularity exec <container> /usr/local/bin/boa
$ podman run --it --rm --entrypoint /usr/local/bin/boa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### celery

```bash
$ singularity exec <container> /usr/local/bin/celery
$ podman run --it --rm --entrypoint /usr/local/bin/celery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/celery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-build

```bash
$ singularity exec <container> /usr/local/bin/conda-build
$ podman run --it --rm --entrypoint /usr/local/bin/conda-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-convert

```bash
$ singularity exec <container> /usr/local/bin/conda-convert
$ podman run --it --rm --entrypoint /usr/local/bin/conda-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-debug

```bash
$ singularity exec <container> /usr/local/bin/conda-debug
$ podman run --it --rm --entrypoint /usr/local/bin/conda-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-develop

```bash
$ singularity exec <container> /usr/local/bin/conda-develop
$ podman run --it --rm --entrypoint /usr/local/bin/conda-develop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-develop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-index

```bash
$ singularity exec <container> /usr/local/bin/conda-index
$ podman run --it --rm --entrypoint /usr/local/bin/conda-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-inspect

```bash
$ singularity exec <container> /usr/local/bin/conda-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/conda-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-mambabuild

```bash
$ singularity exec <container> /usr/local/bin/conda-mambabuild
$ podman run --it --rm --entrypoint /usr/local/bin/conda-mambabuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-mambabuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-metapackage

```bash
$ singularity exec <container> /usr/local/bin/conda-metapackage
$ podman run --it --rm --entrypoint /usr/local/bin/conda-metapackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-metapackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-render

```bash
$ singularity exec <container> /usr/local/bin/conda-render
$ podman run --it --rm --entrypoint /usr/local/bin/conda-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-server

```bash
$ singularity exec <container> /usr/local/bin/conda-server
$ podman run --it --rm --entrypoint /usr/local/bin/conda-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-skeleton

```bash
$ singularity exec <container> /usr/local/bin/conda-skeleton
$ podman run --it --rm --entrypoint /usr/local/bin/conda-skeleton   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-skeleton   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-verify

```bash
$ singularity exec <container> /usr/local/bin/conda-verify
$ podman run --it --rm --entrypoint /usr/local/bin/conda-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### involucro

```bash
$ singularity exec <container> /usr/local/bin/involucro
$ podman run --it --rm --entrypoint /usr/local/bin/involucro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/involucro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### patchelf

```bash
$ singularity exec <container> /usr/local/bin/patchelf
$ podman run --it --rm --entrypoint /usr/local/bin/patchelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/patchelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rg

```bash
$ singularity exec <container> /usr/local/bin/rg
$ podman run --it --rm --entrypoint /usr/local/bin/rg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scalar

```bash
$ singularity exec <container> /usr/local/bin/scalar
$ podman run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skopeo

```bash
$ singularity exec <container> /usr/local/bin/skopeo
$ podman run --it --rm --entrypoint /usr/local/bin/skopeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skopeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchgod

```bash
$ singularity exec <container> /usr/local/bin/watchgod
$ podman run --it --rm --entrypoint /usr/local/bin/watchgod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchgod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccomps

```bash
$ singularity exec <container> /usr/local/bin/ccomps
$ podman run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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