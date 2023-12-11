---
layout: container
name:  "quay.io/biocontainers/metacluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metacluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metacluster/container.yaml"
updated_at: "2023-12-11 02:50:49.876061"
latest: "5.1--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/metacluster"
aliases:
 - "MetaCluster4Fast"
 - "MetaCluster5_1"
 - "MetaCluster5_2"
versions:
 - "5.1--h9f5acd7_4"
 - "5.1--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for metacluster"
config: {"url": "https://biocontainers.pro/tools/metacluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metacluster", "latest": {"5.1--h4ac6f70_6": "sha256:e01c15f812b89a041aa16a10d93352c7a4b9f533918468a26cbfb0b8f21961a8"}, "tags": {"5.1--h9f5acd7_4": "sha256:332254c868999fcb1ad8329f9f81e48fbe52e35ba76514c866e6351f1ef5fac0", "5.1--h4ac6f70_6": "sha256:e01c15f812b89a041aa16a10d93352c7a4b9f533918468a26cbfb0b8f21961a8"}, "docker": "quay.io/biocontainers/metacluster", "aliases": {"MetaCluster4Fast": "/usr/local/bin/MetaCluster4Fast", "MetaCluster5_1": "/usr/local/bin/MetaCluster5_1", "MetaCluster5_2": "/usr/local/bin/MetaCluster5_2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metacluster.
shpc-registry automated BioContainers addition for metacluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metacluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metacluster:5.1--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metacluster/5.1--h4ac6f70_6
$ module help quay.io/biocontainers/metacluster/5.1--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metacluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metacluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metacluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metacluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metacluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metacluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MetaCluster4Fast

```bash
$ singularity exec <container> /usr/local/bin/MetaCluster4Fast
$ podman run --it --rm --entrypoint /usr/local/bin/MetaCluster4Fast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaCluster4Fast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaCluster5_1

```bash
$ singularity exec <container> /usr/local/bin/MetaCluster5_1
$ podman run --it --rm --entrypoint /usr/local/bin/MetaCluster5_1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaCluster5_1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetaCluster5_2

```bash
$ singularity exec <container> /usr/local/bin/MetaCluster5_2
$ podman run --it --rm --entrypoint /usr/local/bin/MetaCluster5_2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaCluster5_2   -v ${PWD} -w ${PWD} <container> -c " $@"
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