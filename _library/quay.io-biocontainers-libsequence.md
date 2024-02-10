---
layout: container
name:  "quay.io/biocontainers/libsequence"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libsequence/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libsequence/container.yaml"
updated_at: "2024-02-10 02:20:49.341551"
latest: "1.9.8--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/libsequence"
aliases:
 - "libsequenceConfig"
versions:
 - "1.9.8--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for libsequence"
config: {"url": "https://biocontainers.pro/tools/libsequence", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libsequence", "latest": {"1.9.8--h9f5acd7_4": "sha256:3073690ddad9f7be0d7c7af5cbf365460b5dcc6a2c167987716c3dc7ac2ac8de"}, "tags": {"1.9.8--h9f5acd7_4": "sha256:3073690ddad9f7be0d7c7af5cbf365460b5dcc6a2c167987716c3dc7ac2ac8de"}, "docker": "quay.io/biocontainers/libsequence", "aliases": {"libsequenceConfig": "/usr/local/bin/libsequenceConfig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/libsequence.
shpc-registry automated BioContainers addition for libsequence
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libsequence
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libsequence:1.9.8--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libsequence/1.9.8--h9f5acd7_4
$ module help quay.io/biocontainers/libsequence/1.9.8--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libsequence-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libsequence-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libsequence-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libsequence-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libsequence-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libsequence-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### libsequenceConfig

```bash
$ singularity exec <container> /usr/local/bin/libsequenceConfig
$ podman run --it --rm --entrypoint /usr/local/bin/libsequenceConfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libsequenceConfig   -v ${PWD} -w ${PWD} <container> -c " $@"
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