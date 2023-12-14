---
layout: container
name:  "quay.io/biocontainers/chopper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chopper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chopper/container.yaml"
updated_at: "2023-12-14 03:10:04.241053"
latest: "0.7.0--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/chopper"
aliases:
 - "chopper"
 - "clang"
 - "clang-15"
 - "clang-cl"
 - "clang-cpp"
versions:
 - "0.2.0--hd03093a_0"
 - "0.4.0--hd03093a_0"
 - "0.3.0--hd03093a_0"
 - "0.5.0--hd03093a_0"
 - "0.5.0--hdcf5f25_2"
 - "0.6.0--hdcf5f25_0"
 - "0.7.0--hdcf5f25_0"
description: "singularity registry hpc automated addition for chopper"
config: {"url": "https://biocontainers.pro/tools/chopper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chopper", "latest": {"0.7.0--hdcf5f25_0": "sha256:14f355b2d4d20905a1b662eac818d321740fa89d7eb8f65ff44851a88f0ec00e"}, "tags": {"0.2.0--hd03093a_0": "sha256:e790dd0088097b57ec66516905d5113b1a480181ef8359f5df359960d2d7512d", "0.4.0--hd03093a_0": "sha256:1ac2d6e9e1f8f6c20d2efc1722c0e5d4b09be26f2695163c5309f32299d09bc4", "0.3.0--hd03093a_0": "sha256:cf1048188833da4dbea16f3d5fd940663c3baa2b547e2b28964652e6bc9a1f86", "0.5.0--hd03093a_0": "sha256:489538b2e6e5beec594a18b70359b391e474b9b84187f0382223ecad88b6291a", "0.5.0--hdcf5f25_2": "sha256:7d493038ffb4b76fee014565d4b6fc08a1c845b7ee7e03639e63a7deb6f4515b", "0.6.0--hdcf5f25_0": "sha256:bb6e943b431ed52c4b66985778c353366c5d3d183b267468d29ea4ee930e126a", "0.7.0--hdcf5f25_0": "sha256:14f355b2d4d20905a1b662eac818d321740fa89d7eb8f65ff44851a88f0ec00e"}, "docker": "quay.io/biocontainers/chopper", "aliases": {"chopper": "/usr/local/bin/chopper", "clang": "/usr/local/bin/clang", "clang-15": "/usr/local/bin/clang-15", "clang-cl": "/usr/local/bin/clang-cl", "clang-cpp": "/usr/local/bin/clang-cpp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chopper.
singularity registry hpc automated addition for chopper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chopper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chopper:0.7.0--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chopper/0.7.0--hdcf5f25_0
$ module help quay.io/biocontainers/chopper/0.7.0--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chopper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chopper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chopper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chopper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chopper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chopper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chopper

```bash
$ singularity exec <container> /usr/local/bin/chopper
$ podman run --it --rm --entrypoint /usr/local/bin/chopper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chopper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang

```bash
$ singularity exec <container> /usr/local/bin/clang
$ podman run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-15

```bash
$ singularity exec <container> /usr/local/bin/clang-15
$ podman run --it --rm --entrypoint /usr/local/bin/clang-15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cl

```bash
$ singularity exec <container> /usr/local/bin/clang-cl
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cpp

```bash
$ singularity exec <container> /usr/local/bin/clang-cpp
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
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