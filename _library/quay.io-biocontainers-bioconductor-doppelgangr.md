---
layout: container
name:  "quay.io/biocontainers/bioconductor-doppelgangr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-doppelgangr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-doppelgangr/container.yaml"
updated_at: "2022-11-03 00:39:24.006886"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-doppelgangr"

versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-doppelgangr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-doppelgangr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-doppelgangr", "latest": {"1.8.0--r351_0": "sha256:bc2522a6097dbcc735d6703002f61280f071be33cdd6050dbae8ee0e7c9bfd94"}, "tags": {"1.8.0--r351_0": "sha256:bc2522a6097dbcc735d6703002f61280f071be33cdd6050dbae8ee0e7c9bfd94"}, "docker": "quay.io/biocontainers/bioconductor-doppelgangr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-doppelgangr.
shpc-registry automated BioContainers addition for bioconductor-doppelgangr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-doppelgangr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-doppelgangr:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-doppelgangr/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-doppelgangr/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-doppelgangr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-doppelgangr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-doppelgangr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-doppelgangr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-doppelgangr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-doppelgangr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-doppelgangr

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