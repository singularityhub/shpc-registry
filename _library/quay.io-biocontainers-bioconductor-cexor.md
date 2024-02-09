---
layout: container
name:  "quay.io/biocontainers/bioconductor-cexor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cexor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cexor/container.yaml"
updated_at: "2024-02-09 02:35:31.616514"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cexor"
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
 - "1.8.0--0"
 - "1.36.0--r42hdfd78af_0"
 - "1.32.0--r41hdfd78af_0"
 - "1.28.0--r40hdfd78af_1"
 - "1.26.0--r40_0"
 - "1.24.0--r36_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cexor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cexor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cexor", "latest": {"1.40.0--r43hdfd78af_0": "sha256:97f2e8b0833e8ddf8e20243bebfd8ee162afe32275767bd4ecdf09bf9524414d"}, "tags": {"1.8.0--0": "sha256:a20ecf2b90cc811a6df29d7569927376118626cb8152002f9671dde56438fdf6", "1.36.0--r42hdfd78af_0": "sha256:cab1466e1e9d385cbd4b48a15577a8d24a063a0ed17f49e5292d63ea7d8def5d", "1.32.0--r41hdfd78af_0": "sha256:27e0f57cf3764c57ba0caf27c95a1acacfe29d0f9e668d079f600981906ddb4e", "1.28.0--r40hdfd78af_1": "sha256:782b6981faaa4fb5200284f3f740792cf1a377fb02e0c36cee87802467b6b20a", "1.26.0--r40_0": "sha256:7624b5ce44868ba6bdd465e70390b172bdddd72d72dbf565f7dd1a6a2cb34a50", "1.24.0--r36_0": "sha256:f2bdc683234f64d38f76b4c478ae6d73ecf613e01e0cdfaac4f30f2c72c1955b", "1.38.0--r43hdfd78af_0": "sha256:a70d360219c22ba9d79fd08c4befe43faa55aeea1415b501018858691fcb0ae4", "1.40.0--r43hdfd78af_0": "sha256:97f2e8b0833e8ddf8e20243bebfd8ee162afe32275767bd4ecdf09bf9524414d"}, "docker": "quay.io/biocontainers/bioconductor-cexor", "aliases": {"pngcp": "/usr/local/bin/pngcp", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cexor.
shpc-registry automated BioContainers addition for bioconductor-cexor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cexor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cexor:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cexor/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cexor/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cexor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cexor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cexor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cexor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cexor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cexor-inspect-deffile:

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