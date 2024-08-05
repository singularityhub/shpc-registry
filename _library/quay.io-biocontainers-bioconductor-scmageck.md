---
layout: container
name:  "quay.io/biocontainers/bioconductor-scmageck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scmageck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scmageck/container.yaml"
updated_at: "2024-08-05 04:03:48.676957"
latest: "1.9.1--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scmageck"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.9.1--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scmageck"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scmageck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scmageck", "latest": {"1.9.1--r42hdfd78af_0": "sha256:43fb973432382f62c38bbeba09c2dd25bccd909b1a00363882729d56360a0dee"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:bf1a5f421fa3201b282fde6312cdf9dda6487060da4d0f3a207bc37fde631adc", "1.9.1--r42hdfd78af_0": "sha256:43fb973432382f62c38bbeba09c2dd25bccd909b1a00363882729d56360a0dee"}, "docker": "quay.io/biocontainers/bioconductor-scmageck"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scmageck.
shpc-registry automated BioContainers addition for bioconductor-scmageck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scmageck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scmageck:1.9.1--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scmageck/1.9.1--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scmageck/1.9.1--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scmageck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scmageck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scmageck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scmageck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scmageck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scmageck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scmageck

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