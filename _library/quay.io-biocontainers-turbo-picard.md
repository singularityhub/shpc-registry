---
layout: container
name:  "quay.io/biocontainers/turbo-picard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/turbo-picard/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/turbo-picard/container.yaml"
updated_at: "2026-10-11 08:33:53.854710"
latest: "0.1.15--hf5b135f_0"
container_url: "https://biocontainers.pro/tools/turbo-picard"
aliases:
 - "turbo-picard"
versions:
 - "0.1.15--hf5b135f_0"
description: "singularity registry hpc automated addition for turbo-picard"
config: {"url": "https://biocontainers.pro/tools/turbo-picard", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for turbo-picard", "latest": {"0.1.15--hf5b135f_0": "sha256:fc384c16379855945f186a6ffb0c06c2f6d1c53039c70965827cacf1970e1bb5"}, "tags": {"0.1.15--hf5b135f_0": "sha256:fc384c16379855945f186a6ffb0c06c2f6d1c53039c70965827cacf1970e1bb5"}, "docker": "quay.io/biocontainers/turbo-picard", "aliases": {"turbo-picard": "/usr/local/bin/turbo-picard"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/turbo-picard.
singularity registry hpc automated addition for turbo-picard
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/turbo-picard
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/turbo-picard:0.1.15--hf5b135f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/turbo-picard/0.1.15--hf5b135f_0
$ module help quay.io/biocontainers/turbo-picard/0.1.15--hf5b135f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### turbo-picard-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### turbo-picard-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### turbo-picard-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### turbo-picard-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### turbo-picard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### turbo-picard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### turbo-picard

```bash
$ singularity exec <container> /usr/local/bin/turbo-picard
$ podman run --it --rm --entrypoint /usr/local/bin/turbo-picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/turbo-picard   -v ${PWD} -w ${PWD} <container> -c " $@"
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