---
layout: container
name:  "quay.io/biocontainers/hiphase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hiphase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hiphase/container.yaml"
updated_at: "2023-09-06 03:07:52.585520"
latest: "0.10.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/hiphase"
aliases:
 - "hiphase"
versions:
 - "0.8.1--h9ee0642_0"
 - "0.10.0--h9ee0642_0"
description: "singularity registry hpc automated addition for hiphase"
config: {"url": "https://biocontainers.pro/tools/hiphase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hiphase", "latest": {"0.10.0--h9ee0642_0": "sha256:8c8259a75e02882a590c687a33d6a405f84a679beea73b13779ec5f01db25bf1"}, "tags": {"0.8.1--h9ee0642_0": "sha256:d05bc9e2f41528acafb442044cf1d193cfd3cfb1fafbc6c5417b91f3b557b36b", "0.10.0--h9ee0642_0": "sha256:8c8259a75e02882a590c687a33d6a405f84a679beea73b13779ec5f01db25bf1"}, "docker": "quay.io/biocontainers/hiphase", "aliases": {"hiphase": "/usr/local/bin/hiphase"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hiphase.
singularity registry hpc automated addition for hiphase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hiphase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hiphase:0.10.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hiphase/0.10.0--h9ee0642_0
$ module help quay.io/biocontainers/hiphase/0.10.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hiphase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hiphase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hiphase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hiphase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hiphase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hiphase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hiphase

```bash
$ singularity exec <container> /usr/local/bin/hiphase
$ podman run --it --rm --entrypoint /usr/local/bin/hiphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiphase   -v ${PWD} -w ${PWD} <container> -c " $@"
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