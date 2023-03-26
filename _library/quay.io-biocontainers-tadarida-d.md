---
layout: container
name:  "quay.io/biocontainers/tadarida-d"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tadarida-d/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tadarida-d/container.yaml"
updated_at: "2023-03-26 03:09:43.403972"
latest: "1.03--hf71b8e2_6"
container_url: "https://biocontainers.pro/tools/tadarida-d"
aliases:
 - "qdoc3"
 - "qmlviewer"
 - "qt3to4"
 - "qtconfig"
 - "qttracereplay"
 - "tadaridaD"
 - "flac"
 - "metaflac"
 - "sndfile-cmp"
 - "sndfile-concat"
 - "sndfile-convert"
 - "sndfile-deinterleave"
 - "sndfile-info"
 - "sndfile-interleave"
 - "sndfile-metadata-get"
 - "sndfile-metadata-set"
versions:
 - "1.03--hf71b8e2_6"
description: "shpc-registry automated BioContainers addition for tadarida-d"
config: {"url": "https://biocontainers.pro/tools/tadarida-d", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tadarida-d", "latest": {"1.03--hf71b8e2_6": "sha256:eb10379fc1249aed32e297659a5b03ca8d83a32c1d14428c3c1c58e89dfdccbd"}, "tags": {"1.03--hf71b8e2_6": "sha256:eb10379fc1249aed32e297659a5b03ca8d83a32c1d14428c3c1c58e89dfdccbd"}, "docker": "quay.io/biocontainers/tadarida-d", "aliases": {"qdoc3": "/usr/local/bin/qdoc3", "qmlviewer": "/usr/local/bin/qmlviewer", "qt3to4": "/usr/local/bin/qt3to4", "qtconfig": "/usr/local/bin/qtconfig", "qttracereplay": "/usr/local/bin/qttracereplay", "tadaridaD": "/usr/local/bin/tadaridaD", "flac": "/usr/local/bin/flac", "metaflac": "/usr/local/bin/metaflac", "sndfile-cmp": "/usr/local/bin/sndfile-cmp", "sndfile-concat": "/usr/local/bin/sndfile-concat", "sndfile-convert": "/usr/local/bin/sndfile-convert", "sndfile-deinterleave": "/usr/local/bin/sndfile-deinterleave", "sndfile-info": "/usr/local/bin/sndfile-info", "sndfile-interleave": "/usr/local/bin/sndfile-interleave", "sndfile-metadata-get": "/usr/local/bin/sndfile-metadata-get", "sndfile-metadata-set": "/usr/local/bin/sndfile-metadata-set"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tadarida-d.
shpc-registry automated BioContainers addition for tadarida-d
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tadarida-d
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tadarida-d:1.03--hf71b8e2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tadarida-d/1.03--hf71b8e2_6
$ module help quay.io/biocontainers/tadarida-d/1.03--hf71b8e2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tadarida-d-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tadarida-d-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tadarida-d-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tadarida-d-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tadarida-d-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tadarida-d-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qdoc3

```bash
$ singularity exec <container> /usr/local/bin/qdoc3
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlviewer

```bash
$ singularity exec <container> /usr/local/bin/qmlviewer
$ podman run --it --rm --entrypoint /usr/local/bin/qmlviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qt3to4

```bash
$ singularity exec <container> /usr/local/bin/qt3to4
$ podman run --it --rm --entrypoint /usr/local/bin/qt3to4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qt3to4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtconfig

```bash
$ singularity exec <container> /usr/local/bin/qtconfig
$ podman run --it --rm --entrypoint /usr/local/bin/qtconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qttracereplay

```bash
$ singularity exec <container> /usr/local/bin/qttracereplay
$ podman run --it --rm --entrypoint /usr/local/bin/qttracereplay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qttracereplay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tadaridaD

```bash
$ singularity exec <container> /usr/local/bin/tadaridaD
$ podman run --it --rm --entrypoint /usr/local/bin/tadaridaD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tadaridaD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flac

```bash
$ singularity exec <container> /usr/local/bin/flac
$ podman run --it --rm --entrypoint /usr/local/bin/flac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaflac

```bash
$ singularity exec <container> /usr/local/bin/metaflac
$ podman run --it --rm --entrypoint /usr/local/bin/metaflac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaflac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-cmp

```bash
$ singularity exec <container> /usr/local/bin/sndfile-cmp
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-concat

```bash
$ singularity exec <container> /usr/local/bin/sndfile-concat
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-convert

```bash
$ singularity exec <container> /usr/local/bin/sndfile-convert
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-deinterleave

```bash
$ singularity exec <container> /usr/local/bin/sndfile-deinterleave
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-deinterleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-deinterleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-info

```bash
$ singularity exec <container> /usr/local/bin/sndfile-info
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-interleave

```bash
$ singularity exec <container> /usr/local/bin/sndfile-interleave
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-metadata-get

```bash
$ singularity exec <container> /usr/local/bin/sndfile-metadata-get
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-metadata-set

```bash
$ singularity exec <container> /usr/local/bin/sndfile-metadata-set
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-set   -v ${PWD} -w ${PWD} <container> -c " $@"
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