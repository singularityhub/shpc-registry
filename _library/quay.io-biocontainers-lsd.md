---
layout: container
name:  "quay.io/biocontainers/lsd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lsd/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/lsd/container.yaml"
updated_at: "2022-10-27 01:15:35.336397"
latest: "2.2.3--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/lsd"
aliases:
 - "lsd"
versions:
 - "2.2.3--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for lsd"
config: {"url": "https://biocontainers.pro/tools/lsd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lsd", "latest": {"2.2.3--hdfd78af_3": "sha256:f2c02a76def877893e21f53f8f6faa46354d274f9923166802bf4b6d9c26c8d4"}, "tags": {"2.2.3--hdfd78af_3": "sha256:f2c02a76def877893e21f53f8f6faa46354d274f9923166802bf4b6d9c26c8d4"}, "docker": "quay.io/biocontainers/lsd", "aliases": {"lsd": "/usr/local/bin/lsd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lsd.
shpc-registry automated BioContainers addition for lsd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lsd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lsd:2.2.3--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lsd/2.2.3--hdfd78af_3
$ module help quay.io/biocontainers/lsd/2.2.3--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lsd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lsd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lsd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lsd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lsd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lsd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lsd

```bash
$ singularity exec <container> /usr/local/bin/lsd
$ podman run --it --rm --entrypoint /usr/local/bin/lsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsd   -v ${PWD} -w ${PWD} <container> -c " $@"
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