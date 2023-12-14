---
layout: container
name:  "quay.io/biocontainers/bioconductor-edaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-edaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-edaseq/container.yaml"
updated_at: "2023-12-14 02:58:30.371535"
latest: "2.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-edaseq"
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
 - "2.8.0--r3.4.1_0"
 - "2.32.0--r42hdfd78af_0"
 - "2.28.0--r41hdfd78af_0"
 - "2.26.0--r41hdfd78af_0"
 - "2.24.0--r40hdfd78af_1"
 - "2.22.0--r40_0"
 - "2.34.0--r43hdfd78af_0"
 - "2.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-edaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-edaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-edaseq", "latest": {"2.36.0--r43hdfd78af_0": "sha256:06fcaca929145704291fe85d3822f91d67ad8070f464cc456d0b27d097867d39"}, "tags": {"2.8.0--r3.4.1_0": "sha256:1f12d27572ba0ee2852930224e8029d8da9e97afd4f79bc034bda7d55fc47594", "2.32.0--r42hdfd78af_0": "sha256:5a139ce7017e0ed880bafc07c1f9807207e571106c9294928115c24e50f882d1", "2.28.0--r41hdfd78af_0": "sha256:aa670b48293bdd1f29883c925b76f7a74fc84e0d161ee21ccf568a36c44469fc", "2.26.0--r41hdfd78af_0": "sha256:1685bc33d5a74f9fecb0d77ff6839824d1a28a44b682cfe33b646a21af2d3753", "2.24.0--r40hdfd78af_1": "sha256:fa95e7f8ff9b1457b62d5727a3a04ea097c28927f137ea85a08b6b356f864f54", "2.22.0--r40_0": "sha256:5c7c52f187b847d3c75f46793568beccd15ac00d1c06c191988c5e989a97771c", "2.34.0--r43hdfd78af_0": "sha256:e6b6cdc398d9893a8236d5f9a722be8153e69ad7f71a2b53eaa7d4ae0cc74d00", "2.36.0--r43hdfd78af_0": "sha256:06fcaca929145704291fe85d3822f91d67ad8070f464cc456d0b27d097867d39"}, "docker": "quay.io/biocontainers/bioconductor-edaseq", "aliases": {"bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-edaseq.
shpc-registry automated BioContainers addition for bioconductor-edaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-edaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-edaseq:2.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-edaseq/2.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-edaseq/2.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-edaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-edaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-edaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-edaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-edaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-edaseq-inspect-deffile:

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