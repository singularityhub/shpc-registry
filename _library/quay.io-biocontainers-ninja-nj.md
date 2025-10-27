---
layout: container
name:  "quay.io/biocontainers/ninja-nj"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ninja-nj/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ninja-nj/container.yaml"
updated_at: "2025-10-27 04:13:53.094667"
latest: "1.00--h9948957_1"
container_url: "https://biocontainers.pro/tools/ninja-nj"
aliases:
 - "Ninja"
versions:
 - "0.97--h9f5acd7_0"
 - "0.98--h9f5acd7_0"
 - "0.98--h4ac6f70_2"
 - "0.98--h4ac6f70_3"
 - "1.00--h9948957_1"
description: "singularity registry hpc automated addition for ninja-nj"
config: {"url": "https://biocontainers.pro/tools/ninja-nj", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ninja-nj", "latest": {"1.00--h9948957_1": "sha256:3baabeedf0020cdb646124743ee743ef000b5a85c6453a038588d1651ec649c0"}, "tags": {"0.97--h9f5acd7_0": "sha256:216fc2e2ba8905fc249e6dbd42c55dae95c05f2af38575d6de2090984196ee58", "0.98--h9f5acd7_0": "sha256:cb14554ac2dbed7c3db8f9962b921858fa6c0b4c9d433a6404c13d63d82d9cb6", "0.98--h4ac6f70_2": "sha256:b2c905e233e13827974544424b7ca760c2ded941eb99b67b530188174efc5b97", "0.98--h4ac6f70_3": "sha256:6665b55a190cd722177d68aa5067b49d8fe544295f01133a7781ee64dac438a5", "1.00--h9948957_1": "sha256:3baabeedf0020cdb646124743ee743ef000b5a85c6453a038588d1651ec649c0"}, "docker": "quay.io/biocontainers/ninja-nj", "aliases": {"Ninja": "/usr/local/bin/Ninja"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ninja-nj.
singularity registry hpc automated addition for ninja-nj
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ninja-nj
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ninja-nj:1.00--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ninja-nj/1.00--h9948957_1
$ module help quay.io/biocontainers/ninja-nj/1.00--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ninja-nj-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ninja-nj-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ninja-nj-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ninja-nj-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ninja-nj-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ninja-nj-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Ninja

```bash
$ singularity exec <container> /usr/local/bin/Ninja
$ podman run --it --rm --entrypoint /usr/local/bin/Ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
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