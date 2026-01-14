---
layout: container
name:  "quay.io/biocontainers/meta-apo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/meta-apo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/meta-apo/container.yaml"
updated_at: "2026-01-14 04:23:28.417213"
latest: "1.1--h9948957_7"
container_url: "https://biocontainers.pro/tools/meta-apo"
aliases:
 - "meta-apo-calibrate"
 - "meta-apo-train"
versions:
 - "1.1--h9f5acd7_4"
 - "1.1--h4ac6f70_6"
 - "1.1--h9948957_7"
description: "shpc-registry automated BioContainers addition for meta-apo"
config: {"url": "https://biocontainers.pro/tools/meta-apo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for meta-apo", "latest": {"1.1--h9948957_7": "sha256:bc21df286542c3e9bf9978a1e7901177b73a21741b695b0934be2a8e92b4ff1a"}, "tags": {"1.1--h9f5acd7_4": "sha256:d6bd635509c102b5f0bef9f957111af3d513644900f51c024a2ac46601b024c1", "1.1--h4ac6f70_6": "sha256:380fc9536a2024a02ec9f70e002b69be13198bbbc8af6932e9ae0e6094faedba", "1.1--h9948957_7": "sha256:bc21df286542c3e9bf9978a1e7901177b73a21741b695b0934be2a8e92b4ff1a"}, "docker": "quay.io/biocontainers/meta-apo", "aliases": {"meta-apo-calibrate": "/usr/local/bin/meta-apo-calibrate", "meta-apo-train": "/usr/local/bin/meta-apo-train"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/meta-apo.
shpc-registry automated BioContainers addition for meta-apo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/meta-apo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/meta-apo:1.1--h9948957_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/meta-apo/1.1--h9948957_7
$ module help quay.io/biocontainers/meta-apo/1.1--h9948957_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### meta-apo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### meta-apo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### meta-apo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### meta-apo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### meta-apo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### meta-apo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### meta-apo-calibrate

```bash
$ singularity exec <container> /usr/local/bin/meta-apo-calibrate
$ podman run --it --rm --entrypoint /usr/local/bin/meta-apo-calibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meta-apo-calibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meta-apo-train

```bash
$ singularity exec <container> /usr/local/bin/meta-apo-train
$ podman run --it --rm --entrypoint /usr/local/bin/meta-apo-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meta-apo-train   -v ${PWD} -w ${PWD} <container> -c " $@"
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