---
layout: container
name:  "quay.io/biocontainers/impg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/impg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/impg/container.yaml"
updated_at: "2025-08-10 04:03:29.186845"
latest: "0.2.4--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/impg"
aliases:
 - "impg"
versions:
 - "0.2.0--h4349ce8_0"
 - "0.2.1--h4349ce8_1"
 - "0.2.2--h4349ce8_0"
 - "0.2.3--h4349ce8_0"
 - "0.2.4--h4349ce8_0"
description: "singularity registry hpc automated addition for impg"
config: {"url": "https://biocontainers.pro/tools/impg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for impg", "latest": {"0.2.4--h4349ce8_0": "sha256:b127f2217178572093eae767deff34de2c13396ea962d3bfbb0c3776939d087e"}, "tags": {"0.2.0--h4349ce8_0": "sha256:6cdafc0ab3c61e21416922011fd5a3a0a4c1d747503bacd3d9f70e6fa99b02ae", "0.2.1--h4349ce8_1": "sha256:45a731507d9680cac61e31f33d479310148c8d3e1e4bc4393e38af3a2f715536", "0.2.2--h4349ce8_0": "sha256:4c19a6002e7cc5b66d61b7bcabff34cfc890662c96ea3be9fb0372eca0854609", "0.2.3--h4349ce8_0": "sha256:24e8904aa2859293cca9e86a94677b574ae9e8cd3d6f8fb28001f8676c4c8696", "0.2.4--h4349ce8_0": "sha256:b127f2217178572093eae767deff34de2c13396ea962d3bfbb0c3776939d087e"}, "docker": "quay.io/biocontainers/impg", "aliases": {"impg": "/usr/local/bin/impg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/impg.
singularity registry hpc automated addition for impg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/impg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/impg:0.2.4--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/impg/0.2.4--h4349ce8_0
$ module help quay.io/biocontainers/impg/0.2.4--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### impg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### impg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### impg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### impg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### impg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### impg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### impg

```bash
$ singularity exec <container> /usr/local/bin/impg
$ podman run --it --rm --entrypoint /usr/local/bin/impg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impg   -v ${PWD} -w ${PWD} <container> -c " $@"
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