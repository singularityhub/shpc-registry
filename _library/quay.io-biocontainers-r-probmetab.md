---
layout: container
name:  "quay.io/biocontainers/r-probmetab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-probmetab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-probmetab/container.yaml"
updated_at: "2024-10-06 03:34:09.214490"
latest: "1.1--r34he1b5a44_4"
container_url: "https://biocontainers.pro/tools/r-probmetab"
aliases:
 - "nc-config"
 - "nccopy"
 - "ncdump"
 - "ncgen"
 - "ncgen3"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
 - "h5debug"
versions:
 - "1.1--r34he1b5a44_4"
description: "shpc-registry automated BioContainers addition for r-probmetab"
config: {"url": "https://biocontainers.pro/tools/r-probmetab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-probmetab", "latest": {"1.1--r34he1b5a44_4": "sha256:8c7b6eda43182d9639334fcdd5b8ea3af1e0d5c714d922fb54fda8bc56b72617"}, "tags": {"1.1--r34he1b5a44_4": "sha256:8c7b6eda43182d9639334fcdd5b8ea3af1e0d5c714d922fb54fda8bc56b72617"}, "docker": "quay.io/biocontainers/r-probmetab", "aliases": {"nc-config": "/usr/local/bin/nc-config", "nccopy": "/usr/local/bin/nccopy", "ncdump": "/usr/local/bin/ncdump", "ncgen": "/usr/local/bin/ncgen", "ncgen3": "/usr/local/bin/ncgen3", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-probmetab.
shpc-registry automated BioContainers addition for r-probmetab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-probmetab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-probmetab:1.1--r34he1b5a44_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-probmetab/1.1--r34he1b5a44_4
$ module help quay.io/biocontainers/r-probmetab/1.1--r34he1b5a44_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-probmetab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-probmetab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-probmetab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-probmetab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-probmetab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-probmetab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nc-config

```bash
$ singularity exec <container> /usr/local/bin/nc-config
$ podman run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nccopy

```bash
$ singularity exec <container> /usr/local/bin/nccopy
$ podman run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdump

```bash
$ singularity exec <container> /usr/local/bin/ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen

```bash
$ singularity exec <container> /usr/local/bin/ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen3

```bash
$ singularity exec <container> /usr/local/bin/ncgen3
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
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