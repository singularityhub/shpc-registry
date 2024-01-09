---
layout: container
name:  "quay.io/biocontainers/bioconductor-fis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fis/container.yaml"
updated_at: "2024-01-09 02:44:49.455893"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fis"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.25.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_1"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fis", "latest": {"1.30.0--r43hdfd78af_0": "sha256:bb83ca9043bc5953df98b451761840cc65dd4fd0a0957bc5b4ac43437a183bb3"}, "tags": {"1.8.0--r341_0": "sha256:9eefe183780a84e6600b34cd484ca4152d5b02ad7ad615fcdcbb78b5d968e994", "1.26.0--r42hdfd78af_0": "sha256:27566accbafffb0988881d4c93c77a53967bc0dcb1150ca252a2be986622b473", "1.25.0--r42hdfd78af_0": "sha256:a6c549e9f6a353c5b2b50e17b13144afc67390788ab5543a3746cd77cb3ac7c8", "1.22.0--r41hdfd78af_1": "sha256:a1812e36d146323f9687fa747e7280556f99fc561fc1d7eecc5efc77c64438e6", "1.20.0--r41hdfd78af_0": "sha256:5fed350b405983d214c084ef9a04017168f2068bdbf09f289ca2d4469e49edab", "1.18.0--r40hdfd78af_1": "sha256:d68b528db09bc18edb1e7f670addfcbce24370c7a53eac1f440877ff0ad0f8ce", "1.28.0--r43hdfd78af_0": "sha256:3d284189a069d5ef23d113b2f1f80f850c38a4ec5470f4642f76b2ee970f7649", "1.30.0--r43hdfd78af_0": "sha256:bb83ca9043bc5953df98b451761840cc65dd4fd0a0957bc5b4ac43437a183bb3"}, "docker": "quay.io/biocontainers/bioconductor-fis", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fis.
shpc-registry automated BioContainers addition for bioconductor-fis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fis:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fis/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fis/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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