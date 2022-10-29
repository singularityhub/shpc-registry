---
layout: container
name:  "quay.io/biocontainers/bioconductor-mulder2012"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mulder2012/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mulder2012/container.yaml"
updated_at: "2022-10-29 05:58:28.623803"
latest: "0.26.0--r36_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mulder2012"
aliases:
 - "aserver"
 - "c89"
 - "c99"
 - "gif2rgb"
 - "gifbuild"
 - "gifclrmp"
 - "gifecho"
 - "giffilter"
 - "giffix"
 - "gifinto"
versions:
 - "0.26.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mulder2012"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mulder2012", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mulder2012", "latest": {"0.26.0--r36_0": "sha256:bf27bf5a0effcf6a4941ec48db83c4d8bc56c2c3eb1cb5349131840726016e33"}, "tags": {"0.26.0--r36_0": "sha256:bf27bf5a0effcf6a4941ec48db83c4d8bc56c2c3eb1cb5349131840726016e33"}, "docker": "quay.io/biocontainers/bioconductor-mulder2012", "aliases": {"aserver": "/usr/local/bin/aserver", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild", "gifclrmp": "/usr/local/bin/gifclrmp", "gifecho": "/usr/local/bin/gifecho", "giffilter": "/usr/local/bin/giffilter", "giffix": "/usr/local/bin/giffix", "gifinto": "/usr/local/bin/gifinto"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mulder2012.
shpc-registry automated BioContainers addition for bioconductor-mulder2012
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mulder2012
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mulder2012:0.26.0--r36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mulder2012/0.26.0--r36_0
$ module help quay.io/biocontainers/bioconductor-mulder2012/0.26.0--r36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mulder2012-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mulder2012-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mulder2012-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mulder2012-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mulder2012-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mulder2012-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gifecho

```bash
$ singularity exec <container> /usr/local/bin/gifecho
$ podman run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffix

```bash
$ singularity exec <container> /usr/local/bin/giffix
$ podman run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifinto

```bash
$ singularity exec <container> /usr/local/bin/gifinto
$ podman run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
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