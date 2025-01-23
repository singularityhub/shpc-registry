---
layout: container
name:  "quay.io/biocontainers/secedo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/secedo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/secedo/container.yaml"
updated_at: "2025-01-23 02:59:53.113851"
latest: "1.0.7--h2ac389b_2"
container_url: "https://biocontainers.pro/tools/secedo"
aliases:
 - "pileup"
 - "secedo"
versions:
 - "1.0.7--h2ac389b_1"
 - "1.0.7--h2ac389b_2"
description: "singularity registry hpc automated addition for secedo"
config: {"url": "https://biocontainers.pro/tools/secedo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for secedo", "latest": {"1.0.7--h2ac389b_2": "sha256:e3cb12540afbd91887f8f1f7da2d726ae30b003b391d929838f85dcc5947a975"}, "tags": {"1.0.7--h2ac389b_1": "sha256:e0d9ae2b4f01956d5e010976a767722a64bd9c6519cc96f07de10a36d69e21ab", "1.0.7--h2ac389b_2": "sha256:e3cb12540afbd91887f8f1f7da2d726ae30b003b391d929838f85dcc5947a975"}, "docker": "quay.io/biocontainers/secedo", "aliases": {"pileup": "/usr/local/bin/pileup", "secedo": "/usr/local/bin/secedo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/secedo.
singularity registry hpc automated addition for secedo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/secedo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/secedo:1.0.7--h2ac389b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/secedo/1.0.7--h2ac389b_2
$ module help quay.io/biocontainers/secedo/1.0.7--h2ac389b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### secedo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### secedo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### secedo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### secedo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### secedo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### secedo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pileup

```bash
$ singularity exec <container> /usr/local/bin/pileup
$ podman run --it --rm --entrypoint /usr/local/bin/pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### secedo

```bash
$ singularity exec <container> /usr/local/bin/secedo
$ podman run --it --rm --entrypoint /usr/local/bin/secedo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/secedo   -v ${PWD} -w ${PWD} <container> -c " $@"
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