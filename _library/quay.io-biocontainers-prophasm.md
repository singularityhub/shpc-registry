---
layout: container
name:  "quay.io/biocontainers/prophasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prophasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prophasm/container.yaml"
updated_at: "2025-05-16 03:36:10.520554"
latest: "0.1.1--h077b44d_5"
container_url: "https://biocontainers.pro/tools/prophasm"
aliases:
 - "prophasm"
versions:
 - "0.1.1--hd03093a_2"
 - "0.1.1--hdcf5f25_4"
 - "0.1.1--h077b44d_5"
description: "shpc-registry automated BioContainers addition for prophasm"
config: {"url": "https://biocontainers.pro/tools/prophasm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prophasm", "latest": {"0.1.1--h077b44d_5": "sha256:b9a496ec54f772cccbd09b1c21e82e75f7a7a30d917f3353b86f570f40fe7f04"}, "tags": {"0.1.1--hd03093a_2": "sha256:96c523622d565b62749dba9c97e3e371d423e3905cb35075bac332d6196bc1cf", "0.1.1--hdcf5f25_4": "sha256:200a2385244d75f12380f7af3c33c68d652aaad87bd251d693744ed803899d72", "0.1.1--h077b44d_5": "sha256:b9a496ec54f772cccbd09b1c21e82e75f7a7a30d917f3353b86f570f40fe7f04"}, "docker": "quay.io/biocontainers/prophasm", "aliases": {"prophasm": "/usr/local/bin/prophasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prophasm.
shpc-registry automated BioContainers addition for prophasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prophasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prophasm:0.1.1--h077b44d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prophasm/0.1.1--h077b44d_5
$ module help quay.io/biocontainers/prophasm/0.1.1--h077b44d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prophasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prophasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prophasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prophasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prophasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prophasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prophasm

```bash
$ singularity exec <container> /usr/local/bin/prophasm
$ podman run --it --rm --entrypoint /usr/local/bin/prophasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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