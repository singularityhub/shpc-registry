---
layout: container
name:  "quay.io/biocontainers/bioconductor-paeg1aprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-paeg1aprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-paeg1aprobe/container.yaml"
updated_at: "2024-11-28 03:03:36.401591"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-paeg1aprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-paeg1aprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-paeg1aprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-paeg1aprobe", "latest": {"2.18.0--r43hdfd78af_13": "sha256:4b913c6d99d4abef11c229c77335e82e8ce39f75c1c07f0cfe9fd4d52b63e643"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:47b25ff3f0bbc3612e4649ceea7a03ace9be6e788f8c6cc1099cab6c3fc20f19", "2.18.0--r42hdfd78af_11": "sha256:0dc4cab27d918a644cae756a31d8431835416ac0779b897784fe04990c2f2b66", "2.18.0--r43hdfd78af_12": "sha256:05ae063e7d76508cb142a1a512d78981e95c8893f7f72127d601a3ca1ce26e57", "2.18.0--r43hdfd78af_13": "sha256:4b913c6d99d4abef11c229c77335e82e8ce39f75c1c07f0cfe9fd4d52b63e643"}, "docker": "quay.io/biocontainers/bioconductor-paeg1aprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-paeg1aprobe.
shpc-registry automated BioContainers addition for bioconductor-paeg1aprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-paeg1aprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-paeg1aprobe:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-paeg1aprobe/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-paeg1aprobe/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-paeg1aprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paeg1aprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paeg1aprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-paeg1aprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-paeg1aprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-paeg1aprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-paeg1aprobe

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