---
layout: container
name:  "quay.io/biocontainers/nonpareil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nonpareil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nonpareil/container.yaml"
updated_at: "2023-03-09 03:38:43.316392"
latest: "3.4.1--r41h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/nonpareil"
aliases:
 - "nonpareil"
versions:
 - "3.4.1--r41h9f5acd7_1"
description: "shpc-registry automated BioContainers addition for nonpareil"
config: {"url": "https://biocontainers.pro/tools/nonpareil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nonpareil", "latest": {"3.4.1--r41h9f5acd7_1": "sha256:c5a505e4313c44fa008fad2afa551cd50b2ea33f50dd2e4e3859c20f02bbab6b"}, "tags": {"3.4.1--r41h9f5acd7_1": "sha256:c5a505e4313c44fa008fad2afa551cd50b2ea33f50dd2e4e3859c20f02bbab6b"}, "docker": "quay.io/biocontainers/nonpareil", "aliases": {"nonpareil": "/usr/local/bin/nonpareil"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nonpareil.
shpc-registry automated BioContainers addition for nonpareil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nonpareil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nonpareil:3.4.1--r41h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nonpareil/3.4.1--r41h9f5acd7_1
$ module help quay.io/biocontainers/nonpareil/3.4.1--r41h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nonpareil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nonpareil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nonpareil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nonpareil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nonpareil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nonpareil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nonpareil

```bash
$ singularity exec <container> /usr/local/bin/nonpareil
$ podman run --it --rm --entrypoint /usr/local/bin/nonpareil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nonpareil   -v ${PWD} -w ${PWD} <container> -c " $@"
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