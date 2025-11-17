---
layout: container
name:  "quay.io/biocontainers/deepchopper-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepchopper-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deepchopper-cli/container.yaml"
updated_at: "2025-11-17 03:22:44.342170"
latest: "1.2.6--py310h9e6395a_1"
container_url: "https://biocontainers.pro/tools/deepchopper-cli"
aliases:
 - "deepchopper-chop"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.2.5--py310h77ce02f_0"
 - "1.2.5--py311hbbdcbde_0"
 - "1.2.6--py311hbbdcbde_0"
 - "1.2.6--py310h9e6395a_1"
description: "singularity registry hpc automated addition for deepchopper-cli"
config: {"url": "https://biocontainers.pro/tools/deepchopper-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for deepchopper-cli", "latest": {"1.2.6--py310h9e6395a_1": "sha256:deb2dd6ef82e6ab231f5a8d107f2a03e39643a7f9bac451b789922012e89c2f1"}, "tags": {"1.2.5--py310h77ce02f_0": "sha256:ad0ca174164b9d4541528956992cf9b6740de0b961eb60649f093885cf7f89ef", "1.2.5--py311hbbdcbde_0": "sha256:3c27c10d314ec2d3b765c7793193abbe2617899c4a055a51bc683b26b5634f0b", "1.2.6--py311hbbdcbde_0": "sha256:ce203f9353082f9c5a59c3c841eada0a9123336ae07959869a3b0e8a32bbeec8", "1.2.6--py310h9e6395a_1": "sha256:deb2dd6ef82e6ab231f5a8d107f2a03e39643a7f9bac451b789922012e89c2f1"}, "docker": "quay.io/biocontainers/deepchopper-cli", "aliases": {"deepchopper-chop": "/usr/local/bin/deepchopper-chop", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepchopper-cli.
singularity registry hpc automated addition for deepchopper-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepchopper-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepchopper-cli:1.2.6--py310h9e6395a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepchopper-cli/1.2.6--py310h9e6395a_1
$ module help quay.io/biocontainers/deepchopper-cli/1.2.6--py310h9e6395a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepchopper-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepchopper-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepchopper-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepchopper-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepchopper-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepchopper-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepchopper-chop

```bash
$ singularity exec <container> /usr/local/bin/deepchopper-chop
$ podman run --it --rm --entrypoint /usr/local/bin/deepchopper-chop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepchopper-chop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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