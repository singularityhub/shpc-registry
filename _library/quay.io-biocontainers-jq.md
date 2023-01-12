---
layout: container
name:  "quay.io/biocontainers/jq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jq/container.yaml"
updated_at: "2023-01-12 03:31:44.676255"
latest: "1.6"
container_url: "https://biocontainers.pro/tools/jq"
aliases:
 - "jq"
 - "onig-config"
versions:
 - "1.5--4"
 - "1.6"
description: "shpc-registry automated BioContainers addition for jq"
config: {"url": "https://biocontainers.pro/tools/jq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jq", "latest": {"1.6": "sha256:8ead3d706ddf3c848a4ec6e5740fb4bdcd5454a97e7c533b7417acede1de4c74"}, "tags": {"1.5--4": "sha256:231dd2321ff3470fd14c5e2a59d5fc5ecb21d91cd62a62e1110efc19138c23fe", "1.6": "sha256:8ead3d706ddf3c848a4ec6e5740fb4bdcd5454a97e7c533b7417acede1de4c74"}, "docker": "quay.io/biocontainers/jq", "aliases": {"jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jq.
shpc-registry automated BioContainers addition for jq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jq:1.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jq/1.6
$ module help quay.io/biocontainers/jq/1.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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