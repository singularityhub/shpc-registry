---
layout: container
name:  "quay.io/biocontainers/roary"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/roary/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/roary/container.yaml"
updated_at: "2023-08-20 02:38:32.817411"
latest: "3.13.0--pl526h516909a_0"
container_url: "https://biocontainers.pro/tools/roary"

versions:
 - "3.9.1--pl5.22.0_0"
 - "3.13.0--pl526h516909a_0"
 - "3.12.0--pl526h516909a_2"
 - "3.10.2--pl5.22.0_0"
description: "shpc-registry automated BioContainers addition for roary"
config: {"url": "https://biocontainers.pro/tools/roary", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for roary", "latest": {"3.13.0--pl526h516909a_0": "sha256:bff7bde69fe0015cf9673fd7657d81c33a4035882d270019f42250e903f51a5d"}, "tags": {"3.9.1--pl5.22.0_0": "sha256:2b149b0c13975b729d1d8cc9e11fdb6613b7de8b49ee5c58c06ff05d16d3c40d", "3.13.0--pl526h516909a_0": "sha256:bff7bde69fe0015cf9673fd7657d81c33a4035882d270019f42250e903f51a5d", "3.12.0--pl526h516909a_2": "sha256:316cfe907b21c10f78ecd4e8b074ab28083fb994a83479f01b1b7c7fc9b655c0", "3.10.2--pl5.22.0_0": "sha256:1ec4554d34e07276f6c1396beaec3d5f5f5c2654edcb8e7d435563142c62035e"}, "docker": "quay.io/biocontainers/roary"}
---

This module is a singularity container wrapper for quay.io/biocontainers/roary.
shpc-registry automated BioContainers addition for roary
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/roary
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/roary:3.13.0--pl526h516909a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/roary/3.13.0--pl526h516909a_0
$ module help quay.io/biocontainers/roary/3.13.0--pl526h516909a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### roary-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### roary-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### roary-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### roary-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### roary-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### roary-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### roary

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