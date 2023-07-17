---
layout: container
name:  "quay.io/biocontainers/bioconductor-clomial"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clomial/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clomial/container.yaml"
updated_at: "2023-07-17 04:12:36.190590"
latest: "1.34.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clomial"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clomial"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clomial", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clomial", "latest": {"1.34.0--r42hdfd78af_0": "sha256:b0e237cc75e4afb0552a6a19d3ab2f387ae963d68403ebb5c4df80b6842a3f16"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:26d7d2d3b6d8b3a46ab2c600964fb7f66fe316c9d710880c85cf20085017592d", "1.34.0--r42hdfd78af_0": "sha256:b0e237cc75e4afb0552a6a19d3ab2f387ae963d68403ebb5c4df80b6842a3f16"}, "docker": "quay.io/biocontainers/bioconductor-clomial"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clomial.
shpc-registry automated BioContainers addition for bioconductor-clomial
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clomial
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clomial:1.34.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clomial/1.34.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clomial/1.34.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clomial-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clomial-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clomial-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clomial-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clomial-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clomial-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clomial

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