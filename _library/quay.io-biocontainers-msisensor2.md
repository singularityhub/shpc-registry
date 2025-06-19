---
layout: container
name:  "quay.io/biocontainers/msisensor2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msisensor2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msisensor2/container.yaml"
updated_at: "2025-06-19 04:09:08.276760"
latest: "0.1--h077b44d_3"
container_url: "https://biocontainers.pro/tools/msisensor2"
aliases:
 - "msisensor2"
versions:
 - "0.1--hd03093a_0"
 - "0.1--hdcf5f25_2"
 - "0.1--h077b44d_3"
description: "shpc-registry automated BioContainers addition for msisensor2"
config: {"url": "https://biocontainers.pro/tools/msisensor2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msisensor2", "latest": {"0.1--h077b44d_3": "sha256:a56c7424e80d5054155f9a2671f80c82a53abb951f8b66d49f00447132532b87"}, "tags": {"0.1--hd03093a_0": "sha256:b01f4a2f7938d42047bdb94a4f2c97dbf26bd53464ad1b82f811f037e3ea3f1d", "0.1--hdcf5f25_2": "sha256:8148cf73d4f98270858358bacad3f391c72dae93582b8baf4e789141fa6ac8de", "0.1--h077b44d_3": "sha256:a56c7424e80d5054155f9a2671f80c82a53abb951f8b66d49f00447132532b87"}, "docker": "quay.io/biocontainers/msisensor2", "aliases": {"msisensor2": "/usr/local/bin/msisensor2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msisensor2.
shpc-registry automated BioContainers addition for msisensor2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msisensor2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msisensor2:0.1--h077b44d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msisensor2/0.1--h077b44d_3
$ module help quay.io/biocontainers/msisensor2/0.1--h077b44d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msisensor2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msisensor2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msisensor2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msisensor2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msisensor2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msisensor2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msisensor2

```bash
$ singularity exec <container> /usr/local/bin/msisensor2
$ podman run --it --rm --entrypoint /usr/local/bin/msisensor2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msisensor2   -v ${PWD} -w ${PWD} <container> -c " $@"
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