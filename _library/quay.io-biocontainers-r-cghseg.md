---
layout: container
name:  "quay.io/biocontainers/r-cghseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cghseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cghseg/container.yaml"
updated_at: "2026-02-04 04:25:48.181600"
latest: "1.0.5--r40h3121a25_3"
container_url: "https://biocontainers.pro/tools/r-cghseg"

versions:
 - "1.0.5--r40h3121a25_2"
 - "1.0.5--r40h3121a25_3"
description: "singularity registry hpc automated addition for r-cghseg"
config: {"url": "https://biocontainers.pro/tools/r-cghseg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-cghseg", "latest": {"1.0.5--r40h3121a25_3": "sha256:4f0936e25776b60d63d9bc29d25d976fd9d2afc361b6b8fab3804991da12c27e"}, "tags": {"1.0.5--r40h3121a25_2": "sha256:1993f9015878b21bef065975870a67a93c9c24da944fbc016e06f79de44a939f", "1.0.5--r40h3121a25_3": "sha256:4f0936e25776b60d63d9bc29d25d976fd9d2afc361b6b8fab3804991da12c27e"}, "docker": "quay.io/biocontainers/r-cghseg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cghseg.
singularity registry hpc automated addition for r-cghseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cghseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cghseg:1.0.5--r40h3121a25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cghseg/1.0.5--r40h3121a25_3
$ module help quay.io/biocontainers/r-cghseg/1.0.5--r40h3121a25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cghseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cghseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cghseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cghseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cghseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cghseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-cghseg

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