---
layout: container
name:  "quay.io/biocontainers/yasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yasm/container.yaml"
updated_at: "2024-06-25 02:36:44.293547"
latest: "1.3.0--0"
container_url: "https://biocontainers.pro/tools/yasm"
aliases:
 - "vsyasm"
 - "yasm"
 - "ytasm"
versions:
 - "1.3.0--0"
description: "shpc-registry automated BioContainers addition for yasm"
config: {"url": "https://biocontainers.pro/tools/yasm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yasm", "latest": {"1.3.0--0": "sha256:0900474f5680e9fcdedae68bf3cd818172b046c86ce854bf8ad3bd8bd6e312dc"}, "tags": {"1.3.0--0": "sha256:0900474f5680e9fcdedae68bf3cd818172b046c86ce854bf8ad3bd8bd6e312dc"}, "docker": "quay.io/biocontainers/yasm", "aliases": {"vsyasm": "/usr/local/bin/vsyasm", "yasm": "/usr/local/bin/yasm", "ytasm": "/usr/local/bin/ytasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yasm.
shpc-registry automated BioContainers addition for yasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yasm:1.3.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yasm/1.3.0--0
$ module help quay.io/biocontainers/yasm/1.3.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vsyasm

```bash
$ singularity exec <container> /usr/local/bin/vsyasm
$ podman run --it --rm --entrypoint /usr/local/bin/vsyasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsyasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yasm

```bash
$ singularity exec <container> /usr/local/bin/yasm
$ podman run --it --rm --entrypoint /usr/local/bin/yasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ytasm

```bash
$ singularity exec <container> /usr/local/bin/ytasm
$ podman run --it --rm --entrypoint /usr/local/bin/ytasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ytasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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