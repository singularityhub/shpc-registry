---
layout: container
name:  "quay.io/biocontainers/cellxgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cellxgene/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cellxgene/container.yaml"
updated_at: "2022-10-29 05:30:07.269739"
latest: "1.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cellxgene"
aliases:
 - "cellxgene"
 - "gunicorn"
 - "2to3-3.10"
 - "f2py3.10"
 - "flask"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5clear"
 - "h5copy"
 - "h5debug"
versions:
 - "1.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cellxgene"
config: {"url": "https://biocontainers.pro/tools/cellxgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cellxgene", "latest": {"1.1.1--pyhdfd78af_0": "sha256:aadbb8e2d4c2d5e52eb318e66811c9a706bb2bc5b2a746c8f202be5044df42a4"}, "tags": {"1.1.1--pyhdfd78af_0": "sha256:aadbb8e2d4c2d5e52eb318e66811c9a706bb2bc5b2a746c8f202be5044df42a4"}, "docker": "quay.io/biocontainers/cellxgene", "aliases": {"cellxgene": "/usr/local/bin/cellxgene", "gunicorn": "/usr/local/bin/gunicorn", "2to3-3.10": "/usr/local/bin/2to3-3.10", "f2py3.10": "/usr/local/bin/f2py3.10", "flask": "/usr/local/bin/flask", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cellxgene.
shpc-registry automated BioContainers addition for cellxgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cellxgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cellxgene:1.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cellxgene/1.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/cellxgene/1.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cellxgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cellxgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cellxgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cellxgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cellxgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cellxgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cellxgene

```bash
$ singularity exec <container> /usr/local/bin/cellxgene
$ podman run --it --rm --entrypoint /usr/local/bin/cellxgene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cellxgene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunicorn

```bash
$ singularity exec <container> /usr/local/bin/gunicorn
$ podman run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
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