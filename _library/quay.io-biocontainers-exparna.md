---
layout: container
name:  "quay.io/biocontainers/exparna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/exparna/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/exparna/container.yaml"
updated_at: "2022-10-27 00:54:04.735046"
latest: "1.0.1--pl5321h9f5acd7_5"
container_url: "https://biocontainers.pro/tools/exparna"
aliases:
 - "ExpaRNA"
 - "RNAmultifold"
versions:
 - "1.0.1--pl5321h9f5acd7_5"
description: "shpc-registry automated BioContainers addition for exparna"
config: {"url": "https://biocontainers.pro/tools/exparna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for exparna", "latest": {"1.0.1--pl5321h9f5acd7_5": "sha256:b49fb292fb9b0cb3806ed7ae453b997759f188f2a76a7500af2c83286bf0849d"}, "tags": {"1.0.1--pl5321h9f5acd7_5": "sha256:b49fb292fb9b0cb3806ed7ae453b997759f188f2a76a7500af2c83286bf0849d"}, "docker": "quay.io/biocontainers/exparna", "aliases": {"ExpaRNA": "/usr/local/bin/ExpaRNA", "RNAmultifold": "/usr/local/bin/RNAmultifold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/exparna.
shpc-registry automated BioContainers addition for exparna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/exparna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/exparna:1.0.1--pl5321h9f5acd7_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/exparna/1.0.1--pl5321h9f5acd7_5
$ module help quay.io/biocontainers/exparna/1.0.1--pl5321h9f5acd7_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### exparna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### exparna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### exparna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### exparna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### exparna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### exparna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ExpaRNA

```bash
$ singularity exec <container> /usr/local/bin/ExpaRNA
$ podman run --it --rm --entrypoint /usr/local/bin/ExpaRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ExpaRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
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