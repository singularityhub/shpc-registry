---
layout: container
name:  "quay.io/biocontainers/bioconductor-s4vectors"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-s4vectors/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-s4vectors/container.yaml"
updated_at: "2024-10-21 03:21:07.055835"
latest: "0.40.2--r43ha9d7317_2"
container_url: "https://biocontainers.pro/tools/bioconductor-s4vectors"
aliases:
 - "pngcp"
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "uconv"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "0.9.0--r3.3.1_0"
 - "0.36.0--r42hc0cfd56_0"
 - "0.32.4--r41hc0cfd56_0"
 - "0.30.0--r41hd029910_0"
 - "0.28.1--r40hd029910_0"
 - "0.26.0--r40h037d062_0"
 - "0.36.0--r42ha9d7317_1"
 - "0.38.1--r43ha9d7317_0"
 - "0.40.2--r43ha9d7317_1"
 - "0.40.2--r43ha9d7317_2"
description: "shpc-registry automated BioContainers addition for bioconductor-s4vectors"
config: {"url": "https://biocontainers.pro/tools/bioconductor-s4vectors", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-s4vectors", "latest": {"0.40.2--r43ha9d7317_2": "sha256:888d155ea9b258c7056d115e30b81bb4a0741faff2cf3a78ab00862fdc442648"}, "tags": {"0.9.0--r3.3.1_0": "sha256:c438cddbc73859fcfe13f6152b9f6e73282a9c90e177266eba6f457ca8e64847", "0.36.0--r42hc0cfd56_0": "sha256:862b4a0b019a1498def09a1b1d686ebd9761fd62efd86031d38a282ecdf51328", "0.32.4--r41hc0cfd56_0": "sha256:ecae13119b5bdedbf5e94968e1b7b10a5813ba7dbbddbf4816a26db0e2b42e4f", "0.30.0--r41hd029910_0": "sha256:6e747c686f28bc71a4e9025e93c735ee0db7bd042215159dbb1f0d25d1f778b5", "0.28.1--r40hd029910_0": "sha256:2f0410544e8e7686ab8d0080458b3a01a35db8a2d5479d3ba316376c4b3bbcec", "0.26.0--r40h037d062_0": "sha256:7cd2d8217057744fb40614f6dad09f8e3827ccf6065783fc3564eb6ad19e3f57", "0.36.0--r42ha9d7317_1": "sha256:141e1b3872b7a096003e50b61c73353de99e3f1451aad73018a0d9268e5133f2", "0.38.1--r43ha9d7317_0": "sha256:e414940cc26d9e5d49a35a5d9940f9a73ea7119e5a7a452d140b1f2b2e4b31ea", "0.40.2--r43ha9d7317_1": "sha256:0ed27178b5c6048873e6ffd65ffd27a14542d25ab2a2f6865539c22c11a5bf42", "0.40.2--r43ha9d7317_2": "sha256:888d155ea9b258c7056d115e30b81bb4a0741faff2cf3a78ab00862fdc442648"}, "docker": "quay.io/biocontainers/bioconductor-s4vectors", "aliases": {"pngcp": "/usr/local/bin/pngcp", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "uconv": "/usr/local/bin/uconv", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-s4vectors.
shpc-registry automated BioContainers addition for bioconductor-s4vectors
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-s4vectors
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-s4vectors:0.40.2--r43ha9d7317_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-s4vectors/0.40.2--r43ha9d7317_2
$ module help quay.io/biocontainers/bioconductor-s4vectors/0.40.2--r43ha9d7317_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-s4vectors-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-s4vectors-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-s4vectors-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-s4vectors-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-s4vectors-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-s4vectors-inspect-deffile:

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