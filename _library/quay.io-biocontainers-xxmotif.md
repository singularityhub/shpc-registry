---
layout: container
name:  "quay.io/biocontainers/xxmotif"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xxmotif/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xxmotif/container.yaml"
updated_at: "2025-02-11 03:39:34.911829"
latest: "1.6--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/xxmotif"
aliases:
 - "XXmotif"
versions:
 - "1.6--h2d50403_2"
 - "1.6--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for xxmotif"
config: {"url": "https://biocontainers.pro/tools/xxmotif", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xxmotif", "latest": {"1.6--h9f5acd7_4": "sha256:9808ac633c97cfb8b72b301b3793eec306c6638bb2f1e16f368fe7756c80b420"}, "tags": {"1.6--h2d50403_2": "sha256:7bc01cae2dde50784481c04307362f1c9bb46ed8c2e79462642d7a5ea662e378", "1.6--h9f5acd7_4": "sha256:9808ac633c97cfb8b72b301b3793eec306c6638bb2f1e16f368fe7756c80b420"}, "docker": "quay.io/biocontainers/xxmotif", "aliases": {"XXmotif": "/usr/local/bin/XXmotif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xxmotif.
shpc-registry automated BioContainers addition for xxmotif
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xxmotif
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xxmotif:1.6--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xxmotif/1.6--h9f5acd7_4
$ module help quay.io/biocontainers/xxmotif/1.6--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xxmotif-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xxmotif-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xxmotif-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xxmotif-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xxmotif-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xxmotif-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### XXmotif

```bash
$ singularity exec <container> /usr/local/bin/XXmotif
$ podman run --it --rm --entrypoint /usr/local/bin/XXmotif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/XXmotif   -v ${PWD} -w ${PWD} <container> -c " $@"
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