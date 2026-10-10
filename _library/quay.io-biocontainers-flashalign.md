---
layout: container
name:  "quay.io/biocontainers/flashalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flashalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flashalign/container.yaml"
updated_at: "2026-10-10 19:51:44.626492"
latest: "0.1.0--h5814d7d_0"
container_url: "https://biocontainers.pro/tools/flashalign"
aliases:
 - "flashalign"
versions:
 - "0.1.0--h5814d7d_0"
description: "singularity registry hpc automated addition for flashalign"
config: {"url": "https://biocontainers.pro/tools/flashalign", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for flashalign", "latest": {"0.1.0--h5814d7d_0": "sha256:5d6a9a3540e7bfc71c05eb4d534859e52e70e30729e285b297ac02db3501e66a"}, "tags": {"0.1.0--h5814d7d_0": "sha256:5d6a9a3540e7bfc71c05eb4d534859e52e70e30729e285b297ac02db3501e66a"}, "docker": "quay.io/biocontainers/flashalign", "aliases": {"flashalign": "/usr/local/bin/flashalign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flashalign.
singularity registry hpc automated addition for flashalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flashalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flashalign:0.1.0--h5814d7d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flashalign/0.1.0--h5814d7d_0
$ module help quay.io/biocontainers/flashalign/0.1.0--h5814d7d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flashalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flashalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flashalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flashalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flashalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flashalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flashalign

```bash
$ singularity exec <container> /usr/local/bin/flashalign
$ podman run --it --rm --entrypoint /usr/local/bin/flashalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flashalign   -v ${PWD} -w ${PWD} <container> -c " $@"
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