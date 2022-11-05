---
layout: container
name:  "quay.io/biocontainers/r-syntactic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-syntactic/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-syntactic/container.yaml"
updated_at: "2022-11-05 00:08:42.801924"
latest: "0.5.2--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-syntactic"

versions:
 - "0.5.2--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-syntactic"
config: {"url": "https://biocontainers.pro/tools/r-syntactic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-syntactic", "latest": {"0.5.2--r41hdfd78af_0": "sha256:cdd5fbf4e79457feecca9b70fb1916e9ce81781da6aded717829b228e2a2a91d"}, "tags": {"0.5.2--r41hdfd78af_0": "sha256:cdd5fbf4e79457feecca9b70fb1916e9ce81781da6aded717829b228e2a2a91d"}, "docker": "quay.io/biocontainers/r-syntactic"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-syntactic.
shpc-registry automated BioContainers addition for r-syntactic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-syntactic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-syntactic:0.5.2--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-syntactic/0.5.2--r41hdfd78af_0
$ module help quay.io/biocontainers/r-syntactic/0.5.2--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-syntactic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-syntactic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-syntactic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-syntactic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-syntactic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-syntactic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-syntactic

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