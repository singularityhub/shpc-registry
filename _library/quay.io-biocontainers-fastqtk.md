---
layout: container
name:  "quay.io/biocontainers/fastqtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastqtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastqtk/container.yaml"
updated_at: "2023-03-17 03:01:17.148907"
latest: "0.27--h5b5514e_1"
container_url: "https://biocontainers.pro/tools/fastqtk"
aliases:
 - "fastqtk"
versions:
 - "0.27--h5b5514e_1"
description: "singularity registry hpc automated addition for fastqtk"
config: {"url": "https://biocontainers.pro/tools/fastqtk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastqtk", "latest": {"0.27--h5b5514e_1": "sha256:c4fa685a5ee96a2b528b40e9676e06d1cfa259cbe6cedbca57562b09d2b50320"}, "tags": {"0.27--h5b5514e_1": "sha256:c4fa685a5ee96a2b528b40e9676e06d1cfa259cbe6cedbca57562b09d2b50320"}, "docker": "quay.io/biocontainers/fastqtk", "aliases": {"fastqtk": "/usr/local/bin/fastqtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastqtk.
singularity registry hpc automated addition for fastqtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastqtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastqtk:0.27--h5b5514e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastqtk/0.27--h5b5514e_1
$ module help quay.io/biocontainers/fastqtk/0.27--h5b5514e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastqtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastqtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastqtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastqtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastqtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastqtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastqtk

```bash
$ singularity exec <container> /usr/local/bin/fastqtk
$ podman run --it --rm --entrypoint /usr/local/bin/fastqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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