---
layout: container
name:  "quay.io/biocontainers/eukrep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eukrep/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/eukrep/container.yaml"
updated_at: "2022-10-29 05:53:52.132445"
latest: "0.6.7--pyh5e36f6f_2"
container_url: "https://biocontainers.pro/tools/eukrep"
aliases:
 - "EukRep"
 - "kpal"
 - "2to3-3.7"
 - "f2py3.7"
 - "futurize"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5clear"
 - "h5copy"
 - "h5debug"
versions:
 - "0.6.7--pyh5e36f6f_2"
description: "shpc-registry automated BioContainers addition for eukrep"
config: {"url": "https://biocontainers.pro/tools/eukrep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eukrep", "latest": {"0.6.7--pyh5e36f6f_2": "sha256:576ddeae452b16ecbf4bc3b4fe57cd8af7e91b7a49a4096c32515bc365483f31"}, "tags": {"0.6.7--pyh5e36f6f_2": "sha256:576ddeae452b16ecbf4bc3b4fe57cd8af7e91b7a49a4096c32515bc365483f31"}, "docker": "quay.io/biocontainers/eukrep", "aliases": {"EukRep": "/usr/local/bin/EukRep", "kpal": "/usr/local/bin/kpal", "2to3-3.7": "/usr/local/bin/2to3-3.7", "f2py3.7": "/usr/local/bin/f2py3.7", "futurize": "/usr/local/bin/futurize", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eukrep.
shpc-registry automated BioContainers addition for eukrep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eukrep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eukrep:0.6.7--pyh5e36f6f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eukrep/0.6.7--pyh5e36f6f_2
$ module help quay.io/biocontainers/eukrep/0.6.7--pyh5e36f6f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eukrep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eukrep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eukrep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eukrep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eukrep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eukrep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EukRep

```bash
$ singularity exec <container> /usr/local/bin/EukRep
$ podman run --it --rm --entrypoint /usr/local/bin/EukRep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukRep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kpal

```bash
$ singularity exec <container> /usr/local/bin/kpal
$ podman run --it --rm --entrypoint /usr/local/bin/kpal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kpal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
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