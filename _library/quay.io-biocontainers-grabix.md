---
layout: container
name:  "quay.io/biocontainers/grabix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grabix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grabix/container.yaml"
updated_at: "2025-02-02 03:27:15.846558"
latest: "0.1.8--h077b44d_11"
container_url: "https://biocontainers.pro/tools/grabix"
aliases:
 - "grabix"
versions:
 - "0.1.8--hd03093a_7"
 - "0.1.8--hdcf5f25_9"
 - "0.1.8--hdcf5f25_10"
 - "0.1.8--h077b44d_11"
description: "shpc-registry automated BioContainers addition for grabix"
config: {"url": "https://biocontainers.pro/tools/grabix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for grabix", "latest": {"0.1.8--h077b44d_11": "sha256:8b3ef76e6d893ef83009458593246c222fce795fea281a30f95a7a88f169729a"}, "tags": {"0.1.8--hd03093a_7": "sha256:3b47aa01ebae80973bac561d1fa8cf58f3828264d744e7ee5798f72052152db8", "0.1.8--hdcf5f25_9": "sha256:10cc7c0b5b9b86cf39558b4ddd76c273966f41faa7500a293ea9fe383613ff3f", "0.1.8--hdcf5f25_10": "sha256:43f92f89d0d33519f480eb49252139424552daac2ce4d95e3b0c6635880c09aa", "0.1.8--h077b44d_11": "sha256:8b3ef76e6d893ef83009458593246c222fce795fea281a30f95a7a88f169729a"}, "docker": "quay.io/biocontainers/grabix", "aliases": {"grabix": "/usr/local/bin/grabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grabix.
shpc-registry automated BioContainers addition for grabix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grabix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grabix:0.1.8--h077b44d_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grabix/0.1.8--h077b44d_11
$ module help quay.io/biocontainers/grabix/0.1.8--h077b44d_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grabix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grabix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grabix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grabix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grabix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grabix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grabix

```bash
$ singularity exec <container> /usr/local/bin/grabix
$ podman run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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