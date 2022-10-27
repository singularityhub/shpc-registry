---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtandem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtandem/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtandem/container.yaml"
updated_at: "2022-10-27 01:12:48.581564"
latest: "1.27.0--r40h1090f8d_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtandem"

versions:
 - "1.27.0--r40h1090f8d_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtandem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtandem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtandem", "latest": {"1.27.0--r40h1090f8d_0": "sha256:a1160e7eacde20ff86bfdf355e06e8a835bc59d40789c1f0479a51d8c9908d33"}, "tags": {"1.27.0--r40h1090f8d_0": "sha256:a1160e7eacde20ff86bfdf355e06e8a835bc59d40789c1f0479a51d8c9908d33"}, "docker": "quay.io/biocontainers/bioconductor-rtandem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtandem.
shpc-registry automated BioContainers addition for bioconductor-rtandem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtandem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtandem:1.27.0--r40h1090f8d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtandem/1.27.0--r40h1090f8d_0
$ module help quay.io/biocontainers/bioconductor-rtandem/1.27.0--r40h1090f8d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtandem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtandem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtandem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtandem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtandem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtandem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtandem

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