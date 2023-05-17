---
layout: container
name:  "quay.io/biocontainers/fastani"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastani/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastani/container.yaml"
updated_at: "2023-05-17 03:19:05.419413"
latest: "1.33--h0fdf51a_1"
container_url: "https://biocontainers.pro/tools/fastani"
aliases:
 - "fastANI"
versions:
 - "1.33--h0fdf51a_1"
description: "shpc-registry automated BioContainers addition for fastani"
config: {"url": "https://biocontainers.pro/tools/fastani", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastani", "latest": {"1.33--h0fdf51a_1": "sha256:4ba79083702b537aa7478c29870a41e651c3a1c9f6ed63fabd8fca6539686efe"}, "tags": {"1.33--h0fdf51a_1": "sha256:4ba79083702b537aa7478c29870a41e651c3a1c9f6ed63fabd8fca6539686efe"}, "docker": "quay.io/biocontainers/fastani", "aliases": {"fastANI": "/usr/local/bin/fastANI"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastani.
shpc-registry automated BioContainers addition for fastani
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastani
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastani:1.33--h0fdf51a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastani/1.33--h0fdf51a_1
$ module help quay.io/biocontainers/fastani/1.33--h0fdf51a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastani-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastani-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastani-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastani-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastani-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastani-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
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