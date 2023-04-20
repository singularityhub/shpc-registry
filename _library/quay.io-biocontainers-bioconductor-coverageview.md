---
layout: container
name:  "quay.io/biocontainers/bioconductor-coverageview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-coverageview/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-coverageview/container.yaml"
updated_at: "2023-04-20 03:00:39.404158"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-coverageview"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-coverageview"
config: {"url": "https://biocontainers.pro/tools/bioconductor-coverageview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-coverageview", "latest": {"1.36.0--r42hdfd78af_0": "sha256:21ccbf8040020bc6fad58e3e26df5a9f7004c8a6e225bed1ec301258427ec1e7"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:95b909085774e3081ca651927abc1359e86366f29bf4d326e54772101ab69ea8", "1.36.0--r42hdfd78af_0": "sha256:21ccbf8040020bc6fad58e3e26df5a9f7004c8a6e225bed1ec301258427ec1e7"}, "docker": "quay.io/biocontainers/bioconductor-coverageview"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-coverageview.
shpc-registry automated BioContainers addition for bioconductor-coverageview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-coverageview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-coverageview:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-coverageview/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-coverageview/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-coverageview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coverageview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coverageview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-coverageview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-coverageview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-coverageview-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-coverageview

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