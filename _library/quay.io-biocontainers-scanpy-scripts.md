---
layout: container
name:  "quay.io/biocontainers/scanpy-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scanpy-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scanpy-scripts/container.yaml"
updated_at: "2023-08-27 03:04:02.763522"
latest: "1.1.2--pypyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/scanpy-scripts"
aliases:
 - "dunamai"
 - "loompy"
 - "scanpy-cli"
 - "scanpy-filter-cells"
 - "scanpy-filter-genes"
 - "scanpy-find-cluster"
 - "scanpy-find-markers"
 - "scanpy-find-variable-genes"
 - "scanpy-integrate"
 - "scanpy-multiplet"
 - "scanpy-neighbors"
 - "scanpy-normalise-data"
 - "scanpy-read-10x"
 - "scanpy-regress"
 - "scanpy-run-pca"
 - "scanpy-run-tsne"
 - "scanpy-run-umap"
 - "scanpy-scale-data"
 - "scanpy-scripts-tests.bats"
 - "tiff2fsspec"
 - "tiffcomment"
 - "JxrDecApp"
 - "JxrEncApp"
 - "cbrunsli"
 - "dbrunsli"
 - "imagecodecs"
 - "lsm2bin"
 - "tifffile"
 - "zfp"
 - "zopfli"
 - "zopflipng"
versions:
 - "1.1.2--pypyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for scanpy-scripts"
config: {"url": "https://biocontainers.pro/tools/scanpy-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scanpy-scripts", "latest": {"1.1.2--pypyhdfd78af_1": "sha256:c58b780539347faadb9073bebde291e5ae029457ec43f8754ad248b1f09fc085"}, "tags": {"1.1.2--pypyhdfd78af_1": "sha256:c58b780539347faadb9073bebde291e5ae029457ec43f8754ad248b1f09fc085"}, "docker": "quay.io/biocontainers/scanpy-scripts", "aliases": {"dunamai": "/usr/local/bin/dunamai", "loompy": "/usr/local/bin/loompy", "scanpy-cli": "/usr/local/bin/scanpy-cli", "scanpy-filter-cells": "/usr/local/bin/scanpy-filter-cells", "scanpy-filter-genes": "/usr/local/bin/scanpy-filter-genes", "scanpy-find-cluster": "/usr/local/bin/scanpy-find-cluster", "scanpy-find-markers": "/usr/local/bin/scanpy-find-markers", "scanpy-find-variable-genes": "/usr/local/bin/scanpy-find-variable-genes", "scanpy-integrate": "/usr/local/bin/scanpy-integrate", "scanpy-multiplet": "/usr/local/bin/scanpy-multiplet", "scanpy-neighbors": "/usr/local/bin/scanpy-neighbors", "scanpy-normalise-data": "/usr/local/bin/scanpy-normalise-data", "scanpy-read-10x": "/usr/local/bin/scanpy-read-10x", "scanpy-regress": "/usr/local/bin/scanpy-regress", "scanpy-run-pca": "/usr/local/bin/scanpy-run-pca", "scanpy-run-tsne": "/usr/local/bin/scanpy-run-tsne", "scanpy-run-umap": "/usr/local/bin/scanpy-run-umap", "scanpy-scale-data": "/usr/local/bin/scanpy-scale-data", "scanpy-scripts-tests.bats": "/usr/local/bin/scanpy-scripts-tests.bats", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "tiffcomment": "/usr/local/bin/tiffcomment", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "imagecodecs": "/usr/local/bin/imagecodecs", "lsm2bin": "/usr/local/bin/lsm2bin", "tifffile": "/usr/local/bin/tifffile", "zfp": "/usr/local/bin/zfp", "zopfli": "/usr/local/bin/zopfli", "zopflipng": "/usr/local/bin/zopflipng"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scanpy-scripts.
shpc-registry automated BioContainers addition for scanpy-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scanpy-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scanpy-scripts:1.1.2--pypyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scanpy-scripts/1.1.2--pypyhdfd78af_1
$ module help quay.io/biocontainers/scanpy-scripts/1.1.2--pypyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scanpy-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scanpy-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scanpy-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scanpy-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scanpy-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scanpy-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-cli

```bash
$ singularity exec <container> /usr/local/bin/scanpy-cli
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-filter-cells

```bash
$ singularity exec <container> /usr/local/bin/scanpy-filter-cells
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-filter-cells   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-filter-cells   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-filter-genes

```bash
$ singularity exec <container> /usr/local/bin/scanpy-filter-genes
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-filter-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-filter-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-find-cluster

```bash
$ singularity exec <container> /usr/local/bin/scanpy-find-cluster
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-find-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-find-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-find-markers

```bash
$ singularity exec <container> /usr/local/bin/scanpy-find-markers
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-find-markers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-find-markers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-find-variable-genes

```bash
$ singularity exec <container> /usr/local/bin/scanpy-find-variable-genes
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-find-variable-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-find-variable-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-integrate

```bash
$ singularity exec <container> /usr/local/bin/scanpy-integrate
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-integrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-integrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-multiplet

```bash
$ singularity exec <container> /usr/local/bin/scanpy-multiplet
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-multiplet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-multiplet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-neighbors

```bash
$ singularity exec <container> /usr/local/bin/scanpy-neighbors
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-neighbors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-neighbors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-normalise-data

```bash
$ singularity exec <container> /usr/local/bin/scanpy-normalise-data
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-normalise-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-normalise-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-read-10x

```bash
$ singularity exec <container> /usr/local/bin/scanpy-read-10x
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-read-10x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-read-10x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-regress

```bash
$ singularity exec <container> /usr/local/bin/scanpy-regress
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-regress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-regress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-run-pca

```bash
$ singularity exec <container> /usr/local/bin/scanpy-run-pca
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-run-pca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-run-pca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-run-tsne

```bash
$ singularity exec <container> /usr/local/bin/scanpy-run-tsne
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-run-tsne   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-run-tsne   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-run-umap

```bash
$ singularity exec <container> /usr/local/bin/scanpy-run-umap
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-run-umap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-run-umap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-scale-data

```bash
$ singularity exec <container> /usr/local/bin/scanpy-scale-data
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-scale-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-scale-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy-scripts-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/scanpy-scripts-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy-scripts-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy-scripts-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### JxrDecApp

```bash
$ singularity exec <container> /usr/local/bin/JxrDecApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrEncApp

```bash
$ singularity exec <container> /usr/local/bin/JxrEncApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbrunsli

```bash
$ singularity exec <container> /usr/local/bin/cbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbrunsli

```bash
$ singularity exec <container> /usr/local/bin/dbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagecodecs

```bash
$ singularity exec <container> /usr/local/bin/imagecodecs
$ podman run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsm2bin

```bash
$ singularity exec <container> /usr/local/bin/lsm2bin
$ podman run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tifffile

```bash
$ singularity exec <container> /usr/local/bin/tifffile
$ podman run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfp

```bash
$ singularity exec <container> /usr/local/bin/zfp
$ podman run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopfli

```bash
$ singularity exec <container> /usr/local/bin/zopfli
$ podman run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopflipng

```bash
$ singularity exec <container> /usr/local/bin/zopflipng
$ podman run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
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