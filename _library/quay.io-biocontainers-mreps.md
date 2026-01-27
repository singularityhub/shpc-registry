---
layout: container
name:  "quay.io/biocontainers/mreps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mreps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mreps/container.yaml"
updated_at: "2026-01-27 04:09:02.322492"
latest: "2.6.01--h7b50bb2_6"
container_url: "https://biocontainers.pro/tools/mreps"
aliases:
 - "mreps"
versions:
 - "2.6.01--hec16e2b_2"
 - "2.6.01--h031d066_4"
 - "2.6.01--h7b50bb2_5"
 - "2.6.01--h7b50bb2_6"
description: "shpc-registry automated BioContainers addition for mreps"
config: {"url": "https://biocontainers.pro/tools/mreps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mreps", "latest": {"2.6.01--h7b50bb2_6": "sha256:e4def78224925965880c53e6bc65e3ae3041c101e0834aa02d7431df1831e254"}, "tags": {"2.6.01--hec16e2b_2": "sha256:345b5ddf18348e042b24a8b553d7755deceb7118fd672af40af68f5affddf04a", "2.6.01--h031d066_4": "sha256:90cab4d1b63ce826b650a60a6bf882cf422f4ddd086be24634d9ec4101ddcbff", "2.6.01--h7b50bb2_5": "sha256:b542fed82de2b564e2998ce64a370d44a6828e5de377eba4a9a12a72aea512ac", "2.6.01--h7b50bb2_6": "sha256:e4def78224925965880c53e6bc65e3ae3041c101e0834aa02d7431df1831e254"}, "docker": "quay.io/biocontainers/mreps", "aliases": {"mreps": "/usr/local/bin/mreps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mreps.
shpc-registry automated BioContainers addition for mreps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mreps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mreps:2.6.01--h7b50bb2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mreps/2.6.01--h7b50bb2_6
$ module help quay.io/biocontainers/mreps/2.6.01--h7b50bb2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mreps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mreps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mreps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mreps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mreps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mreps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mreps

```bash
$ singularity exec <container> /usr/local/bin/mreps
$ podman run --it --rm --entrypoint /usr/local/bin/mreps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mreps   -v ${PWD} -w ${PWD} <container> -c " $@"
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