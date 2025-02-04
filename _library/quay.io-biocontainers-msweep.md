---
layout: container
name:  "quay.io/biocontainers/msweep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msweep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msweep/container.yaml"
updated_at: "2025-02-04 03:03:59.857448"
latest: "2.2.1--h503566f_1"
container_url: "https://biocontainers.pro/tools/msweep"
aliases:
 - "mSWEEP"
versions:
 - "1.6.3--h87f3376_0"
 - "1.6.3--hdbdd923_2"
 - "2.0.0--hdbdd923_0"
 - "2.1.0--hdbdd923_0"
 - "2.1.2--hdbdd923_0"
 - "2.2.0--hdbdd923_0"
 - "2.2.1--hdbdd923_0"
 - "2.2.1--h503566f_1"
description: "singularity registry hpc automated addition for msweep"
config: {"url": "https://biocontainers.pro/tools/msweep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for msweep", "latest": {"2.2.1--h503566f_1": "sha256:603b1a80909dbca706f5fe4f4f6cb6f898386dd6b3ff570abbaf3192e364257c"}, "tags": {"1.6.3--h87f3376_0": "sha256:1f64851d3d1b9baba6036816e1770cdb4e61be4c0c960a0c52ba7d2b3ebc14db", "1.6.3--hdbdd923_2": "sha256:6710c75038dee8af6637700f216b0048eb9e9cb3593d1ce82fdc0f23d80eed14", "2.0.0--hdbdd923_0": "sha256:4b683fa7c4ac27c87384a87bd3d5cadad81e6947247cbd85436e964f21b3ab15", "2.1.0--hdbdd923_0": "sha256:6f74123aec6fce549d3f90b743da42bf10b9f46be367e1f234708c96d3d8a7fc", "2.1.2--hdbdd923_0": "sha256:bf10298f572b9e82495581d3052ad2e83cc84eef51c6a2e70a537510cffe0944", "2.2.0--hdbdd923_0": "sha256:6f8f6be820c6c91e725b141d4fe60e18b18c70f94fc6fac83e77e287b91e54f0", "2.2.1--hdbdd923_0": "sha256:2e50aa3cca44cadfde16df4422ca8eda264ba4c8cde62d3ad604bbe39db4a520", "2.2.1--h503566f_1": "sha256:603b1a80909dbca706f5fe4f4f6cb6f898386dd6b3ff570abbaf3192e364257c"}, "docker": "quay.io/biocontainers/msweep", "aliases": {"mSWEEP": "/usr/local/bin/mSWEEP"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msweep.
singularity registry hpc automated addition for msweep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msweep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msweep:2.2.1--h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msweep/2.2.1--h503566f_1
$ module help quay.io/biocontainers/msweep/2.2.1--h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msweep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msweep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msweep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msweep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msweep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msweep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mSWEEP

```bash
$ singularity exec <container> /usr/local/bin/mSWEEP
$ podman run --it --rm --entrypoint /usr/local/bin/mSWEEP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mSWEEP   -v ${PWD} -w ${PWD} <container> -c " $@"
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