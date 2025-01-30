---
layout: container
name:  "quay.io/biocontainers/bioconductor-quantro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-quantro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-quantro/container.yaml"
updated_at: "2025-01-30 03:59:48.666848"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-quantro"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-quantro"
config: {"url": "https://biocontainers.pro/tools/bioconductor-quantro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-quantro", "latest": {"1.40.0--r44hdfd78af_0": "sha256:b798859fa2bffb7f9667978f2824732522dbc75e8e29d5a03cedac6f6dd10421"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:2c7512c91d49682f57c12bb9204e8e5516483b4e37c40cc36edbf04182df5619", "1.32.0--r42hdfd78af_0": "sha256:20c9ab87d240884d3f0f81a88428e2b9d6ce19b1844c0aafb218e63067ff8a9d", "1.34.0--r43hdfd78af_0": "sha256:2d30116825891b9ff93a49bd6e3616e80e6dbe9825d3ace6c6bc75066ec98988", "1.36.0--r43hdfd78af_0": "sha256:eec5cbf9a9b62454e0ae08f021ecbceaea2fb7ac3b354f3768c01be2b5a50fb5", "1.40.0--r44hdfd78af_0": "sha256:b798859fa2bffb7f9667978f2824732522dbc75e8e29d5a03cedac6f6dd10421"}, "docker": "quay.io/biocontainers/bioconductor-quantro"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-quantro.
shpc-registry automated BioContainers addition for bioconductor-quantro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-quantro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-quantro:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-quantro/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-quantro/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-quantro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quantro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quantro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-quantro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-quantro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-quantro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-quantro

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