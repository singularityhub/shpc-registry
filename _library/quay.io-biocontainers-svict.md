---
layout: container
name:  "quay.io/biocontainers/svict"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svict/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svict/container.yaml"
updated_at: "2024-04-18 02:45:09.364199"
latest: "1.0.1--hdcf5f25_5"
container_url: "https://biocontainers.pro/tools/svict"
aliases:
 - "svict"
versions:
 - "1.0.1--hd03093a_3"
 - "1.0.1--hdcf5f25_5"
description: "shpc-registry automated BioContainers addition for svict"
config: {"url": "https://biocontainers.pro/tools/svict", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svict", "latest": {"1.0.1--hdcf5f25_5": "sha256:ec4b0a49aef6f45b90ae3cd5ca37ab81d2394802b5dee0d681d2f40408b1fe54"}, "tags": {"1.0.1--hd03093a_3": "sha256:d8cb74d96578e959454d209906996bcac2c441f98cf674a2cee5a0f5472743e9", "1.0.1--hdcf5f25_5": "sha256:ec4b0a49aef6f45b90ae3cd5ca37ab81d2394802b5dee0d681d2f40408b1fe54"}, "docker": "quay.io/biocontainers/svict", "aliases": {"svict": "/usr/local/bin/svict"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svict.
shpc-registry automated BioContainers addition for svict
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svict
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svict:1.0.1--hdcf5f25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svict/1.0.1--hdcf5f25_5
$ module help quay.io/biocontainers/svict/1.0.1--hdcf5f25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svict-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svict-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svict-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svict-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svict-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svict-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### svict

```bash
$ singularity exec <container> /usr/local/bin/svict
$ podman run --it --rm --entrypoint /usr/local/bin/svict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svict   -v ${PWD} -w ${PWD} <container> -c " $@"
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