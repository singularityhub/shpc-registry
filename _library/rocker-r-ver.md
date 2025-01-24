---
layout: container
name:  "rocker/r-ver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/r-ver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/r-ver/container.yaml"
updated_at: "2025-01-24 03:35:57.514672"
latest: "4.4.2"
container_url: "https://hub.docker.com/r/rocker/r-ver"
aliases:
 - "R"
 - "Rscript"
versions:
 - "4.2.2"
 - "3.6.3"
 - "4.1.3"
 - "4.0.5"
 - "4.2.3"
 - "4.3.0"
 - "4.3.1"
 - "4.3.2"
 - "4.3.3"
 - "4.4.0"
 - "4.4.1"
 - "4.4.2"
description: "Version-stable build of R"
config: {"docker": "rocker/r-ver", "url": "https://hub.docker.com/r/rocker/r-ver", "maintainer": "@marcodelapierre", "description": "Version-stable build of R", "latest": {"4.4.2": "sha256:45ac2c19f431efdd48d8adc59c51f56b43332c413f7486f148a4def7f8a5f301"}, "tags": {"4.2.2": "sha256:e868e617f2adb9740983d5fed65032afa9632308ab94bde02da09182e46f9389", "3.6.3": "sha256:9414f76c5f91f24617b5275b8fe4f4ff1313b3b10698a525cac0063c01f2ca6d", "4.1.3": "sha256:96be237557b98e5d34957ed4fcbf386999981119086cd4b4cfbafd5c2a47a3f4", "4.0.5": "sha256:fef68eaf0e829d464697948343ac440bbc189a0592b451eb99cddb46a8c8a7e3", "4.2.3": "sha256:6dff804fb051f7c38cf9ebcaf307b5102b46e5187ffe2ce921d760a26facd693", "4.3.0": "sha256:48fb09f63e1cbcc1b0ce3974a8f206bff0804b6921bb36dfa08eafa264dad542", "4.3.1": "sha256:bbb32869133890d2ae65305ae577a86d0ee48b2dd769961ef198aef09eb7bbb6", "4.3.2": "sha256:4e32addfc4da3e660f6e0d05ce5e43d3eceb9db58a60b9a142e0dde9a654ead1", "4.3.3": "sha256:b406ba45a1488053d2ffc68acabe0d742e750bf29ec80ccfe18e4786fa3495d9", "4.4.0": "sha256:73adabf378930f8744f56bac1fe5e99870532eb4ced1a15075991bac909d21f3", "4.4.1": "sha256:78cb94ce2db23aaaf7b546450fcf70b5a3f2ace5a9b5fa1f87217da329211312", "4.4.2": "sha256:45ac2c19f431efdd48d8adc59c51f56b43332c413f7486f148a4def7f8a5f301"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript"}}
---

This module is a singularity container wrapper for rocker/r-ver.
Version-stable build of R
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/r-ver
```

Or a specific version:

```bash
$ shpc install rocker/r-ver:4.4.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/r-ver/4.4.2
$ module help rocker/r-ver/4.4.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
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