---
layout: container
name:  "quay.io/biocontainers/neffy-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/neffy-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/neffy-cli/container.yaml"
updated_at: "2025-11-08 03:53:37.036133"
latest: "0.1.1--h9948957_0"
container_url: "https://biocontainers.pro/tools/neffy-cli"
aliases:
 - "converter"
 - "neff"
versions:
 - "0.1.1--h9948957_0"
description: "singularity registry hpc automated addition for neffy-cli"
config: {"url": "https://biocontainers.pro/tools/neffy-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for neffy-cli", "latest": {"0.1.1--h9948957_0": "sha256:e5804d13ec5524f0dee2ed5561fcd80970bbc278cf79f2d9cc02fb0c570e5423"}, "tags": {"0.1.1--h9948957_0": "sha256:e5804d13ec5524f0dee2ed5561fcd80970bbc278cf79f2d9cc02fb0c570e5423"}, "docker": "quay.io/biocontainers/neffy-cli", "aliases": {"converter": "/usr/local/bin/converter", "neff": "/usr/local/bin/neff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/neffy-cli.
singularity registry hpc automated addition for neffy-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/neffy-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/neffy-cli:0.1.1--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/neffy-cli/0.1.1--h9948957_0
$ module help quay.io/biocontainers/neffy-cli/0.1.1--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### neffy-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### neffy-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### neffy-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### neffy-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### neffy-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### neffy-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### converter

```bash
$ singularity exec <container> /usr/local/bin/converter
$ podman run --it --rm --entrypoint /usr/local/bin/converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### neff

```bash
$ singularity exec <container> /usr/local/bin/neff
$ podman run --it --rm --entrypoint /usr/local/bin/neff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neff   -v ${PWD} -w ${PWD} <container> -c " $@"
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