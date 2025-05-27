---
layout: container
name:  "quay.io/biocontainers/bioconductor-roar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-roar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-roar/container.yaml"
updated_at: "2025-05-27 03:14:01.128855"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-roar"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-roar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-roar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-roar", "latest": {"1.42.0--r44hdfd78af_0": "sha256:281c6472f496e0c6d44027f7a7cbf1c5ab8feab5ad4aa503466e2931e7bd67d7"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:c00453adb121b1e24c5b48afa5f56d6de68323b52213e87b3e415050ef096b34", "1.34.0--r42hdfd78af_0": "sha256:5306d4d08553bffd97fac81b4680738d248ba70c9e3e1d04a3a456ea9c14b7ec", "1.36.0--r43hdfd78af_0": "sha256:3bb1e572b14b1fef2eca4e4ce8ac82dfc8a3cca7620379acb23d7eed7fb07021", "1.38.0--r43hdfd78af_0": "sha256:b834e595cd056cb53d80ff1e4d1d56ebf61b6cb5b2c6111507ff57e763353940", "1.42.0--r44hdfd78af_0": "sha256:281c6472f496e0c6d44027f7a7cbf1c5ab8feab5ad4aa503466e2931e7bd67d7"}, "docker": "quay.io/biocontainers/bioconductor-roar", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-roar.
shpc-registry automated BioContainers addition for bioconductor-roar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-roar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-roar:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-roar/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-roar/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-roar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-roar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-roar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-roar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-roar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-roar-inspect-deffile:

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