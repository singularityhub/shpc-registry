---
layout: container
name:  "quay.io/biocontainers/raxtax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/raxtax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/raxtax/container.yaml"
updated_at: "2026-03-21 04:25:35.728334"
latest: "1.5.0--h4349ce8_1"
container_url: "https://biocontainers.pro/tools/raxtax"
aliases:
 - "raxtax"
versions:
 - "1.5.0--h4349ce8_1"
description: "singularity registry hpc automated addition for raxtax"
config: {"url": "https://biocontainers.pro/tools/raxtax", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for raxtax", "latest": {"1.5.0--h4349ce8_1": "sha256:92ef91d706f682e418259bad51e00b13c6c7f87eee40d19e9003bd7611e09906"}, "tags": {"1.5.0--h4349ce8_1": "sha256:92ef91d706f682e418259bad51e00b13c6c7f87eee40d19e9003bd7611e09906"}, "docker": "quay.io/biocontainers/raxtax", "aliases": {"raxtax": "/usr/local/bin/raxtax"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/raxtax.
singularity registry hpc automated addition for raxtax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/raxtax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/raxtax:1.5.0--h4349ce8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/raxtax/1.5.0--h4349ce8_1
$ module help quay.io/biocontainers/raxtax/1.5.0--h4349ce8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raxtax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raxtax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raxtax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raxtax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raxtax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raxtax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### raxtax

```bash
$ singularity exec <container> /usr/local/bin/raxtax
$ podman run --it --rm --entrypoint /usr/local/bin/raxtax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxtax   -v ${PWD} -w ${PWD} <container> -c " $@"
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