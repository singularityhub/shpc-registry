---
layout: container
name:  "quay.io/biocontainers/bioconductor-affyrnadegradation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affyrnadegradation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affyrnadegradation/container.yaml"
updated_at: "2023-03-05 03:12:12.809543"
latest: "1.44.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affyrnadegradation"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affyrnadegradation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affyrnadegradation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affyrnadegradation", "latest": {"1.44.0--r42hdfd78af_0": "sha256:021371172d8f2f69f7f98fb4b16b1fd40270dd1979609b2c76c38f42ad14bcf9"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:3edc7c31da6d298b7be496a2dab2e5403c475d0925cf32aa829a84380eede033", "1.44.0--r42hdfd78af_0": "sha256:021371172d8f2f69f7f98fb4b16b1fd40270dd1979609b2c76c38f42ad14bcf9"}, "docker": "quay.io/biocontainers/bioconductor-affyrnadegradation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affyrnadegradation.
shpc-registry automated BioContainers addition for bioconductor-affyrnadegradation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affyrnadegradation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affyrnadegradation:1.44.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affyrnadegradation/1.44.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affyrnadegradation/1.44.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affyrnadegradation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyrnadegradation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyrnadegradation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affyrnadegradation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affyrnadegradation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affyrnadegradation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affyrnadegradation

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