---
layout: container
name:  "quay.io/biocontainers/poseidon-xerxes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poseidon-xerxes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poseidon-xerxes/container.yaml"
updated_at: "2025-01-05 03:24:09.301577"
latest: "1.0.1.1--hebebf5b_1"
container_url: "https://biocontainers.pro/tools/poseidon-xerxes"
aliases:
 - "xerxes"
versions:
 - "0.1.2.2--h9325052_0"
 - "0.1.2.2--h9325052_1"
 - "0.1.2.2--hf48d1a7_2"
 - "0.3.4.0--hf48d1a7_0"
 - "1.0.0.2--hf48d1a7_0"
 - "1.0.1.1--hf48d1a7_0"
 - "1.0.1.1--hebebf5b_1"
description: "singularity registry hpc automated addition for poseidon-xerxes"
config: {"url": "https://biocontainers.pro/tools/poseidon-xerxes", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for poseidon-xerxes", "latest": {"1.0.1.1--hebebf5b_1": "sha256:5228f27081c1e44f9c8cb10dcb9e199a863f5a1ced2139faac2ad55f2ab5cfc5"}, "tags": {"0.1.2.2--h9325052_0": "sha256:3e0ddc78b256db1fa2986c4dfc5b9357a8b15a36178b9acd0542b1466877733b", "0.1.2.2--h9325052_1": "sha256:7e4198cea7e12f6af8bd19217ac340be177de18d3a48c269ede16a49a756dbba", "0.1.2.2--hf48d1a7_2": "sha256:d51b114599b4969c6e3c1dd7cc010b60eb61fa95c4e6bdc4075c6070653a8257", "0.3.4.0--hf48d1a7_0": "sha256:7311447a56c504dcf6198b6f51442da54e9ea97131c08d8c26382aa79215433a", "1.0.0.2--hf48d1a7_0": "sha256:144ee3c892aadc1024b1597e9a124f64c18e46bdb785f6ae80751642c933ae9a", "1.0.1.1--hf48d1a7_0": "sha256:0c9cffd1456a8a06b275369be39cd76c7ed899b7b8fa19ccacf07a0060523e63", "1.0.1.1--hebebf5b_1": "sha256:5228f27081c1e44f9c8cb10dcb9e199a863f5a1ced2139faac2ad55f2ab5cfc5"}, "docker": "quay.io/biocontainers/poseidon-xerxes", "aliases": {"xerxes": "/usr/local/bin/xerxes"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/poseidon-xerxes.
singularity registry hpc automated addition for poseidon-xerxes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poseidon-xerxes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poseidon-xerxes:1.0.1.1--hebebf5b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poseidon-xerxes/1.0.1.1--hebebf5b_1
$ module help quay.io/biocontainers/poseidon-xerxes/1.0.1.1--hebebf5b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poseidon-xerxes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poseidon-xerxes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poseidon-xerxes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poseidon-xerxes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poseidon-xerxes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poseidon-xerxes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xerxes

```bash
$ singularity exec <container> /usr/local/bin/xerxes
$ podman run --it --rm --entrypoint /usr/local/bin/xerxes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xerxes   -v ${PWD} -w ${PWD} <container> -c " $@"
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