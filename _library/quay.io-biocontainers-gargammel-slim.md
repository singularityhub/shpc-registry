---
layout: container
name:  "quay.io/biocontainers/gargammel-slim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gargammel-slim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gargammel-slim/container.yaml"
updated_at: "2025-12-26 03:31:53.302530"
latest: "1.1.2--hf107e4d_6"
container_url: "https://biocontainers.pro/tools/gargammel-slim"
aliases:
 - "adptSim"
 - "deamSim"
 - "fragSim"
versions:
 - "1.1.2--h51667aa_3"
 - "1.1.2--he905c8f_4"
 - "1.1.2--h06294c5_5"
 - "1.1.2--hf107e4d_6"
description: "shpc-registry automated BioContainers addition for gargammel-slim"
config: {"url": "https://biocontainers.pro/tools/gargammel-slim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gargammel-slim", "latest": {"1.1.2--hf107e4d_6": "sha256:459a7f4ba4bd42ecd59e52250c7bdc9fe66b317887f90be41cee120de6a04e9b"}, "tags": {"1.1.2--h51667aa_3": "sha256:5c50f53b654e87eda75e90e1158ee2b8f53fefe2e7f145c3f444f45466abf5e1", "1.1.2--he905c8f_4": "sha256:75225bbf40f945dd85a0f8f0f19b17e860711de4d198363f964f1bd7cd957c78", "1.1.2--h06294c5_5": "sha256:406a4e761043d95c4b241c51bb95e807d01e361cc780d99e1196c94d7f7d87c4", "1.1.2--hf107e4d_6": "sha256:459a7f4ba4bd42ecd59e52250c7bdc9fe66b317887f90be41cee120de6a04e9b"}, "docker": "quay.io/biocontainers/gargammel-slim", "aliases": {"adptSim": "/usr/local/bin/adptSim", "deamSim": "/usr/local/bin/deamSim", "fragSim": "/usr/local/bin/fragSim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gargammel-slim.
shpc-registry automated BioContainers addition for gargammel-slim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gargammel-slim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gargammel-slim:1.1.2--hf107e4d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gargammel-slim/1.1.2--hf107e4d_6
$ module help quay.io/biocontainers/gargammel-slim/1.1.2--hf107e4d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gargammel-slim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gargammel-slim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gargammel-slim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gargammel-slim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gargammel-slim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gargammel-slim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adptSim

```bash
$ singularity exec <container> /usr/local/bin/adptSim
$ podman run --it --rm --entrypoint /usr/local/bin/adptSim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adptSim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deamSim

```bash
$ singularity exec <container> /usr/local/bin/deamSim
$ podman run --it --rm --entrypoint /usr/local/bin/deamSim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deamSim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragSim

```bash
$ singularity exec <container> /usr/local/bin/fragSim
$ podman run --it --rm --entrypoint /usr/local/bin/fragSim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragSim   -v ${PWD} -w ${PWD} <container> -c " $@"
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