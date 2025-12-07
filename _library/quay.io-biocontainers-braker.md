---
layout: container
name:  "quay.io/biocontainers/braker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/braker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/braker/container.yaml"
updated_at: "2025-12-07 03:50:56.013227"
latest: "1.9--pl5321hdfd78af_6"
container_url: "https://biocontainers.pro/tools/braker"

versions:
 - "1.9--pl5321hdfd78af_6"
description: "shpc-registry automated BioContainers addition for braker"
config: {"url": "https://biocontainers.pro/tools/braker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for braker", "latest": {"1.9--pl5321hdfd78af_6": "sha256:2fb42337ecccecabda76a9d28514fd150dd724adad99368f44e742fb57fa2370"}, "tags": {"1.9--pl5321hdfd78af_6": "sha256:2fb42337ecccecabda76a9d28514fd150dd724adad99368f44e742fb57fa2370"}, "docker": "quay.io/biocontainers/braker"}
---

This module is a singularity container wrapper for quay.io/biocontainers/braker.
shpc-registry automated BioContainers addition for braker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/braker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/braker:1.9--pl5321hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/braker/1.9--pl5321hdfd78af_6
$ module help quay.io/biocontainers/braker/1.9--pl5321hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### braker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### braker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### braker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### braker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### braker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### braker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### braker

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