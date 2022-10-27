---
layout: container
name:  "quay.io/biocontainers/bmge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bmge/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bmge/container.yaml"
updated_at: "2022-10-27 00:32:44.127105"
latest: "1.12--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bmge"
aliases:
 - "bmge"
versions:
 - "1.12--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bmge"
config: {"url": "https://biocontainers.pro/tools/bmge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bmge", "latest": {"1.12--hdfd78af_1": "sha256:a57150e63e9775579d7bb60e2104838a6f3a517d345786568bc99fdbbab8110f"}, "tags": {"1.12--hdfd78af_1": "sha256:a57150e63e9775579d7bb60e2104838a6f3a517d345786568bc99fdbbab8110f"}, "docker": "quay.io/biocontainers/bmge", "aliases": {"bmge": "/usr/local/bin/bmge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bmge.
shpc-registry automated BioContainers addition for bmge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bmge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bmge:1.12--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bmge/1.12--hdfd78af_1
$ module help quay.io/biocontainers/bmge/1.12--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bmge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bmge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bmge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bmge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bmge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bmge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bmge

```bash
$ singularity exec <container> /usr/local/bin/bmge
$ podman run --it --rm --entrypoint /usr/local/bin/bmge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmge   -v ${PWD} -w ${PWD} <container> -c " $@"
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