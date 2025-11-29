---
layout: container
name:  "quay.io/biocontainers/aardvark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aardvark/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aardvark/container.yaml"
updated_at: "2025-11-29 02:21:03.859289"
latest: "0.9.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/aardvark"
aliases:
 - "aardvark"
versions:
 - "0.7.3--h4349ce8_0"
 - "0.7.4--h4349ce8_0"
 - "0.8.0--h4349ce8_0"
 - "0.8.1--h4349ce8_1"
 - "0.9.0--h4349ce8_0"
description: "singularity registry hpc automated addition for aardvark"
config: {"url": "https://biocontainers.pro/tools/aardvark", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aardvark", "latest": {"0.9.0--h4349ce8_0": "sha256:3bba494689e67e7596be913cc240eb6523b1bd080e28de0afaf461665ec5784c"}, "tags": {"0.7.3--h4349ce8_0": "sha256:bcac1d1cdd20da85b3d71aecb4349273879024cde2c57ec83ed4ee688bd13b52", "0.7.4--h4349ce8_0": "sha256:a474c90d66b249e802e2366341fb82212c2dcd9e4a80daf3b22db1c57ff278fd", "0.8.0--h4349ce8_0": "sha256:1e0b5a564ddc66895b9204233c8abd5ee63d263107aaf689f4a7521de2010797", "0.8.1--h4349ce8_1": "sha256:d031876c6627c068d893a5e32120cba48fe7f50e928850049cbe8cb6af7a0705", "0.9.0--h4349ce8_0": "sha256:3bba494689e67e7596be913cc240eb6523b1bd080e28de0afaf461665ec5784c"}, "docker": "quay.io/biocontainers/aardvark", "aliases": {"aardvark": "/usr/local/bin/aardvark"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aardvark.
singularity registry hpc automated addition for aardvark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aardvark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aardvark:0.9.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aardvark/0.9.0--h4349ce8_0
$ module help quay.io/biocontainers/aardvark/0.9.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aardvark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aardvark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aardvark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aardvark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aardvark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aardvark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aardvark

```bash
$ singularity exec <container> /usr/local/bin/aardvark
$ podman run --it --rm --entrypoint /usr/local/bin/aardvark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aardvark   -v ${PWD} -w ${PWD} <container> -c " $@"
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