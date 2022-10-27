---
layout: container
name:  "quay.io/biocontainers/mono"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mono/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mono/container.yaml"
updated_at: "2022-10-27 00:47:47.091392"
latest: "4.6.2.6--0"
container_url: "https://biocontainers.pro/tools/mono"
aliases:
 - "prj2make"
versions:
 - "4.6.2.6--0"
description: "shpc-registry automated BioContainers addition for mono"
config: {"url": "https://biocontainers.pro/tools/mono", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mono", "latest": {"4.6.2.6--0": "sha256:23f820b58776a14ef6fdb1f1d21eb9353757b09574860f6ec758ce482e514c9a"}, "tags": {"4.6.2.6--0": "sha256:23f820b58776a14ef6fdb1f1d21eb9353757b09574860f6ec758ce482e514c9a"}, "docker": "quay.io/biocontainers/mono", "aliases": {"prj2make": "/usr/local/bin/prj2make"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mono.
shpc-registry automated BioContainers addition for mono
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mono
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mono:4.6.2.6--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mono/4.6.2.6--0
$ module help quay.io/biocontainers/mono/4.6.2.6--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mono-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mono-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mono-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mono-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mono-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mono-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prj2make

```bash
$ singularity exec <container> /usr/local/bin/prj2make
$ podman run --it --rm --entrypoint /usr/local/bin/prj2make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prj2make   -v ${PWD} -w ${PWD} <container> -c " $@"
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