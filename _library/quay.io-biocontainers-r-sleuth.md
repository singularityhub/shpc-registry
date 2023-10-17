---
layout: container
name:  "quay.io/biocontainers/r-sleuth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sleuth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sleuth/container.yaml"
updated_at: "2023-10-17 02:49:48.105152"
latest: "0.30.1--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-sleuth"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.30.0--r41hdfd78af_5"
 - "0.30.1--r42hdfd78af_0"
 - "0.30.1--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-sleuth"
config: {"url": "https://biocontainers.pro/tools/r-sleuth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sleuth", "latest": {"0.30.1--r43hdfd78af_1": "sha256:f3b645a5cdcb2c6b113be9c7cb265bf91045d3e2dd8f62975798419fa844e347"}, "tags": {"0.30.0--r41hdfd78af_5": "sha256:6190232787b5fc4080eb23570cbb56edfaa29a8fb011a56659dfe04db96a8fe4", "0.30.1--r42hdfd78af_0": "sha256:687c3847f46f607bcd1d942ad600006e6efbbcae58d7d513d61225e2196615ac", "0.30.1--r43hdfd78af_1": "sha256:f3b645a5cdcb2c6b113be9c7cb265bf91045d3e2dd8f62975798419fa844e347"}, "docker": "quay.io/biocontainers/r-sleuth", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sleuth.
shpc-registry automated BioContainers addition for r-sleuth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sleuth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sleuth:0.30.1--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sleuth/0.30.1--r43hdfd78af_1
$ module help quay.io/biocontainers/r-sleuth/0.30.1--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sleuth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sleuth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sleuth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sleuth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sleuth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sleuth-inspect-deffile:

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