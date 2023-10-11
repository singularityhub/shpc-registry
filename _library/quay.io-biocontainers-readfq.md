---
layout: container
name:  "quay.io/biocontainers/readfq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/readfq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/readfq/container.yaml"
updated_at: "2023-10-11 02:27:39.702128"
latest: "2015.08.30--he4a0461_5"
container_url: "https://biocontainers.pro/tools/readfq"
aliases:
 - "readfq"
versions:
 - "2015.08.30--h7132678_3"
 - "2015.08.30--he4a0461_5"
description: "shpc-registry automated BioContainers addition for readfq"
config: {"url": "https://biocontainers.pro/tools/readfq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for readfq", "latest": {"2015.08.30--he4a0461_5": "sha256:8548418415a37572aa1d983f4726063afffc2c5d4ecfd8cd635a75ec00c4698f"}, "tags": {"2015.08.30--h7132678_3": "sha256:cdc93f495618e9544da2ccbe82c5440c1ac29759a2443bd90602408b511be744", "2015.08.30--he4a0461_5": "sha256:8548418415a37572aa1d983f4726063afffc2c5d4ecfd8cd635a75ec00c4698f"}, "docker": "quay.io/biocontainers/readfq", "aliases": {"readfq": "/usr/local/bin/readfq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/readfq.
shpc-registry automated BioContainers addition for readfq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/readfq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/readfq:2015.08.30--he4a0461_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/readfq/2015.08.30--he4a0461_5
$ module help quay.io/biocontainers/readfq/2015.08.30--he4a0461_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### readfq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### readfq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### readfq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### readfq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### readfq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### readfq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### readfq

```bash
$ singularity exec <container> /usr/local/bin/readfq
$ podman run --it --rm --entrypoint /usr/local/bin/readfq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readfq   -v ${PWD} -w ${PWD} <container> -c " $@"
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