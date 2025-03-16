---
layout: container
name:  "quay.io/biocontainers/r-lisi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-lisi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-lisi/container.yaml"
updated_at: "2025-03-16 03:29:15.086352"
latest: "1.0--r44he5774e6_8"
container_url: "https://biocontainers.pro/tools/r-lisi"

versions:
 - "1.0--r41h87f3376_2"
 - "1.0--r42h87f3376_3"
 - "1.0--r43hdbdd923_5"
 - "1.0--r44he5774e6_8"
description: "shpc-registry automated BioContainers addition for r-lisi"
config: {"url": "https://biocontainers.pro/tools/r-lisi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-lisi", "latest": {"1.0--r44he5774e6_8": "sha256:7455a3829e0ee9915b0fcce295a0ca1944160bfdcbc5926b0399c50fdb1139d9"}, "tags": {"1.0--r41h87f3376_2": "sha256:5289da382b76282584187a4940c70b3ac2b7f07ee516142e27ae8585c5e1acfb", "1.0--r42h87f3376_3": "sha256:40d80a74cbfaa1ee76bd4479f9aa15c1535eddee811d4f5c3a7152151c5a0874", "1.0--r43hdbdd923_5": "sha256:f9cef982b7b085212f1402d5d1603b7662b0e1d451458c4ef67f680f2183a6df", "1.0--r44he5774e6_8": "sha256:7455a3829e0ee9915b0fcce295a0ca1944160bfdcbc5926b0399c50fdb1139d9"}, "docker": "quay.io/biocontainers/r-lisi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-lisi.
shpc-registry automated BioContainers addition for r-lisi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-lisi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-lisi:1.0--r44he5774e6_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-lisi/1.0--r44he5774e6_8
$ module help quay.io/biocontainers/r-lisi/1.0--r44he5774e6_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-lisi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-lisi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-lisi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-lisi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-lisi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-lisi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-lisi

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