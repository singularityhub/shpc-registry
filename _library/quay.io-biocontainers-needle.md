---
layout: container
name:  "quay.io/biocontainers/needle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/needle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/needle/container.yaml"
updated_at: "2025-11-14 05:09:09.673468"
latest: "1.0.1--h6dccd9a_3"
container_url: "https://biocontainers.pro/tools/needle"
aliases:
 - "needle"
versions:
 - "1.0.1--h19e8d03_1"
 - "1.0.1--h6dccd9a_3"
description: "shpc-registry automated BioContainers addition for needle"
config: {"url": "https://biocontainers.pro/tools/needle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for needle", "latest": {"1.0.1--h6dccd9a_3": "sha256:31a3e95fcf248eb55eb3742d594a74a55ab3996e32d938a3a8694cd2f59774e9"}, "tags": {"1.0.1--h19e8d03_1": "sha256:f48f6909435e6d787cfcf57d6a6bf2e832557f3aeb62f63141ef204b88cf595f", "1.0.1--h6dccd9a_3": "sha256:31a3e95fcf248eb55eb3742d594a74a55ab3996e32d938a3a8694cd2f59774e9"}, "docker": "quay.io/biocontainers/needle", "aliases": {"needle": "/usr/local/bin/needle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/needle.
shpc-registry automated BioContainers addition for needle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/needle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/needle:1.0.1--h6dccd9a_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/needle/1.0.1--h6dccd9a_3
$ module help quay.io/biocontainers/needle/1.0.1--h6dccd9a_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### needle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### needle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### needle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### needle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### needle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### needle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### needle

```bash
$ singularity exec <container> /usr/local/bin/needle
$ podman run --it --rm --entrypoint /usr/local/bin/needle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/needle   -v ${PWD} -w ${PWD} <container> -c " $@"
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