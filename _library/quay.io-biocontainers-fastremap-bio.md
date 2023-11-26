---
layout: container
name:  "quay.io/biocontainers/fastremap-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastremap-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastremap-bio/container.yaml"
updated_at: "2023-11-26 02:39:07.065372"
latest: "1.0.0--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/fastremap-bio"
aliases:
 - "FastRemap"
versions:
 - "1.0.0--hd03093a_0"
 - "1.0.0--hdcf5f25_1"
description: "singularity registry hpc automated addition for fastremap-bio"
config: {"url": "https://biocontainers.pro/tools/fastremap-bio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastremap-bio", "latest": {"1.0.0--hdcf5f25_1": "sha256:52f5ee29f0757576a8ed0265ba0a6f6863f99fa93b0f6c1efcbdab2ff3e67d0d"}, "tags": {"1.0.0--hd03093a_0": "sha256:f25adec9f93cacaeda45bd1a252d9d2fbfbd613d12842f79b4abda77de483ab9", "1.0.0--hdcf5f25_1": "sha256:52f5ee29f0757576a8ed0265ba0a6f6863f99fa93b0f6c1efcbdab2ff3e67d0d"}, "docker": "quay.io/biocontainers/fastremap-bio", "aliases": {"FastRemap": "/usr/local/bin/FastRemap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastremap-bio.
singularity registry hpc automated addition for fastremap-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastremap-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastremap-bio:1.0.0--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastremap-bio/1.0.0--hdcf5f25_1
$ module help quay.io/biocontainers/fastremap-bio/1.0.0--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastremap-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastremap-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastremap-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastremap-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastremap-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastremap-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FastRemap

```bash
$ singularity exec <container> /usr/local/bin/FastRemap
$ podman run --it --rm --entrypoint /usr/local/bin/FastRemap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastRemap   -v ${PWD} -w ${PWD} <container> -c " $@"
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