---
layout: container
name:  "quay.io/biocontainers/mmannot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmannot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmannot/container.yaml"
updated_at: "2024-01-19 02:38:40.666916"
latest: "1.1--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/mmannot"
aliases:
 - "addNH"
 - "mmannot"
versions:
 - "1.0.3--hd03093a_0"
 - "1.1--hdcf5f25_2"
description: "singularity registry hpc automated addition for mmannot"
config: {"url": "https://biocontainers.pro/tools/mmannot", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mmannot", "latest": {"1.1--hdcf5f25_2": "sha256:aa0957c65da9f7493cf9967156d02ba44b2be605fb8c9ecf64f4b813ccff1ce3"}, "tags": {"1.0.3--hd03093a_0": "sha256:eaa22b49303808faa0ee3c286294985da4e192daa807832a9478da5a800ce4a9", "1.1--hdcf5f25_2": "sha256:aa0957c65da9f7493cf9967156d02ba44b2be605fb8c9ecf64f4b813ccff1ce3"}, "docker": "quay.io/biocontainers/mmannot", "aliases": {"addNH": "/usr/local/bin/addNH", "mmannot": "/usr/local/bin/mmannot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmannot.
singularity registry hpc automated addition for mmannot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmannot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmannot:1.1--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmannot/1.1--hdcf5f25_2
$ module help quay.io/biocontainers/mmannot/1.1--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmannot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmannot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmannot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmannot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmannot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmannot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addNH

```bash
$ singularity exec <container> /usr/local/bin/addNH
$ podman run --it --rm --entrypoint /usr/local/bin/addNH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addNH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmannot

```bash
$ singularity exec <container> /usr/local/bin/mmannot
$ podman run --it --rm --entrypoint /usr/local/bin/mmannot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmannot   -v ${PWD} -w ${PWD} <container> -c " $@"
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