---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtrmui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtrmui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtrmui/container.yaml"
updated_at: "2023-09-21 03:11:33.883358"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtrmui"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtrmui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtrmui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtrmui", "latest": {"1.38.0--r43hdfd78af_0": "sha256:213fc6dfa348a21a7adc1cd036e4e2a178ea0e88b7d2eb77d43c90050765f706"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:78fcf82d184877fc40e8a6d2ee7471197b317dc939af89c9dfd5d6d3088f4cfa", "1.36.0--r42hdfd78af_0": "sha256:2c38f0d3eff5ed0d0087e2d069616a25cddb656f4f3979894b6115ec109cab41", "1.38.0--r43hdfd78af_0": "sha256:213fc6dfa348a21a7adc1cd036e4e2a178ea0e88b7d2eb77d43c90050765f706"}, "docker": "quay.io/biocontainers/bioconductor-rtrmui"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtrmui.
shpc-registry automated BioContainers addition for bioconductor-rtrmui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtrmui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtrmui:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtrmui/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtrmui/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtrmui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtrmui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtrmui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtrmui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtrmui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtrmui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtrmui

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