---
layout: container
name:  "quay.io/biocontainers/dinamo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dinamo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dinamo/container.yaml"
updated_at: "2025-03-24 03:46:02.338968"
latest: "1.0--h9948957_7"
container_url: "https://biocontainers.pro/tools/dinamo"
aliases:
 - "dinamo"
versions:
 - "1.0--h2df963e_2"
 - "1.0--h376f1d3_4"
 - "1.0--h376f1d3_5"
 - "1.0--h78569d1_6"
 - "1.0--h4ac6f70_6"
 - "1.0--h9948957_7"
description: "shpc-registry automated BioContainers addition for dinamo"
config: {"url": "https://biocontainers.pro/tools/dinamo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dinamo", "latest": {"1.0--h9948957_7": "sha256:e7fcc07237130e8ffbb1e3a0ca247d80bb60c151dca41eacd4d0a139bbc255d0"}, "tags": {"1.0--h2df963e_2": "sha256:ab8ac75d97e570584c3ab7f30c6f1c9eb2675a3253dc7326bd39bc3aa48cccf3", "1.0--h376f1d3_4": "sha256:64227a611f7a3bc8fc4571cbcd5428d4e6ed4694c7f409c4fb04b46ac9acecde", "1.0--h376f1d3_5": "sha256:1b664ffe850bdf862632e485c4d48bfedd4055d6d78e709f07b51a4a2e7d70e0", "1.0--h78569d1_6": "sha256:405e20996c492273e564d7ed511830fe746d7a61cd9d3130e7a957ac933d428e", "1.0--h4ac6f70_6": "sha256:4a136d45a85d64b8552b50eaa72b9225a14bd5410f4e912bacdf50e38d1d0457", "1.0--h9948957_7": "sha256:e7fcc07237130e8ffbb1e3a0ca247d80bb60c151dca41eacd4d0a139bbc255d0"}, "docker": "quay.io/biocontainers/dinamo", "aliases": {"dinamo": "/usr/local/bin/dinamo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dinamo.
shpc-registry automated BioContainers addition for dinamo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dinamo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dinamo:1.0--h9948957_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dinamo/1.0--h9948957_7
$ module help quay.io/biocontainers/dinamo/1.0--h9948957_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dinamo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dinamo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dinamo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dinamo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dinamo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dinamo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dinamo

```bash
$ singularity exec <container> /usr/local/bin/dinamo
$ podman run --it --rm --entrypoint /usr/local/bin/dinamo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dinamo   -v ${PWD} -w ${PWD} <container> -c " $@"
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