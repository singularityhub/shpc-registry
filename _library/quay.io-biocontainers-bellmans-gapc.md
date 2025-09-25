---
layout: container
name:  "quay.io/biocontainers/bellmans-gapc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bellmans-gapc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bellmans-gapc/container.yaml"
updated_at: "2025-09-25 03:16:21.548557"
latest: "2024.01.12--h3053a90_5"
container_url: "https://biocontainers.pro/tools/bellmans-gapc"
aliases:
 - "gapc"
versions:
 - "2022.07.04--h16d3260_0"
 - "2022.07.04--h16d3260_1"
 - "2022.07.04--hac0e68f_2"
 - "2023.07.05--hac0e68f_0"
 - "2024.01.12--hac0e68f_0"
 - "2024.01.12--h0432e7c_1"
 - "2024.01.12--h0432e7c_3"
 - "2024.01.12--h3053a90_4"
 - "2024.01.12--h3053a90_5"
description: "shpc-registry automated BioContainers addition for bellmans-gapc"
config: {"url": "https://biocontainers.pro/tools/bellmans-gapc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bellmans-gapc", "latest": {"2024.01.12--h3053a90_5": "sha256:1d363afab735de347127f04dec65a0b9426cf4d9a24230893cf80e0a19705c94"}, "tags": {"2022.07.04--h16d3260_0": "sha256:855d0499991c6977e7e904c86c0ac1cff89ac6a0386e719b0635dc71c366520b", "2022.07.04--h16d3260_1": "sha256:d3687cbcc0a8a48f7a328c6e1b6bdb3e76000b3c3c165faea609d4de96c3c319", "2022.07.04--hac0e68f_2": "sha256:f341ee1cf4c49a4ed8c45b17c09e5122597475a92e8b8d0bc4bf88cfd9e3cc83", "2023.07.05--hac0e68f_0": "sha256:c8b9a19590d103a8cdc51a99ad7aace89d13968b795798f359e7f8e39abc86a6", "2024.01.12--hac0e68f_0": "sha256:dfee14f73e761687d795568a97d422f47b828f1c857b006fae4e20983ec656bb", "2024.01.12--h0432e7c_1": "sha256:b831ab4e1db31f3e014f51c0c2c086f37dbca046bfb70406f72905d0f6c8e731", "2024.01.12--h0432e7c_3": "sha256:f65487341a5a4287d73c88f751820062b782e2b4aee2fd9b03c2e8acaf58e5f8", "2024.01.12--h3053a90_4": "sha256:ba4a4b5251884dad1a6aa5644a59086dde15e5b08a40fc1b06cf3555628e7fe8", "2024.01.12--h3053a90_5": "sha256:1d363afab735de347127f04dec65a0b9426cf4d9a24230893cf80e0a19705c94"}, "docker": "quay.io/biocontainers/bellmans-gapc", "aliases": {"gapc": "/usr/local/bin/gapc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bellmans-gapc.
shpc-registry automated BioContainers addition for bellmans-gapc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bellmans-gapc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bellmans-gapc:2024.01.12--h3053a90_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bellmans-gapc/2024.01.12--h3053a90_5
$ module help quay.io/biocontainers/bellmans-gapc/2024.01.12--h3053a90_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bellmans-gapc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bellmans-gapc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bellmans-gapc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bellmans-gapc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bellmans-gapc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bellmans-gapc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gapc

```bash
$ singularity exec <container> /usr/local/bin/gapc
$ podman run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
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