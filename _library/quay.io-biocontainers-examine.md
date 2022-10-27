---
layout: container
name:  "quay.io/biocontainers/examine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/examine/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/examine/container.yaml"
updated_at: "2022-10-27 01:14:30.506533"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/examine"
aliases:
 - "examine"
versions:
 - "1.0.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for examine"
config: {"url": "https://biocontainers.pro/tools/examine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for examine", "latest": {"1.0.1--hdfd78af_0": "sha256:5e339f17aa79cded33c2d25420fe53b90bcb5a5a865b058fb5e8cf509c4b117a"}, "tags": {"1.0.1--hdfd78af_0": "sha256:5e339f17aa79cded33c2d25420fe53b90bcb5a5a865b058fb5e8cf509c4b117a"}, "docker": "quay.io/biocontainers/examine", "aliases": {"examine": "/usr/local/bin/examine"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/examine.
shpc-registry automated BioContainers addition for examine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/examine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/examine:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/examine/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/examine/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### examine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### examine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### examine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### examine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### examine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### examine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### examine

```bash
$ singularity exec <container> /usr/local/bin/examine
$ podman run --it --rm --entrypoint /usr/local/bin/examine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/examine   -v ${PWD} -w ${PWD} <container> -c " $@"
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