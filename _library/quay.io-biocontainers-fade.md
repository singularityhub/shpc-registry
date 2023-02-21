---
layout: container
name:  "quay.io/biocontainers/fade"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fade/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fade/container.yaml"
updated_at: "2023-02-21 03:27:28.823669"
latest: "0.6.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/fade"
aliases:
 - "fade"
versions:
 - "0.6.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for fade"
config: {"url": "https://biocontainers.pro/tools/fade", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fade", "latest": {"0.6.0--h9ee0642_0": "sha256:4d5e940b1d98beaed6a0a1cd65fb5d14f8481a52435e8a0cfd799989dd46cab8"}, "tags": {"0.6.0--h9ee0642_0": "sha256:4d5e940b1d98beaed6a0a1cd65fb5d14f8481a52435e8a0cfd799989dd46cab8"}, "docker": "quay.io/biocontainers/fade", "aliases": {"fade": "/usr/local/bin/fade"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fade.
shpc-registry automated BioContainers addition for fade
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fade
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fade:0.6.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fade/0.6.0--h9ee0642_0
$ module help quay.io/biocontainers/fade/0.6.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fade-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fade-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fade-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fade-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fade-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fade-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fade

```bash
$ singularity exec <container> /usr/local/bin/fade
$ podman run --it --rm --entrypoint /usr/local/bin/fade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fade   -v ${PWD} -w ${PWD} <container> -c " $@"
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