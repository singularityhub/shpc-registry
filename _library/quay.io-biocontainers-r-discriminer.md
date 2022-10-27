---
layout: container
name:  "quay.io/biocontainers/r-discriminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-discriminer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-discriminer/container.yaml"
updated_at: "2022-10-27 01:04:29.113816"
latest: "0.1_29--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-discriminer"

versions:
 - "0.1_29--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-discriminer"
config: {"url": "https://biocontainers.pro/tools/r-discriminer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-discriminer", "latest": {"0.1_29--r3.2.2_0": "sha256:87815ea6aadda7eeccb399f84ea79918509cfd77a381f2e4b19ba666f6334494"}, "tags": {"0.1_29--r3.2.2_0": "sha256:87815ea6aadda7eeccb399f84ea79918509cfd77a381f2e4b19ba666f6334494"}, "docker": "quay.io/biocontainers/r-discriminer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-discriminer.
shpc-registry automated BioContainers addition for r-discriminer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-discriminer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-discriminer:0.1_29--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-discriminer/0.1_29--r3.2.2_0
$ module help quay.io/biocontainers/r-discriminer/0.1_29--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-discriminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-discriminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-discriminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-discriminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-discriminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-discriminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-discriminer

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