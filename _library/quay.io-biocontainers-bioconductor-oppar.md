---
layout: container
name:  "quay.io/biocontainers/bioconductor-oppar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oppar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oppar/container.yaml"
updated_at: "2025-07-11 04:17:45.649850"
latest: "1.34.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-oppar"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341h470a237_0"
 - "1.26.0--r42hc0cfd56_0"
 - "1.22.0--r41hc0cfd56_2"
 - "1.20.0--r41hd029910_0"
 - "1.18.0--r40hd029910_1"
 - "1.16.0--r40h037d062_0"
 - "1.26.0--r42ha9d7317_1"
 - "1.28.0--r43ha9d7317_0"
 - "1.30.0--r43ha9d7317_0"
 - "1.34.0--r44h3df3fcb_0"
 - "1.34.0--r44h3df3fcb_1"
description: "shpc-registry automated BioContainers addition for bioconductor-oppar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oppar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oppar", "latest": {"1.34.0--r44h3df3fcb_1": "sha256:ee6dad5a3a5954cae13d827ccd1ec5449c41e4b0207702e7e2e3b8fa6a088ecb"}, "tags": {"1.8.0--r341h470a237_0": "sha256:471321041246c3d47a10a9af29e16667f7dbeca43b10aa85799f86303a9f183b", "1.26.0--r42hc0cfd56_0": "sha256:2276202074090add56c5411b8e1569defed434c6f1c456b6bc980617f9747394", "1.22.0--r41hc0cfd56_2": "sha256:81f4db80f3bc8fc5e88758e80cd7dd02c4d42d29dc5dd82bb71a540dbef4aa17", "1.20.0--r41hd029910_0": "sha256:0dcd2b0b8634e6f1c8f81bf6b29835570c18043817cc10e2c461857a5beb355d", "1.18.0--r40hd029910_1": "sha256:028db83c3f84bf73bbd15549fa47f4ddac7a72212a5ca584953ebc1827c3a9cd", "1.16.0--r40h037d062_0": "sha256:b8b97aff4b36eb807b507374e93a70ea6e77359f3406cf0267a7c629c2a3d1c4", "1.26.0--r42ha9d7317_1": "sha256:e034e4d2cdf45acc1d75d6755dad5c1c8445a7a257e25f0fe9177fe915ced79a", "1.28.0--r43ha9d7317_0": "sha256:5b4e25148b8ca36120538a64ef6480b1e51ae03f307ff5550de8058bdcb6b6b3", "1.30.0--r43ha9d7317_0": "sha256:7853ffeb08d5c1e99872f1aed9f4668b32e50f8dd664ee05c4ad5d662b331f67", "1.34.0--r44h3df3fcb_0": "sha256:3ccc0920dbc348fb2b2b9e969fd850fda015b4c8c5105e0d254a12a576f912f6", "1.34.0--r44h3df3fcb_1": "sha256:ee6dad5a3a5954cae13d827ccd1ec5449c41e4b0207702e7e2e3b8fa6a088ecb"}, "docker": "quay.io/biocontainers/bioconductor-oppar", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oppar.
shpc-registry automated BioContainers addition for bioconductor-oppar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oppar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oppar:1.34.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oppar/1.34.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-oppar/1.34.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oppar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oppar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oppar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oppar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oppar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oppar-inspect-deffile:

```bash
$ singularity inspect -d <container>
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