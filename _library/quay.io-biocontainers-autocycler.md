---
layout: container
name:  "quay.io/biocontainers/autocycler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autocycler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autocycler/container.yaml"
updated_at: "2025-10-05 03:31:13.408354"
latest: "0.5.2--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/autocycler"
aliases:
 - "autocycler"
versions:
 - "0.2.1--h3ab6199_0"
 - "0.4.0--h3ab6199_0"
 - "0.3.0--h3ab6199_0"
 - "0.5.0--h3ab6199_0"
 - "0.5.2--h3ab6199_0"
description: "singularity registry hpc automated addition for autocycler"
config: {"url": "https://biocontainers.pro/tools/autocycler", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for autocycler", "latest": {"0.5.2--h3ab6199_0": "sha256:58e79c1610e1208b43723c894506bcc30d5ba7e53ae2e5416878b7a39041405c"}, "tags": {"0.2.1--h3ab6199_0": "sha256:ffc8cefd8ba4bced4b70d2f0a9425ef250f464b128cac5b637d0c155c8b6f729", "0.4.0--h3ab6199_0": "sha256:fa6a1c0cfcceefd1e387828e5a384f863a429a062041118a06e4e082672a9c03", "0.3.0--h3ab6199_0": "sha256:229a995a856ad394f4b37c3fd3665e43f94414419c107ccf3ea3cbf44eb6b5e9", "0.5.0--h3ab6199_0": "sha256:ae29391c61b493ed26d4bfd867a7039b2da980444f470ef46e7f5477b037ba6e", "0.5.2--h3ab6199_0": "sha256:58e79c1610e1208b43723c894506bcc30d5ba7e53ae2e5416878b7a39041405c"}, "docker": "quay.io/biocontainers/autocycler", "aliases": {"autocycler": "/usr/local/bin/autocycler"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autocycler.
singularity registry hpc automated addition for autocycler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autocycler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autocycler:0.5.2--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autocycler/0.5.2--h3ab6199_0
$ module help quay.io/biocontainers/autocycler/0.5.2--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autocycler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autocycler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autocycler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autocycler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autocycler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autocycler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autocycler

```bash
$ singularity exec <container> /usr/local/bin/autocycler
$ podman run --it --rm --entrypoint /usr/local/bin/autocycler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autocycler   -v ${PWD} -w ${PWD} <container> -c " $@"
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