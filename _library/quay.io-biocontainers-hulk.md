---
layout: container
name:  "quay.io/biocontainers/hulk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hulk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hulk/container.yaml"
updated_at: "2025-02-17 03:26:29.908736"
latest: "1.0.0--h375a9b1_0"
container_url: "https://biocontainers.pro/tools/hulk"
aliases:
 - "hulk"
versions:
 - "1.0.0--h375a9b1_0"
description: "shpc-registry automated BioContainers addition for hulk"
config: {"url": "https://biocontainers.pro/tools/hulk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hulk", "latest": {"1.0.0--h375a9b1_0": "sha256:881cdd3cd332e83353baa78fdd11a4d95e5dd0a1da599993552bdf6bfac2fa77"}, "tags": {"1.0.0--h375a9b1_0": "sha256:881cdd3cd332e83353baa78fdd11a4d95e5dd0a1da599993552bdf6bfac2fa77"}, "docker": "quay.io/biocontainers/hulk", "aliases": {"hulk": "/usr/local/bin/hulk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hulk.
shpc-registry automated BioContainers addition for hulk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hulk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hulk:1.0.0--h375a9b1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hulk/1.0.0--h375a9b1_0
$ module help quay.io/biocontainers/hulk/1.0.0--h375a9b1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hulk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hulk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hulk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hulk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hulk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hulk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hulk

```bash
$ singularity exec <container> /usr/local/bin/hulk
$ podman run --it --rm --entrypoint /usr/local/bin/hulk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hulk   -v ${PWD} -w ${PWD} <container> -c " $@"
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