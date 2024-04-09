---
layout: container
name:  "quay.io/biocontainers/r-scbio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-scbio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-scbio/container.yaml"
updated_at: "2024-04-09 02:58:03.674241"
latest: "0.1.4--r43hdfd78af_2"
container_url: "https://biocontainers.pro/tools/r-scbio"

versions:
 - "0.1.4--r41hdfd78af_0"
 - "0.1.4--r42hdfd78af_1"
 - "0.1.4--r43hdfd78af_2"
description: "shpc-registry automated BioContainers addition for r-scbio"
config: {"url": "https://biocontainers.pro/tools/r-scbio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-scbio", "latest": {"0.1.4--r43hdfd78af_2": "sha256:747fa3ea89791787ec52f14c398af5b0b5f30dbe88995e8a61e13cfa17982e32"}, "tags": {"0.1.4--r41hdfd78af_0": "sha256:9b76b189e54d5aa42dff5817aedbbe9f786294712793b4195be2083017a007ef", "0.1.4--r42hdfd78af_1": "sha256:610f65d1980849f0b1adfb1252b7c1305a045a6437e973b587b93a86f485df49", "0.1.4--r43hdfd78af_2": "sha256:747fa3ea89791787ec52f14c398af5b0b5f30dbe88995e8a61e13cfa17982e32"}, "docker": "quay.io/biocontainers/r-scbio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-scbio.
shpc-registry automated BioContainers addition for r-scbio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-scbio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-scbio:0.1.4--r43hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-scbio/0.1.4--r43hdfd78af_2
$ module help quay.io/biocontainers/r-scbio/0.1.4--r43hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-scbio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-scbio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-scbio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-scbio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-scbio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-scbio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-scbio

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