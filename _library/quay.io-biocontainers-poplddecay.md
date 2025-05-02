---
layout: container
name:  "quay.io/biocontainers/poplddecay"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poplddecay/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poplddecay/container.yaml"
updated_at: "2025-05-02 03:55:12.148685"
latest: "3.43--h077b44d_2"
container_url: "https://biocontainers.pro/tools/poplddecay"
aliases:
 - "PopLDdecay"
versions:
 - "3.43--hdcf5f25_1"
 - "3.43--h077b44d_2"
description: "singularity registry hpc automated addition for poplddecay"
config: {"url": "https://biocontainers.pro/tools/poplddecay", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for poplddecay", "latest": {"3.43--h077b44d_2": "sha256:731289cdec93a4368b7698b36a91729a3da59328f40779a0e5e1391f87aff352"}, "tags": {"3.43--hdcf5f25_1": "sha256:c17344b653dfef522cc9635876c62bfcc16b2469ad0dfe9c7714aa50e9674de0", "3.43--h077b44d_2": "sha256:731289cdec93a4368b7698b36a91729a3da59328f40779a0e5e1391f87aff352"}, "docker": "quay.io/biocontainers/poplddecay", "aliases": {"PopLDdecay": "/usr/local/bin/PopLDdecay"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/poplddecay.
singularity registry hpc automated addition for poplddecay
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poplddecay
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poplddecay:3.43--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poplddecay/3.43--h077b44d_2
$ module help quay.io/biocontainers/poplddecay/3.43--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poplddecay-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poplddecay-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poplddecay-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poplddecay-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poplddecay-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poplddecay-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PopLDdecay

```bash
$ singularity exec <container> /usr/local/bin/PopLDdecay
$ podman run --it --rm --entrypoint /usr/local/bin/PopLDdecay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PopLDdecay   -v ${PWD} -w ${PWD} <container> -c " $@"
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