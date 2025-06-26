---
layout: container
name:  "quay.io/biocontainers/bioconductor-genelendatabase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genelendatabase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genelendatabase/container.yaml"
updated_at: "2025-06-26 03:42:20.901372"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genelendatabase"
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
 - "1.6.0--0"
 - "1.30.0--r41hdfd78af_1"
 - "1.28.0--r41hdfd78af_0"
 - "1.26.0--r40hdfd78af_1"
 - "1.24.0--r40_0"
 - "1.22.0--r36_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genelendatabase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genelendatabase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genelendatabase", "latest": {"1.42.0--r44hdfd78af_0": "sha256:805bf231e193fb32d7eb4235fe71e05c2a856613bdb95cc6a16718f9aaf7fe31"}, "tags": {"1.6.0--0": "sha256:081739cc66d24cee3a5548491d52713d1e9ccd062f508a6c2aaac16bf2c2b125", "1.30.0--r41hdfd78af_1": "sha256:1b08e3072d9580d3749baf113048c2d9e57d1d7ea9e6b9877107345b822eeb69", "1.28.0--r41hdfd78af_0": "sha256:7bfdec26a7d01fd4bd68e6e0ef22ce16c79e812f852487df1ad23a4735187ae7", "1.26.0--r40hdfd78af_1": "sha256:e42e20d86e86be6e3a7e9c441a690ccbf5d87550a6d4063167b2e2e1b1dd1925", "1.24.0--r40_0": "sha256:a87549821bb452151dbf1d85276525fe036ddd568b154c934951caa498be0b7a", "1.22.0--r36_0": "sha256:3feefeaef89d768eaa9d25307cf040b5f645894d91c791e22e95d810715de908", "1.34.0--r42hdfd78af_0": "sha256:d831717d45cc86501aba18d3a0a3d7bb4820a77f0d24acf04a880d0fef877d11", "1.36.0--r43hdfd78af_0": "sha256:8c556766b6ea0718bd997229f2cc33ce02bd399363ea1195c1f549b97890da62", "1.38.0--r43hdfd78af_0": "sha256:511f8ff7f11d6eaba4817896135ebfc7cd8b005783096c6d99e0fa2af0637620", "1.42.0--r44hdfd78af_0": "sha256:805bf231e193fb32d7eb4235fe71e05c2a856613bdb95cc6a16718f9aaf7fe31"}, "docker": "quay.io/biocontainers/bioconductor-genelendatabase", "aliases": {"pngcp": "/usr/local/bin/pngcp", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genelendatabase.
shpc-registry automated BioContainers addition for bioconductor-genelendatabase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genelendatabase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genelendatabase:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genelendatabase/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genelendatabase/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genelendatabase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genelendatabase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genelendatabase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genelendatabase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genelendatabase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genelendatabase-inspect-deffile:

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