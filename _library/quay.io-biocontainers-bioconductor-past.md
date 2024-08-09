---
layout: container
name:  "quay.io/biocontainers/bioconductor-past"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-past/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-past/container.yaml"
updated_at: "2024-08-09 03:27:14.537741"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-past"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-past"
config: {"url": "https://biocontainers.pro/tools/bioconductor-past", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-past", "latest": {"1.18.0--r43hdfd78af_0": "sha256:bd622c43c8d36476118d971306688d76fd855b31a370b1c771fa73fc84c392df"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:034278a81015a15a67ec9bf15e2f0e60da0a064edb0aff2ba8cb0e36731ee184", "1.14.0--r42hdfd78af_0": "sha256:1a88516f3ee4ba9ec703819af254c3a98507d71970dda935c8158f9d33b3a55a", "1.10.0--r41hdfd78af_0": "sha256:a0f0e12137bfe99aef78bc885d4a7d0933d2ece395edd84771764f600ca72281", "1.16.0--r43hdfd78af_0": "sha256:c59043d5b065a22b45d17fef139c9725c28b9e809d661a587d7a2ba6e6715279", "1.18.0--r43hdfd78af_0": "sha256:bd622c43c8d36476118d971306688d76fd855b31a370b1c771fa73fc84c392df"}, "docker": "quay.io/biocontainers/bioconductor-past", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-past.
shpc-registry automated BioContainers addition for bioconductor-past
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-past
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-past:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-past/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-past/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-past-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-past-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-past-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-past-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-past-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-past-inspect-deffile:

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