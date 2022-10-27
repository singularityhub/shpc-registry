---
layout: container
name:  "quay.io/biocontainers/illumiprocessor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/illumiprocessor/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/illumiprocessor/container.yaml"
updated_at: "2022-10-27 00:52:47.197127"
latest: "2.10--py_0"
container_url: "https://biocontainers.pro/tools/illumiprocessor"
aliases:
 - "illumiprocessor"
versions:
 - "2.10--py_0"
description: "shpc-registry automated BioContainers addition for illumiprocessor"
config: {"url": "https://biocontainers.pro/tools/illumiprocessor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for illumiprocessor", "latest": {"2.10--py_0": "sha256:f7979a71865516fc7782b32947106b8dcd4ca526cc569d3e64e17be6fec245ba"}, "tags": {"2.10--py_0": "sha256:f7979a71865516fc7782b32947106b8dcd4ca526cc569d3e64e17be6fec245ba"}, "docker": "quay.io/biocontainers/illumiprocessor", "aliases": {"illumiprocessor": "/usr/local/bin/illumiprocessor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/illumiprocessor.
shpc-registry automated BioContainers addition for illumiprocessor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/illumiprocessor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/illumiprocessor:2.10--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/illumiprocessor/2.10--py_0
$ module help quay.io/biocontainers/illumiprocessor/2.10--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### illumiprocessor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### illumiprocessor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### illumiprocessor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### illumiprocessor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### illumiprocessor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### illumiprocessor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### illumiprocessor

```bash
$ singularity exec <container> /usr/local/bin/illumiprocessor
$ podman run --it --rm --entrypoint /usr/local/bin/illumiprocessor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illumiprocessor   -v ${PWD} -w ${PWD} <container> -c " $@"
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