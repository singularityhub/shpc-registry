---
layout: container
name:  "quay.io/biocontainers/kseqpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kseqpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kseqpp/container.yaml"
updated_at: "2023-12-27 02:33:41.280986"
latest: "1.1.1--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/kseqpp"

versions:
 - "1.0.0--hd03093a_0"
 - "1.0.0--hd03093a_1"
 - "1.1.1--hdcf5f25_1"
 - "1.0.0--hdcf5f25_3"
description: "singularity registry hpc automated addition for kseqpp"
config: {"url": "https://biocontainers.pro/tools/kseqpp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kseqpp", "latest": {"1.1.1--hdcf5f25_1": "sha256:694d540d933c4f0cdbb1dbb04c89f3706873465a194ec775ddd33995d035fb69"}, "tags": {"1.0.0--hd03093a_0": "sha256:a7262463433b5a59e11a31e5c2afc7a43bedb2df6e7a00c0fc645784add96997", "1.0.0--hd03093a_1": "sha256:e9ad86acad1e2278502f125f90808ec44ab482d05555674af858f382ddba56b7", "1.1.1--hdcf5f25_1": "sha256:694d540d933c4f0cdbb1dbb04c89f3706873465a194ec775ddd33995d035fb69", "1.0.0--hdcf5f25_3": "sha256:178431d40df4c588472fdedb0c17468ceca4150a69914f3cc65d3795b63087b2"}, "docker": "quay.io/biocontainers/kseqpp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/kseqpp.
singularity registry hpc automated addition for kseqpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kseqpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kseqpp:1.1.1--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kseqpp/1.1.1--hdcf5f25_1
$ module help quay.io/biocontainers/kseqpp/1.1.1--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kseqpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kseqpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kseqpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kseqpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kseqpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kseqpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### kseqpp

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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