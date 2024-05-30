---
layout: container
name:  "quay.io/biocontainers/crux-toolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crux-toolkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crux-toolkit/container.yaml"
updated_at: "2024-05-30 02:56:04.954734"
latest: "4.1--hdbdd923_2"
container_url: "https://biocontainers.pro/tools/crux-toolkit"
aliases:
 - "crux"
versions:
 - "4.1--h87f3376_0"
 - "4.1--hdbdd923_2"
description: "shpc-registry automated BioContainers addition for crux-toolkit"
config: {"url": "https://biocontainers.pro/tools/crux-toolkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crux-toolkit", "latest": {"4.1--hdbdd923_2": "sha256:62177882be4d11c455e27f0a847b29ad25f4c246ee5a563f2e8019032f73dd20"}, "tags": {"4.1--h87f3376_0": "sha256:0438c28b84c662a60bb8b11f057aefd2045e565928fddb86e639610072c266b0", "4.1--hdbdd923_2": "sha256:62177882be4d11c455e27f0a847b29ad25f4c246ee5a563f2e8019032f73dd20"}, "docker": "quay.io/biocontainers/crux-toolkit", "aliases": {"crux": "/usr/local/bin/crux"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crux-toolkit.
shpc-registry automated BioContainers addition for crux-toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crux-toolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crux-toolkit:4.1--hdbdd923_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crux-toolkit/4.1--hdbdd923_2
$ module help quay.io/biocontainers/crux-toolkit/4.1--hdbdd923_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crux-toolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crux-toolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crux-toolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crux-toolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crux-toolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crux-toolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crux

```bash
$ singularity exec <container> /usr/local/bin/crux
$ podman run --it --rm --entrypoint /usr/local/bin/crux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crux   -v ${PWD} -w ${PWD} <container> -c " $@"
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