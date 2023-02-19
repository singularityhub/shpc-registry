---
layout: container
name:  "quay.io/biocontainers/bioconductor-frmatools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-frmatools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-frmatools/container.yaml"
updated_at: "2023-02-19 03:33:02.293445"
latest: "1.50.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-frmatools"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-frmatools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-frmatools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-frmatools", "latest": {"1.50.0--r42hdfd78af_0": "sha256:ea437aba6cc393f1f62b488d23f12324c209c2fbc6eaa8c3474d5d00b2223879"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:568b8a453f6f91450c4e2eb78b162a10046113515daa126afb3028eff696018c", "1.50.0--r42hdfd78af_0": "sha256:ea437aba6cc393f1f62b488d23f12324c209c2fbc6eaa8c3474d5d00b2223879"}, "docker": "quay.io/biocontainers/bioconductor-frmatools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-frmatools.
shpc-registry automated BioContainers addition for bioconductor-frmatools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-frmatools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-frmatools:1.50.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-frmatools/1.50.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-frmatools/1.50.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-frmatools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frmatools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frmatools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-frmatools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-frmatools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-frmatools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-frmatools

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