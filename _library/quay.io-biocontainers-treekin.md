---
layout: container
name:  "quay.io/biocontainers/treekin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treekin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treekin/container.yaml"
updated_at: "2024-04-18 02:30:31.369117"
latest: "0.5.1--hf3d7b6d_4"
container_url: "https://biocontainers.pro/tools/treekin"
aliases:
 - "qd-config"
 - "treekin"
versions:
 - "0.5.1--hc6f38ce_2"
 - "0.5.1--hc6f38ce_3"
 - "0.5.1--hf3d7b6d_4"
description: "shpc-registry automated BioContainers addition for treekin"
config: {"url": "https://biocontainers.pro/tools/treekin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for treekin", "latest": {"0.5.1--hf3d7b6d_4": "sha256:d13a42f26ce0f23bfc8beb3caa65297a3aaf0cb786b5fa8811067f6022172e34"}, "tags": {"0.5.1--hc6f38ce_2": "sha256:98a3ac9e950a5636288d1cf83bb1e331cc9336d8e8336a479936e094843ac865", "0.5.1--hc6f38ce_3": "sha256:3f2010a154d6c9031960378fe2c01dca0341038c57d41056be55328d162e5aab", "0.5.1--hf3d7b6d_4": "sha256:d13a42f26ce0f23bfc8beb3caa65297a3aaf0cb786b5fa8811067f6022172e34"}, "docker": "quay.io/biocontainers/treekin", "aliases": {"qd-config": "/usr/local/bin/qd-config", "treekin": "/usr/local/bin/treekin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treekin.
shpc-registry automated BioContainers addition for treekin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treekin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treekin:0.5.1--hf3d7b6d_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treekin/0.5.1--hf3d7b6d_4
$ module help quay.io/biocontainers/treekin/0.5.1--hf3d7b6d_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treekin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treekin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treekin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treekin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treekin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treekin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qd-config

```bash
$ singularity exec <container> /usr/local/bin/qd-config
$ podman run --it --rm --entrypoint /usr/local/bin/qd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treekin

```bash
$ singularity exec <container> /usr/local/bin/treekin
$ podman run --it --rm --entrypoint /usr/local/bin/treekin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treekin   -v ${PWD} -w ${PWD} <container> -c " $@"
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