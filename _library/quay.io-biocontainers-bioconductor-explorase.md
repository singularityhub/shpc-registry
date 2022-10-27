---
layout: container
name:  "quay.io/biocontainers/bioconductor-explorase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-explorase/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-explorase/container.yaml"
updated_at: "2022-10-27 00:26:43.547799"
latest: "1.53.0--r40hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-explorase"
aliases:
 - "ggobi"
versions:
 - "1.53.0--r40hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-explorase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-explorase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-explorase", "latest": {"1.53.0--r40hdfd78af_2": "sha256:eda2a656e4c60f2920a9ab3ed00ecfad04746b067618eee0c082d9319ff6bcc9"}, "tags": {"1.53.0--r40hdfd78af_2": "sha256:eda2a656e4c60f2920a9ab3ed00ecfad04746b067618eee0c082d9319ff6bcc9"}, "docker": "quay.io/biocontainers/bioconductor-explorase", "aliases": {"ggobi": "/usr/local/bin/ggobi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-explorase.
shpc-registry automated BioContainers addition for bioconductor-explorase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-explorase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-explorase:1.53.0--r40hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-explorase/1.53.0--r40hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-explorase/1.53.0--r40hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-explorase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-explorase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-explorase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-explorase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-explorase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-explorase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ggobi

```bash
$ singularity exec <container> /usr/local/bin/ggobi
$ podman run --it --rm --entrypoint /usr/local/bin/ggobi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ggobi   -v ${PWD} -w ${PWD} <container> -c " $@"
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