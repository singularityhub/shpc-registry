---
layout: container
name:  "quay.io/biocontainers/bioconductor-miasim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-miasim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-miasim/container.yaml"
updated_at: "2024-01-10 03:11:52.001713"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-miasim"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-miasim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-miasim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-miasim", "latest": {"1.8.0--r43hdfd78af_0": "sha256:e270f4e353106542743c0b9eb91578e9d446902a4c059194d3337022b5755d56"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:81851e2e601e89d43957d634afb11774eb000940c19099e91d9a8bb6908004d3", "1.4.0--r42hdfd78af_0": "sha256:7f29aed5ddf6b438ffb436485e46cc28bcf59c159da7536defa87f1445da8289", "1.6.0--r43hdfd78af_0": "sha256:1109aecf2f9cd40a1a2c89620f2d971936f6b66c5ce57873aabe326a554f357a", "1.8.0--r43hdfd78af_0": "sha256:e270f4e353106542743c0b9eb91578e9d446902a4c059194d3337022b5755d56"}, "docker": "quay.io/biocontainers/bioconductor-miasim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-miasim.
shpc-registry automated BioContainers addition for bioconductor-miasim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-miasim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-miasim:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-miasim/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-miasim/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-miasim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-miasim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-miasim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-miasim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-miasim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-miasim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-miasim

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