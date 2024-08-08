---
layout: container
name:  "quay.io/biocontainers/bioconductor-affyhgu133aexpr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affyhgu133aexpr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affyhgu133aexpr/container.yaml"
updated_at: "2024-08-08 02:41:59.623326"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affyhgu133aexpr"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affyhgu133aexpr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affyhgu133aexpr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affyhgu133aexpr", "latest": {"1.40.0--r43hdfd78af_0": "sha256:a676ae17dfead694546e7f50c786c480b78bd39d7ff530df9bed7c2510dbfa64"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:2741bb47953188437a76bc4a6fb30e5dbc8851b8e83722bb0f50e92d3be471de", "1.35.0--r42hdfd78af_0": "sha256:3558661c351b432fb141005bae5647b1b1eccb766529a969cf6c0fd2778ffb43", "1.38.0--r43hdfd78af_0": "sha256:18e6557f51de5f56266fd0de05b9c0a6e6878c0f5987fa3bc0aaf04afb6f750b", "1.40.0--r43hdfd78af_0": "sha256:a676ae17dfead694546e7f50c786c480b78bd39d7ff530df9bed7c2510dbfa64"}, "docker": "quay.io/biocontainers/bioconductor-affyhgu133aexpr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affyhgu133aexpr.
shpc-registry automated BioContainers addition for bioconductor-affyhgu133aexpr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affyhgu133aexpr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affyhgu133aexpr:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affyhgu133aexpr/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affyhgu133aexpr/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affyhgu133aexpr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyhgu133aexpr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyhgu133aexpr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affyhgu133aexpr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affyhgu133aexpr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affyhgu133aexpr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affyhgu133aexpr

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