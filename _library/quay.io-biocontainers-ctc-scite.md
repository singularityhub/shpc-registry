---
layout: container
name:  "quay.io/biocontainers/ctc-scite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ctc-scite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ctc-scite/container.yaml"
updated_at: "2025-04-25 03:43:04.426585"
latest: "1.0.2--h9948957_0"
container_url: "https://biocontainers.pro/tools/ctc-scite"
aliases:
 - "CTC-SCITE"
versions:
 - "1.0.2--h9948957_0"
description: "singularity registry hpc automated addition for ctc-scite"
config: {"url": "https://biocontainers.pro/tools/ctc-scite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ctc-scite", "latest": {"1.0.2--h9948957_0": "sha256:32221834cd06f88dee0f7e0adf56ad7b924773fe9a16c15ef6a27baf82225c24"}, "tags": {"1.0.2--h9948957_0": "sha256:32221834cd06f88dee0f7e0adf56ad7b924773fe9a16c15ef6a27baf82225c24"}, "docker": "quay.io/biocontainers/ctc-scite", "aliases": {"CTC-SCITE": "/usr/local/bin/CTC-SCITE"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ctc-scite.
singularity registry hpc automated addition for ctc-scite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ctc-scite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ctc-scite:1.0.2--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ctc-scite/1.0.2--h9948957_0
$ module help quay.io/biocontainers/ctc-scite/1.0.2--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ctc-scite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ctc-scite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ctc-scite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ctc-scite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ctc-scite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ctc-scite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CTC-SCITE

```bash
$ singularity exec <container> /usr/local/bin/CTC-SCITE
$ podman run --it --rm --entrypoint /usr/local/bin/CTC-SCITE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CTC-SCITE   -v ${PWD} -w ${PWD} <container> -c " $@"
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