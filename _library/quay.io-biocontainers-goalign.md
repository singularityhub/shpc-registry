---
layout: container
name:  "quay.io/biocontainers/goalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/goalign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/goalign/container.yaml"
updated_at: "2022-11-01 03:58:57.738765"
latest: "0.3.5--h4b4d50d_1"
container_url: "https://biocontainers.pro/tools/goalign"
aliases:
 - "goalign"
 - "goalign_test.sh"
versions:
 - "0.3.5--h4b4d50d_1"
description: "shpc-registry automated BioContainers addition for goalign"
config: {"url": "https://biocontainers.pro/tools/goalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for goalign", "latest": {"0.3.5--h4b4d50d_1": "sha256:6e4e94a717a283c00bcedb937a6d4a38939253f0124e52225a29b341b0cde1dd"}, "tags": {"0.3.5--h4b4d50d_1": "sha256:6e4e94a717a283c00bcedb937a6d4a38939253f0124e52225a29b341b0cde1dd"}, "docker": "quay.io/biocontainers/goalign", "aliases": {"goalign": "/usr/local/bin/goalign", "goalign_test.sh": "/usr/local/bin/goalign_test.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/goalign.
shpc-registry automated BioContainers addition for goalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/goalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/goalign:0.3.5--h4b4d50d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/goalign/0.3.5--h4b4d50d_1
$ module help quay.io/biocontainers/goalign/0.3.5--h4b4d50d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### goalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### goalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### goalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### goalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### goalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### goalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### goalign

```bash
$ singularity exec <container> /usr/local/bin/goalign
$ podman run --it --rm --entrypoint /usr/local/bin/goalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/goalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### goalign_test.sh

```bash
$ singularity exec <container> /usr/local/bin/goalign_test.sh
$ podman run --it --rm --entrypoint /usr/local/bin/goalign_test.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/goalign_test.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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