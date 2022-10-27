---
layout: container
name:  "quay.io/biocontainers/clairvoyante"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clairvoyante/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/clairvoyante/container.yaml"
updated_at: "2022-10-27 00:48:45.334837"
latest: "1.02--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/clairvoyante"
aliases:
 - "clairvoyante.py"
 - "libpypy-c.so"
 - "libpypy-c.so.debug"
 - "pypy"
 - "pypy.debug"
 - "virtualenv-pypy"
versions:
 - "1.02--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for clairvoyante"
config: {"url": "https://biocontainers.pro/tools/clairvoyante", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clairvoyante", "latest": {"1.02--hdfd78af_2": "sha256:ff4463765f330c42a338de65fb6278d98e02cb772af052746b9f552e03812c56"}, "tags": {"1.02--hdfd78af_2": "sha256:ff4463765f330c42a338de65fb6278d98e02cb772af052746b9f552e03812c56"}, "docker": "quay.io/biocontainers/clairvoyante", "aliases": {"clairvoyante.py": "/usr/local/bin/clairvoyante.py", "libpypy-c.so": "/usr/local/bin/libpypy-c.so", "libpypy-c.so.debug": "/usr/local/bin/libpypy-c.so.debug", "pypy": "/usr/local/bin/pypy", "pypy.debug": "/usr/local/bin/pypy.debug", "virtualenv-pypy": "/usr/local/bin/virtualenv-pypy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clairvoyante.
shpc-registry automated BioContainers addition for clairvoyante
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clairvoyante
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clairvoyante:1.02--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clairvoyante/1.02--hdfd78af_2
$ module help quay.io/biocontainers/clairvoyante/1.02--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clairvoyante-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clairvoyante-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clairvoyante-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clairvoyante-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clairvoyante-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clairvoyante-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clairvoyante.py

```bash
$ singularity exec <container> /usr/local/bin/clairvoyante.py
$ podman run --it --rm --entrypoint /usr/local/bin/clairvoyante.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clairvoyante.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libpypy-c.so

```bash
$ singularity exec <container> /usr/local/bin/libpypy-c.so
$ podman run --it --rm --entrypoint /usr/local/bin/libpypy-c.so   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libpypy-c.so   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libpypy-c.so.debug

```bash
$ singularity exec <container> /usr/local/bin/libpypy-c.so.debug
$ podman run --it --rm --entrypoint /usr/local/bin/libpypy-c.so.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libpypy-c.so.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy

```bash
$ singularity exec <container> /usr/local/bin/pypy
$ podman run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy.debug

```bash
$ singularity exec <container> /usr/local/bin/pypy.debug
$ podman run --it --rm --entrypoint /usr/local/bin/pypy.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv-pypy

```bash
$ singularity exec <container> /usr/local/bin/virtualenv-pypy
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv-pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv-pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
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