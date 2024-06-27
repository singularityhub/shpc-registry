---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicalignments"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicalignments/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicalignments/container.yaml"
updated_at: "2024-06-27 03:16:52.725671"
latest: "1.38.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicalignments"
aliases:
 - "pngcp"
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.6.3--1"
 - "1.34.0--r42hc0cfd56_0"
 - "1.30.0--r41hc0cfd56_2"
 - "1.28.0--r41hd029910_0"
 - "1.26.0--r40hd029910_1"
 - "1.24.0--r40h037d062_0"
 - "1.34.0--r42ha9d7317_1"
 - "1.36.0--r43ha9d7317_0"
 - "1.38.0--r43ha9d7317_0"
 - "1.38.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicalignments"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicalignments", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicalignments", "latest": {"1.38.0--r43ha9d7317_1": "sha256:1bcb9e2b61f5b19e31641cbd2ffe0cea9413ade3d5eb2c6cb39817020a04cbc6"}, "tags": {"1.6.3--1": "sha256:3d1492a9f8edf486e4de19074ecc12256400d71cc6d4ec3479472b1dcdd7333b", "1.34.0--r42hc0cfd56_0": "sha256:8bb6ca722c9d9ca038384b9407c6529be5100628b66237627ee1b19707b80c94", "1.30.0--r41hc0cfd56_2": "sha256:2ec7685ba14cc873523ad304b3f0a4acb270f067688d048730ed254778e29227", "1.28.0--r41hd029910_0": "sha256:5fc9b53113543911b749ab9c6dff9492836a471747f9b610532cf232f1d24fee", "1.26.0--r40hd029910_1": "sha256:58e72ac2f51c3f4bbb0fc8398db059e62895e0d77fec5acd9a63b0ada8a8ee54", "1.24.0--r40h037d062_0": "sha256:dc47a66f16c69a9dc67f1b1813825552917f6d3f3750ca00a6e8a26d25ea2acb", "1.34.0--r42ha9d7317_1": "sha256:32bf5fb27495a788955c99fd9fde982dc66b23511c7d2f438d5e2388d2db9eba", "1.36.0--r43ha9d7317_0": "sha256:05a8dcb406c6278c127c1dd46ffd73234cdaed369c509007d01fa883503da71e", "1.38.0--r43ha9d7317_0": "sha256:f94532c792ea5bacffdf559df3753dbd8c748f3220f64c1e5f57940775df7849", "1.38.0--r43ha9d7317_1": "sha256:1bcb9e2b61f5b19e31641cbd2ffe0cea9413ade3d5eb2c6cb39817020a04cbc6"}, "docker": "quay.io/biocontainers/bioconductor-genomicalignments", "aliases": {"pngcp": "/usr/local/bin/pngcp", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicalignments.
shpc-registry automated BioContainers addition for bioconductor-genomicalignments
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicalignments
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicalignments:1.38.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicalignments/1.38.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-genomicalignments/1.38.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicalignments-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicalignments-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicalignments-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicalignments-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicalignments-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicalignments-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pngcp

```bash
$ singularity exec <container> /usr/local/bin/pngcp
$ podman run --it --rm --entrypoint /usr/local/bin/pngcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmp2tiff

```bash
$ singularity exec <container> /usr/local/bin/bmp2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/bmp2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmp2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2tiff

```bash
$ singularity exec <container> /usr/local/bin/gif2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/gif2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ras2tiff

```bash
$ singularity exec <container> /usr/local/bin/ras2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/ras2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ras2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgb2ycbcr

```bash
$ singularity exec <container> /usr/local/bin/rgb2ycbcr
$ podman run --it --rm --entrypoint /usr/local/bin/rgb2ycbcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgb2ycbcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thumbnail

```bash
$ singularity exec <container> /usr/local/bin/thumbnail
$ podman run --it --rm --entrypoint /usr/local/bin/thumbnail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thumbnail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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