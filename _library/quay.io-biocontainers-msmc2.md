---
layout: container
name:  "quay.io/biocontainers/msmc2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msmc2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msmc2/container.yaml"
updated_at: "2024-08-16 03:07:36.088664"
latest: "2.1.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/msmc2"
aliases:
 - "msmc2_Linux"
versions:
 - "2.1.4--hdfd78af_0"
description: "singularity registry hpc automated addition for msmc2"
config: {"url": "https://biocontainers.pro/tools/msmc2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for msmc2", "latest": {"2.1.4--hdfd78af_0": "sha256:b0b71fa1586514f96a53a74aebad634513e624e89b503370525f95a8f0cd175c"}, "tags": {"2.1.4--hdfd78af_0": "sha256:b0b71fa1586514f96a53a74aebad634513e624e89b503370525f95a8f0cd175c"}, "docker": "quay.io/biocontainers/msmc2", "aliases": {"msmc2_Linux": "/usr/local/bin/msmc2_Linux"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msmc2.
singularity registry hpc automated addition for msmc2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msmc2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msmc2:2.1.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msmc2/2.1.4--hdfd78af_0
$ module help quay.io/biocontainers/msmc2/2.1.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msmc2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msmc2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msmc2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msmc2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msmc2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msmc2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msmc2_Linux

```bash
$ singularity exec <container> /usr/local/bin/msmc2_Linux
$ podman run --it --rm --entrypoint /usr/local/bin/msmc2_Linux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msmc2_Linux   -v ${PWD} -w ${PWD} <container> -c " $@"
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