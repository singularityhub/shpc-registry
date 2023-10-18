---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86/container.yaml"
updated_at: "2023-10-18 02:33:47.613307"
latest: "2.99.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-ensdb.hsapiens.v86"

versions:
 - "2.99.0--r41hdfd78af_9"
 - "2.99.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-ensdb.hsapiens.v86"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensdb.hsapiens.v86", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensdb.hsapiens.v86", "latest": {"2.99.0--r42hdfd78af_10": "sha256:b7a0ed9dd27741ff50c3c7ef8329cbab15dac279185c8bbd6fdcf6cc25defea1"}, "tags": {"2.99.0--r41hdfd78af_9": "sha256:a41bf55d8ee3fb2d36f7eafd6c9f33822fde52a127e2c80239a4e50f7741a866", "2.99.0--r42hdfd78af_10": "sha256:b7a0ed9dd27741ff50c3c7ef8329cbab15dac279185c8bbd6fdcf6cc25defea1"}, "docker": "quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86.
shpc-registry automated BioContainers addition for bioconductor-ensdb.hsapiens.v86
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86:2.99.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86/2.99.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-ensdb.hsapiens.v86/2.99.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensdb.hsapiens.v86-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.hsapiens.v86-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.hsapiens.v86-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensdb.hsapiens.v86-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensdb.hsapiens.v86-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensdb.hsapiens.v86-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ensdb.hsapiens.v86

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