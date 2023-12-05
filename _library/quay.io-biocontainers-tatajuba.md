---
layout: container
name:  "quay.io/biocontainers/tatajuba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tatajuba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tatajuba/container.yaml"
updated_at: "2023-12-05 02:38:38.828460"
latest: "1.0.4--he4a0461_3"
container_url: "https://biocontainers.pro/tools/tatajuba"
aliases:
 - "tatajuba"
versions:
 - "1.0.4--h7132678_1"
 - "1.0.4--he4a0461_3"
description: "shpc-registry automated BioContainers addition for tatajuba"
config: {"url": "https://biocontainers.pro/tools/tatajuba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tatajuba", "latest": {"1.0.4--he4a0461_3": "sha256:ab507a60d16cd67ea7d72814d04319682ce0b7502ed3a9caa2b4f1d0347fc7c5"}, "tags": {"1.0.4--h7132678_1": "sha256:94c0e10fe9d50cfcbc5b910d42cd19c5ff398a6b9b6bcd2e4a612f4e7c2e3ee7", "1.0.4--he4a0461_3": "sha256:ab507a60d16cd67ea7d72814d04319682ce0b7502ed3a9caa2b4f1d0347fc7c5"}, "docker": "quay.io/biocontainers/tatajuba", "aliases": {"tatajuba": "/usr/local/bin/tatajuba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tatajuba.
shpc-registry automated BioContainers addition for tatajuba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tatajuba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tatajuba:1.0.4--he4a0461_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tatajuba/1.0.4--he4a0461_3
$ module help quay.io/biocontainers/tatajuba/1.0.4--he4a0461_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tatajuba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tatajuba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tatajuba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tatajuba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tatajuba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tatajuba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tatajuba

```bash
$ singularity exec <container> /usr/local/bin/tatajuba
$ podman run --it --rm --entrypoint /usr/local/bin/tatajuba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tatajuba   -v ${PWD} -w ${PWD} <container> -c " $@"
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