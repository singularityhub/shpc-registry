---
layout: container
name:  "quay.io/biocontainers/fastobo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastobo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fastobo/container.yaml"
updated_at: "2022-10-27 00:41:47.944480"
latest: "0.9.3--py37hfa133b6_0"
container_url: "https://biocontainers.pro/tools/fastobo"

versions:
 - "0.9.3--py37hfa133b6_0"
description: "shpc-registry automated BioContainers addition for fastobo"
config: {"url": "https://biocontainers.pro/tools/fastobo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastobo", "latest": {"0.9.3--py37hfa133b6_0": "sha256:198362f9416f7adef5678bf2cc4da2c9807c0ba5e1affdb8b71339157089cacd"}, "tags": {"0.9.3--py37hfa133b6_0": "sha256:198362f9416f7adef5678bf2cc4da2c9807c0ba5e1affdb8b71339157089cacd"}, "docker": "quay.io/biocontainers/fastobo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastobo.
shpc-registry automated BioContainers addition for fastobo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastobo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastobo:0.9.3--py37hfa133b6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastobo/0.9.3--py37hfa133b6_0
$ module help quay.io/biocontainers/fastobo/0.9.3--py37hfa133b6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastobo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastobo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastobo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastobo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastobo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastobo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fastobo

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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