---
layout: container
name:  "quay.io/biocontainers/irma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irma/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/irma/container.yaml"
updated_at: "2022-10-27 00:27:19.587929"
latest: "1.0.2--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/irma"
aliases:
 - "IRMA"
 - "LABEL"
 - "QUICK_INSTALL.txt"
versions:
 - "1.0.2--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for irma"
config: {"url": "https://biocontainers.pro/tools/irma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irma", "latest": {"1.0.2--pl5321hdfd78af_2": "sha256:1ae0ba56c93255dd42011f02887d78decae4b0231940ba47d08c378de1e4ccc9"}, "tags": {"1.0.2--pl5321hdfd78af_2": "sha256:1ae0ba56c93255dd42011f02887d78decae4b0231940ba47d08c378de1e4ccc9"}, "docker": "quay.io/biocontainers/irma", "aliases": {"IRMA": "/usr/local/bin/IRMA", "LABEL": "/usr/local/bin/LABEL", "QUICK_INSTALL.txt": "/usr/local/bin/QUICK_INSTALL.txt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/irma.
shpc-registry automated BioContainers addition for irma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/irma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/irma:1.0.2--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/irma/1.0.2--pl5321hdfd78af_2
$ module help quay.io/biocontainers/irma/1.0.2--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### irma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### irma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### irma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### irma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### irma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### irma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### IRMA

```bash
$ singularity exec <container> /usr/local/bin/IRMA
$ podman run --it --rm --entrypoint /usr/local/bin/IRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LABEL

```bash
$ singularity exec <container> /usr/local/bin/LABEL
$ podman run --it --rm --entrypoint /usr/local/bin/LABEL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABEL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### QUICK_INSTALL.txt

```bash
$ singularity exec <container> /usr/local/bin/QUICK_INSTALL.txt
$ podman run --it --rm --entrypoint /usr/local/bin/QUICK_INSTALL.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QUICK_INSTALL.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
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