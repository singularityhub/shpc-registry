---
layout: container
name:  "quay.io/biocontainers/pilon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pilon/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pilon/container.yaml"
updated_at: "2022-10-27 00:37:47.890534"
latest: "1.24--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pilon"

versions:
 - "1.24--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pilon"
config: {"url": "https://biocontainers.pro/tools/pilon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pilon", "latest": {"1.24--hdfd78af_0": "sha256:54c025a97d0b8763b7668383d3efa353d3ecac3f114ca7f93bffe0e71c2f7877"}, "tags": {"1.24--hdfd78af_0": "sha256:54c025a97d0b8763b7668383d3efa353d3ecac3f114ca7f93bffe0e71c2f7877"}, "docker": "quay.io/biocontainers/pilon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pilon.
shpc-registry automated BioContainers addition for pilon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pilon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pilon:1.24--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pilon/1.24--hdfd78af_0
$ module help quay.io/biocontainers/pilon/1.24--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pilon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pilon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pilon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pilon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pilon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pilon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pilon

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