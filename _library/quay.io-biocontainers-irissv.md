---
layout: container
name:  "quay.io/biocontainers/irissv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irissv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/irissv/container.yaml"
updated_at: "2022-10-27 01:04:27.378457"
latest: "1.0.4--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/irissv"
aliases:
 - "iris"
 - "iris.jar"
versions:
 - "1.0.4--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for irissv"
config: {"url": "https://biocontainers.pro/tools/irissv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irissv", "latest": {"1.0.4--hdfd78af_2": "sha256:e854b554b11377b9b47f32d1c33b13d84b9fde2c5b99045d946f1e01568ec6a1"}, "tags": {"1.0.4--hdfd78af_2": "sha256:e854b554b11377b9b47f32d1c33b13d84b9fde2c5b99045d946f1e01568ec6a1"}, "docker": "quay.io/biocontainers/irissv", "aliases": {"iris": "/usr/local/bin/iris", "iris.jar": "/usr/local/bin/iris.jar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/irissv.
shpc-registry automated BioContainers addition for irissv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/irissv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/irissv:1.0.4--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/irissv/1.0.4--hdfd78af_2
$ module help quay.io/biocontainers/irissv/1.0.4--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### irissv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### irissv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### irissv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### irissv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### irissv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### irissv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iris

```bash
$ singularity exec <container> /usr/local/bin/iris
$ podman run --it --rm --entrypoint /usr/local/bin/iris   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iris   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iris.jar

```bash
$ singularity exec <container> /usr/local/bin/iris.jar
$ podman run --it --rm --entrypoint /usr/local/bin/iris.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iris.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
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