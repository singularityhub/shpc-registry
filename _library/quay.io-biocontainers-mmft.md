---
layout: container
name:  "quay.io/biocontainers/mmft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmft/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmft/container.yaml"
updated_at: "2025-10-31 04:15:30.428537"
latest: "0.3.2--hc1c3326_0"
container_url: "https://biocontainers.pro/tools/mmft"
aliases:
 - "mmft"
versions:
 - "0.2.1--hc1c3326_0"
 - "0.3.2--hc1c3326_0"
description: "singularity registry hpc automated addition for mmft"
config: {"url": "https://biocontainers.pro/tools/mmft", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mmft", "latest": {"0.3.2--hc1c3326_0": "sha256:0776cfec83b5efd95212fda8c4372c33e3293bf4b6447a3ef3fbd525673798a7"}, "tags": {"0.2.1--hc1c3326_0": "sha256:548b6364a73abb0d9fadc849c8a3d4b7162f00f2a503ce767418d3f743fc862e", "0.3.2--hc1c3326_0": "sha256:0776cfec83b5efd95212fda8c4372c33e3293bf4b6447a3ef3fbd525673798a7"}, "docker": "quay.io/biocontainers/mmft", "aliases": {"mmft": "/usr/local/bin/mmft"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmft.
singularity registry hpc automated addition for mmft
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmft
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmft:0.3.2--hc1c3326_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmft/0.3.2--hc1c3326_0
$ module help quay.io/biocontainers/mmft/0.3.2--hc1c3326_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmft-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmft-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmft-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmft-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mmft

```bash
$ singularity exec <container> /usr/local/bin/mmft
$ podman run --it --rm --entrypoint /usr/local/bin/mmft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmft   -v ${PWD} -w ${PWD} <container> -c " $@"
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