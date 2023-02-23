---
layout: container
name:  "quay.io/biocontainers/zmwfilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zmwfilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/zmwfilter/container.yaml"
updated_at: "2023-02-23 03:28:46.543216"
latest: "1.0.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/zmwfilter"
aliases:
 - "zmwfilter"
versions:
 - "1.0.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for zmwfilter"
config: {"url": "https://biocontainers.pro/tools/zmwfilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zmwfilter", "latest": {"1.0.0--h9ee0642_1": "sha256:3356d3b21e4fc7e41d4a92feb570900a9013c5e3c717e1fc35a480db5f95926c"}, "tags": {"1.0.0--h9ee0642_1": "sha256:3356d3b21e4fc7e41d4a92feb570900a9013c5e3c717e1fc35a480db5f95926c"}, "docker": "quay.io/biocontainers/zmwfilter", "aliases": {"zmwfilter": "/usr/local/bin/zmwfilter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zmwfilter.
shpc-registry automated BioContainers addition for zmwfilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zmwfilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zmwfilter:1.0.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zmwfilter/1.0.0--h9ee0642_1
$ module help quay.io/biocontainers/zmwfilter/1.0.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zmwfilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zmwfilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zmwfilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zmwfilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zmwfilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zmwfilter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### zmwfilter

```bash
$ singularity exec <container> /usr/local/bin/zmwfilter
$ podman run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
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