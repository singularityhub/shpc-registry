---
layout: container
name:  "quay.io/biocontainers/r-spdep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-spdep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-spdep/container.yaml"
updated_at: "2025-06-04 15:34:33.869501"
latest: "0.6_8--r3.3.1_0"
container_url: "https://biocontainers.pro/tools/r-spdep"
aliases:
 - "pango-querymodules"
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "uconv"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "0.6_8--r3.3.1_0"
 - "0.6_8--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-spdep"
config: {"url": "https://biocontainers.pro/tools/r-spdep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-spdep", "latest": {"0.6_8--r3.3.1_0": "sha256:fba1567b118518881eec420b30894c1c4a05292e48f0aa444618b3a822051d38"}, "tags": {"0.6_8--r3.3.1_0": "sha256:fba1567b118518881eec420b30894c1c4a05292e48f0aa444618b3a822051d38", "0.6_8--r3.3.2_0": "sha256:1531f94c152e022ceb0bd2c31c4975fb77b24872b2fafecfd2b96641a7749541"}, "docker": "quay.io/biocontainers/r-spdep", "aliases": {"pango-querymodules": "/usr/local/bin/pango-querymodules", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "uconv": "/usr/local/bin/uconv", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-spdep.
shpc-registry automated BioContainers addition for r-spdep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-spdep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-spdep:0.6_8--r3.3.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-spdep/0.6_8--r3.3.1_0
$ module help quay.io/biocontainers/r-spdep/0.6_8--r3.3.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-spdep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-spdep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-spdep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-spdep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-spdep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-spdep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pango-querymodules

```bash
$ singularity exec <container> /usr/local/bin/pango-querymodules
$ podman run --it --rm --entrypoint /usr/local/bin/pango-querymodules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pango-querymodules   -v ${PWD} -w ${PWD} <container> -c " $@"
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