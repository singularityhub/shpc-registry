---
layout: container
name:  "quay.io/biocontainers/kb-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kb-python/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kb-python/container.yaml"
updated_at: "2022-10-27 00:55:02.104588"
latest: "0.27.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/kb-python"
aliases:
 - "bustools"
 - "kallisto"
 - "kb"
 - "loompy"
 - "shortuuid"
versions:
 - "0.27.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for kb-python"
config: {"url": "https://biocontainers.pro/tools/kb-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kb-python", "latest": {"0.27.3--pyhdfd78af_0": "sha256:cdfb73adb53db24d183a03951c8ae2bfacaa37c1fe64bad57ebff4c0cf0c834a"}, "tags": {"0.27.3--pyhdfd78af_0": "sha256:cdfb73adb53db24d183a03951c8ae2bfacaa37c1fe64bad57ebff4c0cf0c834a"}, "docker": "quay.io/biocontainers/kb-python", "aliases": {"bustools": "/usr/local/bin/bustools", "kallisto": "/usr/local/bin/kallisto", "kb": "/usr/local/bin/kb", "loompy": "/usr/local/bin/loompy", "shortuuid": "/usr/local/bin/shortuuid"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kb-python.
shpc-registry automated BioContainers addition for kb-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kb-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kb-python:0.27.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kb-python/0.27.3--pyhdfd78af_0
$ module help quay.io/biocontainers/kb-python/0.27.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kb-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kb-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kb-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kb-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kb-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kb-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bustools

```bash
$ singularity exec <container> /usr/local/bin/bustools
$ podman run --it --rm --entrypoint /usr/local/bin/bustools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bustools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kb

```bash
$ singularity exec <container> /usr/local/bin/kb
$ podman run --it --rm --entrypoint /usr/local/bin/kb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shortuuid

```bash
$ singularity exec <container> /usr/local/bin/shortuuid
$ podman run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
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