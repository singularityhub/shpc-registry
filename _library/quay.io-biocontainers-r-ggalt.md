---
layout: container
name:  "quay.io/biocontainers/r-ggalt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ggalt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ggalt/container.yaml"
updated_at: "2025-09-17 03:21:45.503322"
latest: "0.4.0--r3.3.2_0"
container_url: "https://biocontainers.pro/tools/r-ggalt"
aliases:
 - "nad2bin"
 - "invgeod"
 - "invproj"
 - "cs2cs"
 - "geod"
 - "proj"
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
versions:
 - "0.4.0--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-ggalt"
config: {"url": "https://biocontainers.pro/tools/r-ggalt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ggalt", "latest": {"0.4.0--r3.3.2_0": "sha256:0b8826f195f7ea5cfad9e2d3eb0205d5ccb178cdcfe856278ad45b72036858ae"}, "tags": {"0.4.0--r3.3.2_0": "sha256:0b8826f195f7ea5cfad9e2d3eb0205d5ccb178cdcfe856278ad45b72036858ae"}, "docker": "quay.io/biocontainers/r-ggalt", "aliases": {"nad2bin": "/usr/local/bin/nad2bin", "invgeod": "/usr/local/bin/invgeod", "invproj": "/usr/local/bin/invproj", "cs2cs": "/usr/local/bin/cs2cs", "geod": "/usr/local/bin/geod", "proj": "/usr/local/bin/proj", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ggalt.
shpc-registry automated BioContainers addition for r-ggalt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ggalt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ggalt:0.4.0--r3.3.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ggalt/0.4.0--r3.3.2_0
$ module help quay.io/biocontainers/r-ggalt/0.4.0--r3.3.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ggalt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ggalt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ggalt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ggalt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ggalt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ggalt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nad2bin

```bash
$ singularity exec <container> /usr/local/bin/nad2bin
$ podman run --it --rm --entrypoint /usr/local/bin/nad2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nad2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invgeod

```bash
$ singularity exec <container> /usr/local/bin/invgeod
$ podman run --it --rm --entrypoint /usr/local/bin/invgeod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invgeod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invproj

```bash
$ singularity exec <container> /usr/local/bin/invproj
$ podman run --it --rm --entrypoint /usr/local/bin/invproj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invproj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cs2cs

```bash
$ singularity exec <container> /usr/local/bin/cs2cs
$ podman run --it --rm --entrypoint /usr/local/bin/cs2cs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cs2cs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geod

```bash
$ singularity exec <container> /usr/local/bin/geod
$ podman run --it --rm --entrypoint /usr/local/bin/geod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proj

```bash
$ singularity exec <container> /usr/local/bin/proj
$ podman run --it --rm --entrypoint /usr/local/bin/proj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proj   -v ${PWD} -w ${PWD} <container> -c " $@"
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