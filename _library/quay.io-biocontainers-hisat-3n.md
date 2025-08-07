---
layout: container
name:  "quay.io/biocontainers/hisat-3n"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hisat-3n/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hisat-3n/container.yaml"
updated_at: "2025-08-07 09:44:27.718154"
latest: "0.0.3--h503566f_0"
container_url: "https://biocontainers.pro/tools/hisat-3n"
aliases:
 - "hisat-3n"
 - "hisat-3n-build"
 - "hisat-3n-table"
 - "hisat2-align-l"
 - "hisat2-align-s"
 - "hisat2-build"
 - "hisat2-build-l"
 - "hisat2-build-s"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.0.3--h503566f_0"
description: "singularity registry hpc automated addition for hisat-3n"
config: {"url": "https://biocontainers.pro/tools/hisat-3n", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hisat-3n", "latest": {"0.0.3--h503566f_0": "sha256:be5b339b288df410b1825d4630d836b02bf24d92c09f98532dc3080930eefa90"}, "tags": {"0.0.3--h503566f_0": "sha256:be5b339b288df410b1825d4630d836b02bf24d92c09f98532dc3080930eefa90"}, "docker": "quay.io/biocontainers/hisat-3n", "aliases": {"hisat-3n": "/usr/local/bin/hisat-3n", "hisat-3n-build": "/usr/local/bin/hisat-3n-build", "hisat-3n-table": "/usr/local/bin/hisat-3n-table", "hisat2-align-l": "/usr/local/bin/hisat2-align-l", "hisat2-align-s": "/usr/local/bin/hisat2-align-s", "hisat2-build": "/usr/local/bin/hisat2-build", "hisat2-build-l": "/usr/local/bin/hisat2-build-l", "hisat2-build-s": "/usr/local/bin/hisat2-build-s", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hisat-3n.
singularity registry hpc automated addition for hisat-3n
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hisat-3n
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hisat-3n:0.0.3--h503566f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hisat-3n/0.0.3--h503566f_0
$ module help quay.io/biocontainers/hisat-3n/0.0.3--h503566f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hisat-3n-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hisat-3n-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hisat-3n-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hisat-3n-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hisat-3n-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hisat-3n-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hisat-3n

```bash
$ singularity exec <container> /usr/local/bin/hisat-3n
$ podman run --it --rm --entrypoint /usr/local/bin/hisat-3n   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat-3n   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat-3n-build

```bash
$ singularity exec <container> /usr/local/bin/hisat-3n-build
$ podman run --it --rm --entrypoint /usr/local/bin/hisat-3n-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat-3n-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat-3n-table

```bash
$ singularity exec <container> /usr/local/bin/hisat-3n-table
$ podman run --it --rm --entrypoint /usr/local/bin/hisat-3n-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat-3n-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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