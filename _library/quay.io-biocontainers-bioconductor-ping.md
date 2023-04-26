---
layout: container
name:  "quay.io/biocontainers/bioconductor-ping"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ping/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ping/container.yaml"
updated_at: "2023-04-26 02:43:28.688895"
latest: "2.42.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ping"

versions:
 - "2.38.0--r41hc0cfd56_2"
 - "2.42.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ping"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ping", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ping", "latest": {"2.42.0--r42hc0cfd56_0": "sha256:05f7bee952e37ac03c1df68b8a9daa467f2601bfb8a7fa79062ce676ff92d435"}, "tags": {"2.38.0--r41hc0cfd56_2": "sha256:e775289ed6871fa41a2cb690d0a37a6ee1caaf17a537d5bc3c0cf2aab62e4a2a", "2.42.0--r42hc0cfd56_0": "sha256:05f7bee952e37ac03c1df68b8a9daa467f2601bfb8a7fa79062ce676ff92d435"}, "docker": "quay.io/biocontainers/bioconductor-ping"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ping.
shpc-registry automated BioContainers addition for bioconductor-ping
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ping
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ping:2.42.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ping/2.42.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-ping/2.42.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ping-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ping-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ping-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ping-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ping-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ping-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ping

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