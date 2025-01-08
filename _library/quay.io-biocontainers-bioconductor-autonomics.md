---
layout: container
name:  "quay.io/biocontainers/bioconductor-autonomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-autonomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-autonomics/container.yaml"
updated_at: "2025-01-08 03:17:15.618996"
latest: "1.10.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-autonomics"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-autonomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-autonomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-autonomics", "latest": {"1.10.2--r43hdfd78af_0": "sha256:f9b1a2667e42d21b1d88ebb57faf265a1f62ca10e006e8c0b975e12d18fe42c3"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:5ecf76b90b44c0592fdd77fcc64e33f2ce159f1a01d180f747745627f8ea2a02", "1.6.0--r42hdfd78af_0": "sha256:8964b3e957039d322f1539ed88c22c4c53aeac25e6e434fc0bc6d0032f82e4d4", "1.8.0--r43hdfd78af_0": "sha256:6ada179c4b1d2db8d9e317d538731449145007becb7d8091d9efc74861e33f68", "1.10.2--r43hdfd78af_0": "sha256:f9b1a2667e42d21b1d88ebb57faf265a1f62ca10e006e8c0b975e12d18fe42c3"}, "docker": "quay.io/biocontainers/bioconductor-autonomics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-autonomics.
shpc-registry automated BioContainers addition for bioconductor-autonomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-autonomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-autonomics:1.10.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-autonomics/1.10.2--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-autonomics/1.10.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-autonomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-autonomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-autonomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-autonomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-autonomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-autonomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-autonomics

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