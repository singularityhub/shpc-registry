---
layout: container
name:  "quay.io/biocontainers/bioconductor-setools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-setools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-setools/container.yaml"
updated_at: "2025-09-11 05:33:21.354543"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-setools"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-setools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-setools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-setools", "latest": {"1.20.0--r44hdfd78af_0": "sha256:fd16589bd92f316a112d8ca5811583f3ad55756ed2bf2697511924675cc03b28"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:ec2fe894331d6332c07cbc937e8e5cc140eebe3bc078204fcc6c97520b9b0bb3", "1.12.0--r42hdfd78af_0": "sha256:92014ab2b468162c918074daeda5f7cb915f30c5838f96728b03d0ce8a66eead", "1.14.0--r43hdfd78af_0": "sha256:c45ec5ba47f3faf81c733f01ddf9df4db6ca9af2bdd9c59b538ce2fb668fcfca", "1.16.0--r43hdfd78af_0": "sha256:be6939743499f6e6e5e00d427d8cc145f4dec74ccf10ab5643b4aa156ce649c2", "1.20.0--r44hdfd78af_0": "sha256:fd16589bd92f316a112d8ca5811583f3ad55756ed2bf2697511924675cc03b28"}, "docker": "quay.io/biocontainers/bioconductor-setools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-setools.
shpc-registry automated BioContainers addition for bioconductor-setools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-setools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-setools:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-setools/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-setools/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-setools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-setools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-setools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-setools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-setools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-setools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-setools

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