---
layout: container
name:  "quay.io/biocontainers/migraine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/migraine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/migraine/container.yaml"
updated_at: "2024-01-02 02:32:06.685760"
latest: "0.6.0--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/migraine"
aliases:
 - "migraine"
versions:
 - "0.6.0--h9f5acd7_1"
 - "0.6.0--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for migraine"
config: {"url": "https://biocontainers.pro/tools/migraine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for migraine", "latest": {"0.6.0--h4ac6f70_3": "sha256:c8e699b0fd9b6659c8bcbed7b7c687291151a2926d8828d8c5ff24ab39504c5d"}, "tags": {"0.6.0--h9f5acd7_1": "sha256:706ef4cb96d7a213c0f33a00cd6b9de71008f8f950a7444a42395eb367452bf4", "0.6.0--h4ac6f70_3": "sha256:c8e699b0fd9b6659c8bcbed7b7c687291151a2926d8828d8c5ff24ab39504c5d"}, "docker": "quay.io/biocontainers/migraine", "aliases": {"migraine": "/usr/local/bin/migraine"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/migraine.
shpc-registry automated BioContainers addition for migraine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/migraine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/migraine:0.6.0--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/migraine/0.6.0--h4ac6f70_3
$ module help quay.io/biocontainers/migraine/0.6.0--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### migraine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### migraine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### migraine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### migraine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### migraine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### migraine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### migraine

```bash
$ singularity exec <container> /usr/local/bin/migraine
$ podman run --it --rm --entrypoint /usr/local/bin/migraine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/migraine   -v ${PWD} -w ${PWD} <container> -c " $@"
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