---
layout: container
name:  "quay.io/biocontainers/catfasta2phyml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/catfasta2phyml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/catfasta2phyml/container.yaml"
updated_at: "2025-04-22 03:39:43.124546"
latest: "1.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/catfasta2phyml"
aliases:
 - "catfasta2phyml"
versions:
 - "1.2.0--hdfd78af_0"
 - "1.2.1--hdfd78af_0"
description: "singularity registry hpc automated addition for catfasta2phyml"
config: {"url": "https://biocontainers.pro/tools/catfasta2phyml", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for catfasta2phyml", "latest": {"1.2.1--hdfd78af_0": "sha256:bb903db6eecae77b4d7296bee9d461c25be40b2ee64460c83771a3cc7ceb9374"}, "tags": {"1.2.0--hdfd78af_0": "sha256:3f950b0242e2aace28f6bd9ea441309085c56ab9a4d762ba60dd3d9c7362034d", "1.2.1--hdfd78af_0": "sha256:bb903db6eecae77b4d7296bee9d461c25be40b2ee64460c83771a3cc7ceb9374"}, "docker": "quay.io/biocontainers/catfasta2phyml", "aliases": {"catfasta2phyml": "/usr/local/bin/catfasta2phyml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/catfasta2phyml.
singularity registry hpc automated addition for catfasta2phyml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/catfasta2phyml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/catfasta2phyml:1.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/catfasta2phyml/1.2.1--hdfd78af_0
$ module help quay.io/biocontainers/catfasta2phyml/1.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### catfasta2phyml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### catfasta2phyml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### catfasta2phyml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### catfasta2phyml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### catfasta2phyml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### catfasta2phyml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### catfasta2phyml

```bash
$ singularity exec <container> /usr/local/bin/catfasta2phyml
$ podman run --it --rm --entrypoint /usr/local/bin/catfasta2phyml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catfasta2phyml   -v ${PWD} -w ${PWD} <container> -c " $@"
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