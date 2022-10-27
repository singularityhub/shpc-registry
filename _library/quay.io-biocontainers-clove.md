---
layout: container
name:  "quay.io/biocontainers/clove"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clove/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/clove/container.yaml"
updated_at: "2022-10-27 00:58:34.078858"
latest: "0.17--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/clove"
aliases:
 - "clove"
versions:
 - "0.17--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for clove"
config: {"url": "https://biocontainers.pro/tools/clove", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clove", "latest": {"0.17--hdfd78af_2": "sha256:6e44fe93b8364c5c0fe808922ceaef7cb181ddca2a31204ac5b484e126a5dc6f"}, "tags": {"0.17--hdfd78af_2": "sha256:6e44fe93b8364c5c0fe808922ceaef7cb181ddca2a31204ac5b484e126a5dc6f"}, "docker": "quay.io/biocontainers/clove", "aliases": {"clove": "/usr/local/bin/clove"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clove.
shpc-registry automated BioContainers addition for clove
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clove
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clove:0.17--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clove/0.17--hdfd78af_2
$ module help quay.io/biocontainers/clove/0.17--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clove-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clove-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clove-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clove-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clove-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clove-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clove

```bash
$ singularity exec <container> /usr/local/bin/clove
$ podman run --it --rm --entrypoint /usr/local/bin/clove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clove   -v ${PWD} -w ${PWD} <container> -c " $@"
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