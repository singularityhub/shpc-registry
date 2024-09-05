---
layout: container
name:  "quay.io/biocontainers/seqstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqstats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqstats/container.yaml"
updated_at: "2024-09-05 02:47:44.571212"
latest: "1.0.0--he4a0461_4"
container_url: "https://biocontainers.pro/tools/seqstats"
aliases:
 - "seqstats"
versions:
 - "1.0.0--h7132678_2"
 - "1.0.0--he4a0461_4"
description: "shpc-registry automated BioContainers addition for seqstats"
config: {"url": "https://biocontainers.pro/tools/seqstats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqstats", "latest": {"1.0.0--he4a0461_4": "sha256:419a12b037e63e5b94a9a4c31602543c80bc21cf69351b69c3a93b57bb520208"}, "tags": {"1.0.0--h7132678_2": "sha256:13154910066a24216e77d4a220bd67357903bf2d8ad164c177f5854f835cf9fe", "1.0.0--he4a0461_4": "sha256:419a12b037e63e5b94a9a4c31602543c80bc21cf69351b69c3a93b57bb520208"}, "docker": "quay.io/biocontainers/seqstats", "aliases": {"seqstats": "/usr/local/bin/seqstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqstats.
shpc-registry automated BioContainers addition for seqstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqstats:1.0.0--he4a0461_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqstats/1.0.0--he4a0461_4
$ module help quay.io/biocontainers/seqstats/1.0.0--he4a0461_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqstats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqstats

```bash
$ singularity exec <container> /usr/local/bin/seqstats
$ podman run --it --rm --entrypoint /usr/local/bin/seqstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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