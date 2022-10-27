---
layout: container
name:  "quay.io/biocontainers/ostir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ostir/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ostir/container.yaml"
updated_at: "2022-10-27 00:40:19.719455"
latest: "1.0.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ostir"
aliases:
 - "ostir"
versions:
 - "1.0.6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ostir"
config: {"url": "https://biocontainers.pro/tools/ostir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ostir", "latest": {"1.0.6--pyhdfd78af_0": "sha256:4f6d965f7f20e3f8562fa59259aa995773ac37c6c0987444782f719036348296"}, "tags": {"1.0.6--pyhdfd78af_0": "sha256:4f6d965f7f20e3f8562fa59259aa995773ac37c6c0987444782f719036348296"}, "docker": "quay.io/biocontainers/ostir", "aliases": {"ostir": "/usr/local/bin/ostir"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ostir.
shpc-registry automated BioContainers addition for ostir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ostir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ostir:1.0.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ostir/1.0.6--pyhdfd78af_0
$ module help quay.io/biocontainers/ostir/1.0.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ostir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ostir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ostir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ostir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ostir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ostir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ostir

```bash
$ singularity exec <container> /usr/local/bin/ostir
$ podman run --it --rm --entrypoint /usr/local/bin/ostir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ostir   -v ${PWD} -w ${PWD} <container> -c " $@"
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