---
layout: container
name:  "quay.io/biocontainers/r-pophelper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pophelper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pophelper/container.yaml"
updated_at: "2024-05-11 02:59:07.799963"
latest: "2.3.1--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/r-pophelper"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.3.1--r41hdfd78af_2"
 - "2.3.1--r42hdfd78af_3"
 - "2.3.1--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for r-pophelper"
config: {"url": "https://biocontainers.pro/tools/r-pophelper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-pophelper", "latest": {"2.3.1--r43hdfd78af_4": "sha256:5258a619faba17728db2d0d5e9e75b41a880c6481e0693ef0d9536b854d13f93"}, "tags": {"2.3.1--r41hdfd78af_2": "sha256:fc3cf60bce1f4ba6157df792b9dd59aa4dbbf5ac88ccdf73c5aeee4327667ab2", "2.3.1--r42hdfd78af_3": "sha256:2c722df01484edd0090fe40888b91896e57388b8b8338aead08efcedd597813b", "2.3.1--r43hdfd78af_4": "sha256:5258a619faba17728db2d0d5e9e75b41a880c6481e0693ef0d9536b854d13f93"}, "docker": "quay.io/biocontainers/r-pophelper", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pophelper.
shpc-registry automated BioContainers addition for r-pophelper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pophelper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pophelper:2.3.1--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pophelper/2.3.1--r43hdfd78af_4
$ module help quay.io/biocontainers/r-pophelper/2.3.1--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pophelper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pophelper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pophelper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pophelper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pophelper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pophelper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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