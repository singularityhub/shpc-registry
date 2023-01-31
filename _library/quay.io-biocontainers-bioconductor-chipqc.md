---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipqc/container.yaml"
updated_at: "2023-01-31 03:13:10.579210"
latest: "1.34.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipqc"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipqc", "latest": {"1.34.0--r42hdfd78af_0": "sha256:81df0405afa1374f0b27500d16417a60992fe91382c23745869033008ea4e71c"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:7231aedf5c9fd4a740daf85cc82687707b15890867de361154b9b493a349e7a5", "1.34.0--r42hdfd78af_0": "sha256:81df0405afa1374f0b27500d16417a60992fe91382c23745869033008ea4e71c"}, "docker": "quay.io/biocontainers/bioconductor-chipqc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipqc.
shpc-registry automated BioContainers addition for bioconductor-chipqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipqc:1.34.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipqc/1.34.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipqc/1.34.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chipqc

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