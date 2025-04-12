---
layout: container
name:  "quay.io/biocontainers/bioconductor-tdaracne"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tdaracne/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tdaracne/container.yaml"
updated_at: "2025-04-12 03:01:47.420354"
latest: "1.47.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tdaracne"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.47.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tdaracne"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tdaracne", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tdaracne", "latest": {"1.47.0--r42hdfd78af_0": "sha256:55409ae060293d74c953972762675f24c68e3474daa15878b27d10eb953f47c1"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:049a8c4f40963b3699e08d7a841d883ec370eaaada4076df1d307580e3cd9ebb", "1.47.0--r42hdfd78af_0": "sha256:55409ae060293d74c953972762675f24c68e3474daa15878b27d10eb953f47c1"}, "docker": "quay.io/biocontainers/bioconductor-tdaracne"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tdaracne.
shpc-registry automated BioContainers addition for bioconductor-tdaracne
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tdaracne
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tdaracne:1.47.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tdaracne/1.47.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tdaracne/1.47.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tdaracne-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tdaracne-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tdaracne-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tdaracne-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tdaracne-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tdaracne-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tdaracne

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