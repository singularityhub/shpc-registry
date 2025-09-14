---
layout: container
name:  "quay.io/biocontainers/uniqsketch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uniqsketch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/uniqsketch/container.yaml"
updated_at: "2025-09-14 03:14:45.894373"
latest: "1.1.0--h077b44d_0"
container_url: "https://biocontainers.pro/tools/uniqsketch"
aliases:
 - "comparesketch"
 - "querysketch"
 - "uniqsketch"
versions:
 - "1.1.0--h077b44d_0"
description: "singularity registry hpc automated addition for uniqsketch"
config: {"url": "https://biocontainers.pro/tools/uniqsketch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for uniqsketch", "latest": {"1.1.0--h077b44d_0": "sha256:599f747947a95ec1dfa9e389e8eab616c17fe47deabe1c0770ba9fa46ec8cecc"}, "tags": {"1.1.0--h077b44d_0": "sha256:599f747947a95ec1dfa9e389e8eab616c17fe47deabe1c0770ba9fa46ec8cecc"}, "docker": "quay.io/biocontainers/uniqsketch", "aliases": {"comparesketch": "/usr/local/bin/comparesketch", "querysketch": "/usr/local/bin/querysketch", "uniqsketch": "/usr/local/bin/uniqsketch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/uniqsketch.
singularity registry hpc automated addition for uniqsketch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uniqsketch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uniqsketch:1.1.0--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uniqsketch/1.1.0--h077b44d_0
$ module help quay.io/biocontainers/uniqsketch/1.1.0--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uniqsketch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uniqsketch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uniqsketch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uniqsketch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uniqsketch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uniqsketch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### comparesketch

```bash
$ singularity exec <container> /usr/local/bin/comparesketch
$ podman run --it --rm --entrypoint /usr/local/bin/comparesketch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparesketch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### querysketch

```bash
$ singularity exec <container> /usr/local/bin/querysketch
$ podman run --it --rm --entrypoint /usr/local/bin/querysketch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/querysketch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniqsketch

```bash
$ singularity exec <container> /usr/local/bin/uniqsketch
$ podman run --it --rm --entrypoint /usr/local/bin/uniqsketch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniqsketch   -v ${PWD} -w ${PWD} <container> -c " $@"
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