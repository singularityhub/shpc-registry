---
layout: container
name:  "quay.io/biocontainers/vpolo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vpolo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vpolo/container.yaml"
updated_at: "2022-10-29 05:47:37.341996"
latest: "0.3.0--pyh864c0ab_0"
container_url: "https://biocontainers.pro/tools/vpolo"
aliases:
 - "2to3"
 - "2to3-3.8"
 - "c_rehash"
 - "captoinfo"
 - "clear"
 - "easy_install"
 - "idle3"
 - "idle3.8"
 - "infocmp"
 - "infotocap"
versions:
 - "0.3.0--pyh864c0ab_0"
description: "shpc-registry automated BioContainers addition for vpolo"
config: {"url": "https://biocontainers.pro/tools/vpolo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vpolo", "latest": {"0.3.0--pyh864c0ab_0": "sha256:bf7ada0539b7a6ae93863fe1a8cc255d5308670004eec5718ed4f089eebb8356"}, "tags": {"0.3.0--pyh864c0ab_0": "sha256:bf7ada0539b7a6ae93863fe1a8cc255d5308670004eec5718ed4f089eebb8356"}, "docker": "quay.io/biocontainers/vpolo", "aliases": {"2to3": "/usr/local/bin/2to3", "2to3-3.8": "/usr/local/bin/2to3-3.8", "c_rehash": "/usr/local/bin/c_rehash", "captoinfo": "/usr/local/bin/captoinfo", "clear": "/usr/local/bin/clear", "easy_install": "/usr/local/bin/easy_install", "idle3": "/usr/local/bin/idle3", "idle3.8": "/usr/local/bin/idle3.8", "infocmp": "/usr/local/bin/infocmp", "infotocap": "/usr/local/bin/infotocap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vpolo.
shpc-registry automated BioContainers addition for vpolo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vpolo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vpolo:0.3.0--pyh864c0ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vpolo/0.3.0--pyh864c0ab_0
$ module help quay.io/biocontainers/vpolo/0.3.0--pyh864c0ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vpolo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vpolo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vpolo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vpolo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vpolo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vpolo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3

```bash
$ singularity exec <container> /usr/local/bin/2to3
$ podman run --it --rm --entrypoint /usr/local/bin/2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c_rehash

```bash
$ singularity exec <container> /usr/local/bin/c_rehash
$ podman run --it --rm --entrypoint /usr/local/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### captoinfo

```bash
$ singularity exec <container> /usr/local/bin/captoinfo
$ podman run --it --rm --entrypoint /usr/local/bin/captoinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/captoinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clear

```bash
$ singularity exec <container> /usr/local/bin/clear
$ podman run --it --rm --entrypoint /usr/local/bin/clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install

```bash
$ singularity exec <container> /usr/local/bin/easy_install
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3

```bash
$ singularity exec <container> /usr/local/bin/idle3
$ podman run --it --rm --entrypoint /usr/local/bin/idle3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infocmp

```bash
$ singularity exec <container> /usr/local/bin/infocmp
$ podman run --it --rm --entrypoint /usr/local/bin/infocmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infocmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infotocap

```bash
$ singularity exec <container> /usr/local/bin/infotocap
$ podman run --it --rm --entrypoint /usr/local/bin/infotocap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infotocap   -v ${PWD} -w ${PWD} <container> -c " $@"
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