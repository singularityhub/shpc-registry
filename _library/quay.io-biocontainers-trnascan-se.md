---
layout: container
name:  "quay.io/biocontainers/trnascan-se"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trnascan-se/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/trnascan-se/container.yaml"
updated_at: "2022-10-27 00:32:32.177247"
latest: "2.0.9--pl5321hec16e2b_3"
container_url: "https://biocontainers.pro/tools/trnascan-se"

versions:
 - "2.0.9--pl5321hec16e2b_3"
description: "shpc-registry automated BioContainers addition for trnascan-se"
config: {"url": "https://biocontainers.pro/tools/trnascan-se", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trnascan-se", "latest": {"2.0.9--pl5321hec16e2b_3": "sha256:fd0e8936d0d819cdfee10e4d5246cfc07a52b391432b525390580fc42c08d9db"}, "tags": {"2.0.9--pl5321hec16e2b_3": "sha256:fd0e8936d0d819cdfee10e4d5246cfc07a52b391432b525390580fc42c08d9db"}, "docker": "quay.io/biocontainers/trnascan-se"}
---

This module is a singularity container wrapper for quay.io/biocontainers/trnascan-se.
shpc-registry automated BioContainers addition for trnascan-se
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trnascan-se
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trnascan-se:2.0.9--pl5321hec16e2b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trnascan-se/2.0.9--pl5321hec16e2b_3
$ module help quay.io/biocontainers/trnascan-se/2.0.9--pl5321hec16e2b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trnascan-se-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trnascan-se-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trnascan-se-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trnascan-se-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trnascan-se-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trnascan-se-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### trnascan-se

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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