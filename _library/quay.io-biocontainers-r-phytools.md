---
layout: container
name:  "quay.io/biocontainers/r-phytools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-phytools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-phytools/container.yaml"
updated_at: "2024-10-19 02:59:45.494410"
latest: "0.6_99--r40h6115d3f_1"
container_url: "https://biocontainers.pro/tools/r-phytools"

versions:
 - "0.6_99--r40h6115d3f_1"
description: "shpc-registry automated BioContainers addition for r-phytools"
config: {"url": "https://biocontainers.pro/tools/r-phytools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-phytools", "latest": {"0.6_99--r40h6115d3f_1": "sha256:26932ea0465125e7e60ffcd6b62a93e06dc8ccca65592e5b992610a212220089"}, "tags": {"0.6_99--r40h6115d3f_1": "sha256:26932ea0465125e7e60ffcd6b62a93e06dc8ccca65592e5b992610a212220089"}, "docker": "quay.io/biocontainers/r-phytools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-phytools.
shpc-registry automated BioContainers addition for r-phytools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-phytools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-phytools:0.6_99--r40h6115d3f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-phytools/0.6_99--r40h6115d3f_1
$ module help quay.io/biocontainers/r-phytools/0.6_99--r40h6115d3f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-phytools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-phytools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-phytools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-phytools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-phytools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-phytools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-phytools

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