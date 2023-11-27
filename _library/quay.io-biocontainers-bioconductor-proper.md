---
layout: container
name:  "quay.io/biocontainers/bioconductor-proper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proper/container.yaml"
updated_at: "2023-11-27 02:55:12.429534"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proper"
aliases:
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.3.2_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.26.0--r41hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proper", "latest": {"1.32.0--r43hdfd78af_0": "sha256:c996b96d85e2804aab33f1d2bf86a6aff43616e0015a746aae7a0ddc4488f0b2"}, "tags": {"1.8.0--r3.3.2_0": "sha256:9e8950a8327f2062a7bc3916b5945ea57cb1831ef41fd5bbbded0e80318a28e0", "1.30.0--r42hdfd78af_0": "sha256:cd05a3c0abc959d52cf8cda4e18078041e6e3395873da4a51d891f54d691d4ba", "1.26.0--r41hdfd78af_0": "sha256:f2ca2b05874fa65978886731c04dffd8a6d171343b138f75df954f572a83da98", "1.24.0--r41hdfd78af_0": "sha256:0733435705f4bca6da4bfed2786a08bea16a6b874d159dbb59bd8112d0a15880", "1.22.0--r40hdfd78af_1": "sha256:48da2cdf4c71fbdbdbfd0c8a8a2e4d6f320418766b595674e54f326877dbf4a1", "1.20.0--r40_0": "sha256:3507c7aeb294e8399cfcdc117567f59a88d41994872d745528265d3babd3e050", "1.32.0--r43hdfd78af_0": "sha256:c996b96d85e2804aab33f1d2bf86a6aff43616e0015a746aae7a0ddc4488f0b2"}, "docker": "quay.io/biocontainers/bioconductor-proper", "aliases": {"bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proper.
shpc-registry automated BioContainers addition for bioconductor-proper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proper:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proper/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-proper/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proper-inspect-deffile:

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


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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