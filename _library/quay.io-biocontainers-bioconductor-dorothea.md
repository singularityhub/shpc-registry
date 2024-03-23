---
layout: container
name:  "quay.io/biocontainers/bioconductor-dorothea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dorothea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dorothea/container.yaml"
updated_at: "2024-03-23 02:41:10.782312"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dorothea"

versions:
 - "1.6.0--r41hdfd78af_1"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dorothea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dorothea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dorothea", "latest": {"1.14.0--r43hdfd78af_0": "sha256:b331cf7a529352f8286adfa85ffbd9e234dca5f71a0d33ae48fc0688704fc749"}, "tags": {"1.6.0--r41hdfd78af_1": "sha256:e9f6245e6c70212bdb4595e7941cf7cab1fe35f32dfd88cd68d4bcdf42ff7ac1", "1.10.0--r42hdfd78af_0": "sha256:91908a4283ed88e49752c5c95d0556248761e1250b16b02e23a46e28d3f3adcb", "1.12.0--r43hdfd78af_0": "sha256:9a6c8b77a60be2254a830e40820a424d6069a49538578c36378d51d6b11bbf03", "1.14.0--r43hdfd78af_0": "sha256:b331cf7a529352f8286adfa85ffbd9e234dca5f71a0d33ae48fc0688704fc749"}, "docker": "quay.io/biocontainers/bioconductor-dorothea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dorothea.
shpc-registry automated BioContainers addition for bioconductor-dorothea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dorothea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dorothea:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dorothea/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dorothea/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dorothea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dorothea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dorothea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dorothea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dorothea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dorothea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dorothea

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