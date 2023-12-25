---
layout: container
name:  "quay.io/biocontainers/bioconductor-dama"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dama/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dama/container.yaml"
updated_at: "2023-12-25 02:54:15.212643"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dama"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dama"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dama", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dama", "latest": {"1.74.0--r43hdfd78af_0": "sha256:dde39e19e279a8d62e686e37f3d2543b87db9e8018bb0aecba5737d822d6fa39"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:5538621d1dd4e6a27f6a89e24d7f6c04d970ebe66f36f300334731e037801a48", "1.70.0--r42hdfd78af_0": "sha256:c135414007bd676ca5094beaceed4d80c42141ab80e825907b44c2f956fef5ae", "1.72.0--r43hdfd78af_0": "sha256:f6063e6289ef8a03588f1e1bd9afd6399c5230ccfaa8ac3e2ed54f4646d2ba63", "1.74.0--r43hdfd78af_0": "sha256:dde39e19e279a8d62e686e37f3d2543b87db9e8018bb0aecba5737d822d6fa39"}, "docker": "quay.io/biocontainers/bioconductor-dama"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dama.
shpc-registry automated BioContainers addition for bioconductor-dama
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dama
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dama:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dama/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dama/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dama-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dama-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dama-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dama-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dama-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dama-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dama

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