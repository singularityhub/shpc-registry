---
layout: container
name:  "quay.io/biocontainers/log4cpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/log4cpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/log4cpp/container.yaml"
updated_at: "2023-03-05 03:34:44.216095"
latest: "1.1--0"
container_url: "https://biocontainers.pro/tools/log4cpp"
aliases:
 - "log4cpp-config"
versions:
 - "1.1--0"
description: "shpc-registry automated BioContainers addition for log4cpp"
config: {"url": "https://biocontainers.pro/tools/log4cpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for log4cpp", "latest": {"1.1--0": "sha256:1d69b44d13138fd226e365a7e82f4876f9cf2cc299075844a02d59473e28d51b"}, "tags": {"1.1--0": "sha256:1d69b44d13138fd226e365a7e82f4876f9cf2cc299075844a02d59473e28d51b"}, "docker": "quay.io/biocontainers/log4cpp", "aliases": {"log4cpp-config": "/usr/local/bin/log4cpp-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/log4cpp.
shpc-registry automated BioContainers addition for log4cpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/log4cpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/log4cpp:1.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/log4cpp/1.1--0
$ module help quay.io/biocontainers/log4cpp/1.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### log4cpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### log4cpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### log4cpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### log4cpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### log4cpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### log4cpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### log4cpp-config

```bash
$ singularity exec <container> /usr/local/bin/log4cpp-config
$ podman run --it --rm --entrypoint /usr/local/bin/log4cpp-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/log4cpp-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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