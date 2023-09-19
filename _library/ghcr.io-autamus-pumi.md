---
layout: container
name:  "ghcr.io/autamus/pumi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/pumi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/pumi/container.yaml"
updated_at: "2023-09-19 02:23:26.037829"
latest: "2.2.6"
container_url: "https://github.com/orgs/autamus/packages/container/package/pumi"
aliases:
 - "print_pumipic_partition"
versions:
 - "2.2.5"
 - "2.2.6"
 - "latest"
 - "2.2.7"
description: "SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI)."
config: {"docker": "ghcr.io/autamus/pumi", "url": "https://github.com/orgs/autamus/packages/container/package/pumi", "maintainer": "@vsoch", "description": "SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI).", "latest": {"2.2.6": "sha256:1ad880ab6bedad474935938f2e0c1d79c4970e3deaeaeb44687c66c5158ffd00"}, "tags": {"2.2.5": "sha256:b27b85dee50631bbc40977a23a00830acf0c236bb0966c2d11f9b62a8fbcff6f", "2.2.6": "sha256:1ad880ab6bedad474935938f2e0c1d79c4970e3deaeaeb44687c66c5158ffd00", "latest": "sha256:35238311728bf14119a732bbeb4bbb71df5d34d7225a8209915b9b321ceca634", "2.2.7": "sha256:35238311728bf14119a732bbeb4bbb71df5d34d7225a8209915b9b321ceca634"}, "aliases": {"print_pumipic_partition": "/opt/view/bin/print_pumipic_partition"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/pumi.
SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI).
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/pumi
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/pumi:2.2.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/pumi/2.2.6
$ module help ghcr.io/autamus/pumi/2.2.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pumi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pumi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pumi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pumi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pumi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pumi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### print_pumipic_partition

```bash
$ singularity exec <container> /opt/view/bin/print_pumipic_partition
$ podman run --it --rm --entrypoint /opt/view/bin/print_pumipic_partition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/print_pumipic_partition   -v ${PWD} -w ${PWD} <container> -c " $@"
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