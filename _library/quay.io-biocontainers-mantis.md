---
layout: container
name:  "quay.io/biocontainers/mantis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mantis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mantis/container.yaml"
updated_at: "2023-10-23 02:50:14.275964"
latest: "0.2--h2e03b76_3"
container_url: "https://biocontainers.pro/tools/mantis"
aliases:
 - "mantis"
versions:
 - "0.2--h2e03b76_3"
description: "shpc-registry automated BioContainers addition for mantis"
config: {"url": "https://biocontainers.pro/tools/mantis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mantis", "latest": {"0.2--h2e03b76_3": "sha256:9c9911ccc4264f0b91d763d588453b3ad078169592df0e1bf3e30b2e656a2a51"}, "tags": {"0.2--h2e03b76_3": "sha256:9c9911ccc4264f0b91d763d588453b3ad078169592df0e1bf3e30b2e656a2a51"}, "docker": "quay.io/biocontainers/mantis", "aliases": {"mantis": "/usr/local/bin/mantis"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mantis.
shpc-registry automated BioContainers addition for mantis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mantis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mantis:0.2--h2e03b76_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mantis/0.2--h2e03b76_3
$ module help quay.io/biocontainers/mantis/0.2--h2e03b76_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mantis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mantis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mantis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mantis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mantis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mantis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mantis

```bash
$ singularity exec <container> /usr/local/bin/mantis
$ podman run --it --rm --entrypoint /usr/local/bin/mantis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mantis   -v ${PWD} -w ${PWD} <container> -c " $@"
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