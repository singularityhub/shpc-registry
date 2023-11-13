---
layout: container
name:  "quay.io/biocontainers/squid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/squid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/squid/container.yaml"
updated_at: "2023-11-13 02:32:58.241775"
latest: "1.5--h422817f_7"
container_url: "https://biocontainers.pro/tools/squid"
aliases:
 - "squid"
versions:
 - "1.5--h30ed3be_5"
 - "1.5--h82967d4_6"
 - "1.5--h422817f_7"
description: "shpc-registry automated BioContainers addition for squid"
config: {"url": "https://biocontainers.pro/tools/squid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for squid", "latest": {"1.5--h422817f_7": "sha256:69c44ab400e1053b3e2b43de2b3454cb77a10e87abf993853842e62e60b55271"}, "tags": {"1.5--h30ed3be_5": "sha256:1e7d7a7b2424c5b912514471646aca6146f02b113645f78b97ee2a91d2bfae25", "1.5--h82967d4_6": "sha256:5d0823e0720cdc9b515516d8330a4612b9823901c3a35fc4371d65e0bb661cc4", "1.5--h422817f_7": "sha256:69c44ab400e1053b3e2b43de2b3454cb77a10e87abf993853842e62e60b55271"}, "docker": "quay.io/biocontainers/squid", "aliases": {"squid": "/usr/local/bin/squid"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/squid.
shpc-registry automated BioContainers addition for squid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/squid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/squid:1.5--h422817f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/squid/1.5--h422817f_7
$ module help quay.io/biocontainers/squid/1.5--h422817f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### squid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### squid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### squid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### squid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### squid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### squid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### squid

```bash
$ singularity exec <container> /usr/local/bin/squid
$ podman run --it --rm --entrypoint /usr/local/bin/squid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/squid   -v ${PWD} -w ${PWD} <container> -c " $@"
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