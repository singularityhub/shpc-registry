---
layout: container
name:  "quay.io/biocontainers/ontime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ontime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ontime/container.yaml"
updated_at: "2023-09-11 03:11:35.581030"
latest: "0.1.3--h031d066_2"
container_url: "https://biocontainers.pro/tools/ontime"
aliases:
 - "ontime"
versions:
 - "0.1.3--hec16e2b_0"
 - "0.1.3--h031d066_2"
description: "singularity registry hpc automated addition for ontime"
config: {"url": "https://biocontainers.pro/tools/ontime", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ontime", "latest": {"0.1.3--h031d066_2": "sha256:cb9d2cdeb2b39ed5870ef511fc68d4c526753aaa5a46da9799ac2dcc6dc45d81"}, "tags": {"0.1.3--hec16e2b_0": "sha256:7b24635eae78943080e36ac55dd3966b72cb8ba4f3183be7139def4e5119ca69", "0.1.3--h031d066_2": "sha256:cb9d2cdeb2b39ed5870ef511fc68d4c526753aaa5a46da9799ac2dcc6dc45d81"}, "docker": "quay.io/biocontainers/ontime", "aliases": {"ontime": "/usr/local/bin/ontime"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ontime.
singularity registry hpc automated addition for ontime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ontime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ontime:0.1.3--h031d066_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ontime/0.1.3--h031d066_2
$ module help quay.io/biocontainers/ontime/0.1.3--h031d066_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ontime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ontime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ontime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ontime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ontime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ontime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ontime

```bash
$ singularity exec <container> /usr/local/bin/ontime
$ podman run --it --rm --entrypoint /usr/local/bin/ontime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ontime   -v ${PWD} -w ${PWD} <container> -c " $@"
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