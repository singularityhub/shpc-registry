---
layout: container
name:  "quay.io/biocontainers/d4tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/d4tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/d4tools/container.yaml"
updated_at: "2024-02-21 02:36:58.620206"
latest: "0.3.8--hdbdd923_1"
container_url: "https://biocontainers.pro/tools/d4tools"
aliases:
 - "d4tools"
 - "starcode"
versions:
 - "0.3.8--h87f3376_0"
 - "0.3.8--hdbdd923_1"
description: "singularity registry hpc automated addition for d4tools"
config: {"url": "https://biocontainers.pro/tools/d4tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for d4tools", "latest": {"0.3.8--hdbdd923_1": "sha256:3f6e427b4b2dc4860e21fd106924a46569b8590e7597a8748247467d556bd594"}, "tags": {"0.3.8--h87f3376_0": "sha256:cee34924572fe75db1e653d33953b6824701544478f2a38d40abe2cc59132916", "0.3.8--hdbdd923_1": "sha256:3f6e427b4b2dc4860e21fd106924a46569b8590e7597a8748247467d556bd594"}, "docker": "quay.io/biocontainers/d4tools", "aliases": {"d4tools": "/usr/local/bin/d4tools", "starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/d4tools.
singularity registry hpc automated addition for d4tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/d4tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/d4tools:0.3.8--hdbdd923_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/d4tools/0.3.8--hdbdd923_1
$ module help quay.io/biocontainers/d4tools/0.3.8--hdbdd923_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### d4tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### d4tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### d4tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### d4tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### d4tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### d4tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### d4tools

```bash
$ singularity exec <container> /usr/local/bin/d4tools
$ podman run --it --rm --entrypoint /usr/local/bin/d4tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/d4tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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