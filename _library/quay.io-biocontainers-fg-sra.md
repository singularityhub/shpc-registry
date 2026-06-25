---
layout: container
name:  "quay.io/biocontainers/fg-sra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fg-sra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fg-sra/container.yaml"
updated_at: "2026-06-25 06:53:32.164684"
latest: "0.1.0--hdaf81d9_0"
container_url: "https://biocontainers.pro/tools/fg-sra"
aliases:
 - "fg-sra"
versions:
 - "0.1.0--hdaf81d9_0"
description: "singularity registry hpc automated addition for fg-sra"
config: {"url": "https://biocontainers.pro/tools/fg-sra", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fg-sra", "latest": {"0.1.0--hdaf81d9_0": "sha256:bc02a2ff35f1c9fa7c30be4130c7942d9b93434e7717fc207fc8aa4eaaaac9ec"}, "tags": {"0.1.0--hdaf81d9_0": "sha256:bc02a2ff35f1c9fa7c30be4130c7942d9b93434e7717fc207fc8aa4eaaaac9ec"}, "docker": "quay.io/biocontainers/fg-sra", "aliases": {"fg-sra": "/usr/local/bin/fg-sra"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fg-sra.
singularity registry hpc automated addition for fg-sra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fg-sra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fg-sra:0.1.0--hdaf81d9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fg-sra/0.1.0--hdaf81d9_0
$ module help quay.io/biocontainers/fg-sra/0.1.0--hdaf81d9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fg-sra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fg-sra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fg-sra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fg-sra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fg-sra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fg-sra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fg-sra

```bash
$ singularity exec <container> /usr/local/bin/fg-sra
$ podman run --it --rm --entrypoint /usr/local/bin/fg-sra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fg-sra   -v ${PWD} -w ${PWD} <container> -c " $@"
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