---
layout: container
name:  "quay.io/biocontainers/fastvep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastvep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastvep/container.yaml"
updated_at: "2026-11-07 09:16:37.985030"
latest: "0.4.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/fastvep"
aliases:
 - "fastvep"
 - "fastvep-web"
versions:
 - "0.4.0--hfa8f182_0"
description: "singularity registry hpc automated addition for fastvep"
config: {"url": "https://biocontainers.pro/tools/fastvep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastvep", "latest": {"0.4.0--hfa8f182_0": "sha256:d311a0af937431da7bc3aab3c2068c888fc73b43832b2b3cfc44df0b82a9be5a"}, "tags": {"0.4.0--hfa8f182_0": "sha256:d311a0af937431da7bc3aab3c2068c888fc73b43832b2b3cfc44df0b82a9be5a"}, "docker": "quay.io/biocontainers/fastvep", "aliases": {"fastvep": "/usr/local/bin/fastvep", "fastvep-web": "/usr/local/bin/fastvep-web"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastvep.
singularity registry hpc automated addition for fastvep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastvep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastvep:0.4.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastvep/0.4.0--hfa8f182_0
$ module help quay.io/biocontainers/fastvep/0.4.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastvep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastvep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastvep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastvep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastvep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastvep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastvep

```bash
$ singularity exec <container> /usr/local/bin/fastvep
$ podman run --it --rm --entrypoint /usr/local/bin/fastvep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastvep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastvep-web

```bash
$ singularity exec <container> /usr/local/bin/fastvep-web
$ podman run --it --rm --entrypoint /usr/local/bin/fastvep-web   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastvep-web   -v ${PWD} -w ${PWD} <container> -c " $@"
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