---
layout: container
name:  "quay.io/biocontainers/r-r4cker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-r4cker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-r4cker/container.yaml"
updated_at: "2023-01-21 03:08:04.475740"
latest: "1.0--r42hdfd78af_4"
container_url: "https://biocontainers.pro/tools/r-r4cker"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0--r41hdfd78af_3"
 - "1.0--r42hdfd78af_4"
description: "shpc-registry automated BioContainers addition for r-r4cker"
config: {"url": "https://biocontainers.pro/tools/r-r4cker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-r4cker", "latest": {"1.0--r42hdfd78af_4": "sha256:1227e32d3e1c12124101e6a1bb9810f2230d17317e874536439726e51ce1e36b"}, "tags": {"1.0--r41hdfd78af_3": "sha256:c849bb82d1552fc0eb0ab5377b6e4a4a647c25b35c49f698cde7ea73337c9b3f", "1.0--r42hdfd78af_4": "sha256:1227e32d3e1c12124101e6a1bb9810f2230d17317e874536439726e51ce1e36b"}, "docker": "quay.io/biocontainers/r-r4cker", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-r4cker.
shpc-registry automated BioContainers addition for r-r4cker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-r4cker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-r4cker:1.0--r42hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-r4cker/1.0--r42hdfd78af_4
$ module help quay.io/biocontainers/r-r4cker/1.0--r42hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-r4cker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-r4cker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-r4cker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-r4cker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-r4cker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-r4cker-inspect-deffile:

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