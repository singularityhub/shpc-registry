---
layout: container
name:  "quay.io/biocontainers/alamem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alamem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alamem/container.yaml"
updated_at: "2026-10-26 00:41:50.727942"
latest: "0.1.5--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/alamem"
aliases:
 - "alamem"
versions:
 - "0.1.5--hfa8f182_0"
description: "singularity registry hpc automated addition for alamem"
config: {"url": "https://biocontainers.pro/tools/alamem", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for alamem", "latest": {"0.1.5--hfa8f182_0": "sha256:e0120a040cd0430f082b38158ed8eb7a190b4be67037b9b3537cd66cf6743c4b"}, "tags": {"0.1.5--hfa8f182_0": "sha256:e0120a040cd0430f082b38158ed8eb7a190b4be67037b9b3537cd66cf6743c4b"}, "docker": "quay.io/biocontainers/alamem", "aliases": {"alamem": "/usr/local/bin/alamem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alamem.
singularity registry hpc automated addition for alamem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alamem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alamem:0.1.5--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alamem/0.1.5--hfa8f182_0
$ module help quay.io/biocontainers/alamem/0.1.5--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alamem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alamem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alamem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alamem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alamem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alamem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alamem

```bash
$ singularity exec <container> /usr/local/bin/alamem
$ podman run --it --rm --entrypoint /usr/local/bin/alamem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alamem   -v ${PWD} -w ${PWD} <container> -c " $@"
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