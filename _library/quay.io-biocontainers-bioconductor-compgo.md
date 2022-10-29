---
layout: container
name:  "quay.io/biocontainers/bioconductor-compgo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-compgo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-compgo/container.yaml"
updated_at: "2022-10-29 05:37:11.765568"
latest: "1.26.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-compgo"
aliases:
 - "2to3-3.9"
 - "aserver"
 - "gif2rgb"
 - "gifbuild"
 - "gifclrmp"
 - "giffix"
 - "giftext"
 - "giftool"
 - "idle3.9"
 - "jaotc"
versions:
 - "1.26.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-compgo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-compgo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-compgo", "latest": {"1.26.0--r40hdfd78af_1": "sha256:7e521dc05d2cb48816e7cfd8b18123ffba7244c53ccf53681f6a1bd64aa9bea3"}, "tags": {"1.26.0--r40hdfd78af_1": "sha256:7e521dc05d2cb48816e7cfd8b18123ffba7244c53ccf53681f6a1bd64aa9bea3"}, "docker": "quay.io/biocontainers/bioconductor-compgo", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "aserver": "/usr/local/bin/aserver", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild", "gifclrmp": "/usr/local/bin/gifclrmp", "giffix": "/usr/local/bin/giffix", "giftext": "/usr/local/bin/giftext", "giftool": "/usr/local/bin/giftool", "idle3.9": "/usr/local/bin/idle3.9", "jaotc": "/usr/local/bin/jaotc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-compgo.
shpc-registry automated BioContainers addition for bioconductor-compgo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-compgo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-compgo:1.26.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-compgo/1.26.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-compgo/1.26.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-compgo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compgo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compgo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-compgo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-compgo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-compgo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifclrmp

```bash
$ singularity exec <container> /usr/local/bin/gifclrmp
$ podman run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffix

```bash
$ singularity exec <container> /usr/local/bin/giffix
$ podman run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftext

```bash
$ singularity exec <container> /usr/local/bin/giftext
$ podman run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftool

```bash
$ singularity exec <container> /usr/local/bin/giftool
$ podman run --it --rm --entrypoint /usr/local/bin/giftool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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