---
layout: container
name:  "quay.io/biocontainers/grep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grep/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/grep/container.yaml"
updated_at: "2022-10-27 00:32:47.546646"
latest: "3.4--hcb20899_2"
container_url: "https://biocontainers.pro/tools/grep"

versions:
 - "3.4--hcb20899_2"
description: "shpc-registry automated BioContainers addition for grep"
config: {"url": "https://biocontainers.pro/tools/grep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for grep", "latest": {"3.4--hcb20899_2": "sha256:8482764cb21b0d1250b7947b9343a8503cdfa22be79ff292f7c3393c81062fbc"}, "tags": {"3.4--hcb20899_2": "sha256:8482764cb21b0d1250b7947b9343a8503cdfa22be79ff292f7c3393c81062fbc"}, "docker": "quay.io/biocontainers/grep"}
---

This module is a singularity container wrapper for quay.io/biocontainers/grep.
shpc-registry automated BioContainers addition for grep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grep:3.4--hcb20899_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grep/3.4--hcb20899_2
$ module help quay.io/biocontainers/grep/3.4--hcb20899_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### grep

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