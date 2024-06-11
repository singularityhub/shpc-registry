---
layout: container
name:  "quay.io/biocontainers/r-pctgcdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pctgcdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pctgcdata/container.yaml"
updated_at: "2024-06-11 05:17:18.132170"
latest: "0.3.0--r43h9ee0642_4"
container_url: "https://biocontainers.pro/tools/r-pctgcdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.3.0--r41h9ee0642_2"
 - "0.3.0--r42h9ee0642_3"
 - "0.3.0--r43h9ee0642_4"
description: "shpc-registry automated BioContainers addition for r-pctgcdata"
config: {"url": "https://biocontainers.pro/tools/r-pctgcdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-pctgcdata", "latest": {"0.3.0--r43h9ee0642_4": "sha256:d3e4d47aa33201cebdf6889f2c6be59dbd737017b332436aa79ef4bb2734b5da"}, "tags": {"0.3.0--r41h9ee0642_2": "sha256:9645f369bc68715dfde8b2ce507e01cbfc2c0f7c030cb5578445676a18473991", "0.3.0--r42h9ee0642_3": "sha256:d198c5876be29e615eff5273d83a0ca7ff5428c589428f145379b857001391f9", "0.3.0--r43h9ee0642_4": "sha256:d3e4d47aa33201cebdf6889f2c6be59dbd737017b332436aa79ef4bb2734b5da"}, "docker": "quay.io/biocontainers/r-pctgcdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pctgcdata.
shpc-registry automated BioContainers addition for r-pctgcdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pctgcdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pctgcdata:0.3.0--r43h9ee0642_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pctgcdata/0.3.0--r43h9ee0642_4
$ module help quay.io/biocontainers/r-pctgcdata/0.3.0--r43h9ee0642_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pctgcdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pctgcdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pctgcdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pctgcdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pctgcdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pctgcdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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