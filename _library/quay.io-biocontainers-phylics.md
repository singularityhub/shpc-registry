---
layout: container
name:  "quay.io/biocontainers/phylics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylics/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/phylics/container.yaml"
updated_at: "2022-10-27 00:38:13.553998"
latest: "1.0.7--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/phylics"

versions:
 - "1.0.7--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for phylics"
config: {"url": "https://biocontainers.pro/tools/phylics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylics", "latest": {"1.0.7--pyhdfd78af_0": "sha256:c686973ff9057f12c6badb1a5d0df95c7d0a210ca440a223cfd7ca763984b2cc"}, "tags": {"1.0.7--pyhdfd78af_0": "sha256:c686973ff9057f12c6badb1a5d0df95c7d0a210ca440a223cfd7ca763984b2cc"}, "docker": "quay.io/biocontainers/phylics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylics.
shpc-registry automated BioContainers addition for phylics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylics:1.0.7--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylics/1.0.7--pyhdfd78af_0
$ module help quay.io/biocontainers/phylics/1.0.7--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### phylics

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