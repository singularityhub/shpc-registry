---
layout: container
name:  "quay.io/biocontainers/riblast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riblast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riblast/container.yaml"
updated_at: "2023-10-15 03:17:51.929105"
latest: "1.2.0--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/riblast"
aliases:
 - "RIblast"
versions:
 - "1.2.0--hdcf5f25_0"
description: "singularity registry hpc automated addition for riblast"
config: {"url": "https://biocontainers.pro/tools/riblast", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for riblast", "latest": {"1.2.0--hdcf5f25_0": "sha256:a67330e55d7994ca25e3f4cca1749d41fbf064c2d6778fa6c32213022fd365d9"}, "tags": {"1.2.0--hdcf5f25_0": "sha256:a67330e55d7994ca25e3f4cca1749d41fbf064c2d6778fa6c32213022fd365d9"}, "docker": "quay.io/biocontainers/riblast", "aliases": {"RIblast": "/usr/local/bin/RIblast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riblast.
singularity registry hpc automated addition for riblast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riblast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riblast:1.2.0--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riblast/1.2.0--hdcf5f25_0
$ module help quay.io/biocontainers/riblast/1.2.0--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riblast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riblast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riblast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riblast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riblast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riblast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RIblast

```bash
$ singularity exec <container> /usr/local/bin/RIblast
$ podman run --it --rm --entrypoint /usr/local/bin/RIblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RIblast   -v ${PWD} -w ${PWD} <container> -c " $@"
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