---
layout: container
name:  "quay.io/biocontainers/dehomopolymerate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dehomopolymerate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dehomopolymerate/container.yaml"
updated_at: "2024-01-01 02:48:15.826646"
latest: "0.4.0--he4a0461_4"
container_url: "https://biocontainers.pro/tools/dehomopolymerate"
aliases:
 - "dehomopolymerate"
versions:
 - "0.4.0--h7132678_2"
 - "0.4.0--he4a0461_4"
description: "shpc-registry automated BioContainers addition for dehomopolymerate"
config: {"url": "https://biocontainers.pro/tools/dehomopolymerate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dehomopolymerate", "latest": {"0.4.0--he4a0461_4": "sha256:3836f72b07c52ab37d178164bb093736490225a7755e733a8a035721daeb7f83"}, "tags": {"0.4.0--h7132678_2": "sha256:d2a18c0fb9f6891121952ac40ff09eb8f098b18fb79a51264911467442c8731a", "0.4.0--he4a0461_4": "sha256:3836f72b07c52ab37d178164bb093736490225a7755e733a8a035721daeb7f83"}, "docker": "quay.io/biocontainers/dehomopolymerate", "aliases": {"dehomopolymerate": "/usr/local/bin/dehomopolymerate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dehomopolymerate.
shpc-registry automated BioContainers addition for dehomopolymerate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dehomopolymerate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dehomopolymerate:0.4.0--he4a0461_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dehomopolymerate/0.4.0--he4a0461_4
$ module help quay.io/biocontainers/dehomopolymerate/0.4.0--he4a0461_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dehomopolymerate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dehomopolymerate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dehomopolymerate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dehomopolymerate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dehomopolymerate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dehomopolymerate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dehomopolymerate

```bash
$ singularity exec <container> /usr/local/bin/dehomopolymerate
$ podman run --it --rm --entrypoint /usr/local/bin/dehomopolymerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dehomopolymerate   -v ${PWD} -w ${PWD} <container> -c " $@"
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