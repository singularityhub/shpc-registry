---
layout: container
name:  "quay.io/biocontainers/ont-tombo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ont-tombo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ont-tombo/container.yaml"
updated_at: "2022-10-29 05:50:18.343860"
latest: "1.5--py27r36hb3f55d8_2"
container_url: "https://biocontainers.pro/tools/ont-tombo"
aliases:
 - "tombo"
 - "f2py2"
 - "f2py2.7"
 - "faidx"
 - "futurize"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5clear"
 - "h5copy"
versions:
 - "1.5--py27r36hb3f55d8_2"
description: "shpc-registry automated BioContainers addition for ont-tombo"
config: {"url": "https://biocontainers.pro/tools/ont-tombo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ont-tombo", "latest": {"1.5--py27r36hb3f55d8_2": "sha256:889d31cba456da799a30fcaa8846b1a26f16aec7a362b8b4250e47aa5759b7fc"}, "tags": {"1.5--py27r36hb3f55d8_2": "sha256:889d31cba456da799a30fcaa8846b1a26f16aec7a362b8b4250e47aa5759b7fc"}, "docker": "quay.io/biocontainers/ont-tombo", "aliases": {"tombo": "/usr/local/bin/tombo", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "faidx": "/usr/local/bin/faidx", "futurize": "/usr/local/bin/futurize", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ont-tombo.
shpc-registry automated BioContainers addition for ont-tombo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ont-tombo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ont-tombo:1.5--py27r36hb3f55d8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ont-tombo/1.5--py27r36hb3f55d8_2
$ module help quay.io/biocontainers/ont-tombo/1.5--py27r36hb3f55d8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ont-tombo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ont-tombo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ont-tombo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ont-tombo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ont-tombo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ont-tombo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tombo

```bash
$ singularity exec <container> /usr/local/bin/tombo
$ podman run --it --rm --entrypoint /usr/local/bin/tombo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tombo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
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