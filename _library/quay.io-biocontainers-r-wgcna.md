---
layout: container
name:  "quay.io/biocontainers/r-wgcna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-wgcna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-wgcna/container.yaml"
updated_at: "2023-12-10 03:07:54.529836"
latest: "1.71--r43h21a89ab_4"
container_url: "https://biocontainers.pro/tools/r-wgcna"

versions:
 - "1.71--r41hecf12ef_0"
 - "1.71--r42hecf12ef_2"
 - "1.71--r42h21a89ab_3"
 - "1.71--r43h21a89ab_4"
description: "shpc-registry automated BioContainers addition for r-wgcna"
config: {"url": "https://biocontainers.pro/tools/r-wgcna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-wgcna", "latest": {"1.71--r43h21a89ab_4": "sha256:115be8815c6f96bf494e45f124ce8b60f26ae987b2538da1f925cf44da3f7727"}, "tags": {"1.71--r41hecf12ef_0": "sha256:cf8283be7ca15cb9cd473d76baebdc0ba3d0b46b14a89ec1334095c36d3f2f7e", "1.71--r42hecf12ef_2": "sha256:1ed10b40e891b9aeadfb004b4b2f5445117f7cd4bf45e54fef6131d20ea79361", "1.71--r42h21a89ab_3": "sha256:3a66fa88767dbc7647ee1a8445454100c4168e958d0e30f39b2e4b7addacc5d1", "1.71--r43h21a89ab_4": "sha256:115be8815c6f96bf494e45f124ce8b60f26ae987b2538da1f925cf44da3f7727"}, "docker": "quay.io/biocontainers/r-wgcna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-wgcna.
shpc-registry automated BioContainers addition for r-wgcna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-wgcna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-wgcna:1.71--r43h21a89ab_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-wgcna/1.71--r43h21a89ab_4
$ module help quay.io/biocontainers/r-wgcna/1.71--r43h21a89ab_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-wgcna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-wgcna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-wgcna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-wgcna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-wgcna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-wgcna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-wgcna

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