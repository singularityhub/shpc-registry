---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74av2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74av2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74av2cdf/container.yaml"
updated_at: "2023-09-04 03:56:52.777519"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74av2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74av2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74av2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74av2cdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:02f3759db36dc60654e126f3f2f7dd1b8c85fdd2123f977f5d1d54e046c70d2a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:7b9f0d7bb792e74bc892cadd8315b85a84b0d51b8e61cc81e87bc52cacf4e308", "2.18.0--r42hdfd78af_10": "sha256:02f3759db36dc60654e126f3f2f7dd1b8c85fdd2123f977f5d1d54e046c70d2a"}, "docker": "quay.io/biocontainers/bioconductor-mgu74av2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74av2cdf.
shpc-registry automated BioContainers addition for bioconductor-mgu74av2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74av2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74av2cdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74av2cdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-mgu74av2cdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74av2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74av2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74av2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74av2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74av2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74av2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74av2cdf

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