---
layout: container
name:  "quay.io/biocontainers/tntblast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tntblast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tntblast/container.yaml"
updated_at: "2024-12-14 03:29:28.859447"
latest: "2.66--h6b557da_0"
container_url: "https://biocontainers.pro/tools/tntblast"
aliases:
 - "tntblast"
versions:
 - "2.61--hdcf5f25_0"
 - "2.66--h6b557da_0"
description: "singularity registry hpc automated addition for tntblast"
config: {"url": "https://biocontainers.pro/tools/tntblast", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tntblast", "latest": {"2.66--h6b557da_0": "sha256:991f21e5c10867b01b8d8d9499c858c183e6068f71f75b3d73d62c9ac895d4ed"}, "tags": {"2.61--hdcf5f25_0": "sha256:46ef993bbd28d9e45bd7846babee3393256145aebdfe27ff321d074c1a70bd6c", "2.66--h6b557da_0": "sha256:991f21e5c10867b01b8d8d9499c858c183e6068f71f75b3d73d62c9ac895d4ed"}, "docker": "quay.io/biocontainers/tntblast", "aliases": {"tntblast": "/usr/local/bin/tntblast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tntblast.
singularity registry hpc automated addition for tntblast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tntblast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tntblast:2.66--h6b557da_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tntblast/2.66--h6b557da_0
$ module help quay.io/biocontainers/tntblast/2.66--h6b557da_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tntblast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tntblast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tntblast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tntblast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tntblast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tntblast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tntblast

```bash
$ singularity exec <container> /usr/local/bin/tntblast
$ podman run --it --rm --entrypoint /usr/local/bin/tntblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tntblast   -v ${PWD} -w ${PWD} <container> -c " $@"
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