---
layout: container
name:  "quay.io/biocontainers/r-metacoder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-metacoder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-metacoder/container.yaml"
updated_at: "2023-03-10 03:08:54.312593"
latest: "0.3.5--r42hecf12ef_2"
container_url: "https://biocontainers.pro/tools/r-metacoder"

versions:
 - "0.3.5--r41hecf12ef_1"
 - "0.3.5--r42hecf12ef_2"
description: "shpc-registry automated BioContainers addition for r-metacoder"
config: {"url": "https://biocontainers.pro/tools/r-metacoder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-metacoder", "latest": {"0.3.5--r42hecf12ef_2": "sha256:014f333643f9a42999ff7c1296428e728315227f0fe4616564252563c195f906"}, "tags": {"0.3.5--r41hecf12ef_1": "sha256:8696246aa3556d541a75ec7bb7554db97bdfc3a513509cc3bbf4bf58fde44510", "0.3.5--r42hecf12ef_2": "sha256:014f333643f9a42999ff7c1296428e728315227f0fe4616564252563c195f906"}, "docker": "quay.io/biocontainers/r-metacoder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-metacoder.
shpc-registry automated BioContainers addition for r-metacoder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-metacoder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-metacoder:0.3.5--r42hecf12ef_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-metacoder/0.3.5--r42hecf12ef_2
$ module help quay.io/biocontainers/r-metacoder/0.3.5--r42hecf12ef_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-metacoder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-metacoder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-metacoder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-metacoder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-metacoder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-metacoder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-metacoder

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