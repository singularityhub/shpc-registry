---
layout: container
name:  "quay.io/biocontainers/vnl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vnl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vnl/container.yaml"
updated_at: "2024-09-24 02:59:24.215397"
latest: "1.17.0--0"
container_url: "https://biocontainers.pro/tools/vnl"

versions:
 - "1.17.0--0"
description: "shpc-registry automated BioContainers addition for vnl"
config: {"url": "https://biocontainers.pro/tools/vnl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vnl", "latest": {"1.17.0--0": "sha256:4929d51c7035e5d19cf94ef7212b47657d2db1cf962f17e88db75225b393dd8a"}, "tags": {"1.17.0--0": "sha256:4929d51c7035e5d19cf94ef7212b47657d2db1cf962f17e88db75225b393dd8a"}, "docker": "quay.io/biocontainers/vnl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/vnl.
shpc-registry automated BioContainers addition for vnl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vnl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vnl:1.17.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vnl/1.17.0--0
$ module help quay.io/biocontainers/vnl/1.17.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vnl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vnl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vnl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vnl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vnl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vnl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### vnl

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