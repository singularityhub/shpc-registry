---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathview/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathview/container.yaml"
updated_at: "2024-02-12 03:36:49.496379"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathview"
aliases:
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "uconv"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.9.0--r3.3.1_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.34.0--r41hdfd78af_0"
 - "1.32.0--r41hdfd78af_0"
 - "1.30.1--r40hdfd78af_0"
 - "1.28.0--r40_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathview"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathview", "latest": {"1.42.0--r43hdfd78af_0": "sha256:f367d79bbfd665025fc87239013c52cdb88a4a063377c0d746d891a9f1ace2a5"}, "tags": {"1.9.0--r3.3.1_0": "sha256:26b40ed1c40166565f17f5f68bf66d85868190deedf4fb1e143b2fc269b482ad", "1.38.0--r42hdfd78af_0": "sha256:f6f4144f4a40050610720b1023c9b88dcccf3501a6bc074727cb064408a4cf69", "1.34.0--r41hdfd78af_0": "sha256:4214800ccddc9e8deb5d7ceade6224088fbeea5054da4c712bd17a0ef09219cc", "1.32.0--r41hdfd78af_0": "sha256:a6a9bf49d597560af173ae4e6e4dd3ebd8b47d8ebaef6c3948cb2b216eb6a50d", "1.30.1--r40hdfd78af_0": "sha256:9986e2e4486459a982737a9a9fc1d9854141589273e7a8f7124a26825699ac5a", "1.28.0--r40_0": "sha256:47dc1af47e8453f76a88fa61b6891d2b58f497d3c07248e73d6017b98c9ab6bc", "1.40.0--r43hdfd78af_0": "sha256:495a5b91f3e56860b33177396b709d2baf5dafb15caa98051bd8b52693816e60", "1.42.0--r43hdfd78af_0": "sha256:f367d79bbfd665025fc87239013c52cdb88a4a063377c0d746d891a9f1ace2a5"}, "docker": "quay.io/biocontainers/bioconductor-pathview", "aliases": {"bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "uconv": "/usr/local/bin/uconv", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathview.
shpc-registry automated BioContainers addition for bioconductor-pathview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathview:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathview/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathview/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathview-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
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