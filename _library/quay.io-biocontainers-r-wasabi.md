---
layout: container
name:  "quay.io/biocontainers/r-wasabi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-wasabi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-wasabi/container.yaml"
updated_at: "2024-12-17 03:55:11.753000"
latest: "1.0.1--r43hdfd78af_6"
container_url: "https://biocontainers.pro/tools/r-wasabi"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.1--r41hdfd78af_4"
 - "1.0.1--r42hdfd78af_5"
 - "1.0.1--r43hdfd78af_6"
description: "shpc-registry automated BioContainers addition for r-wasabi"
config: {"url": "https://biocontainers.pro/tools/r-wasabi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-wasabi", "latest": {"1.0.1--r43hdfd78af_6": "sha256:24abe2bcffbca698a6948165de4747ff224bb53f12ed646f65618e352d9a2e93"}, "tags": {"1.0.1--r41hdfd78af_4": "sha256:c475dbda694bef4031d2c966873456584f3732d61b18f6fb1f46d02df06fb987", "1.0.1--r42hdfd78af_5": "sha256:f2e9812a196b87ca475c6377ffbd4570a1707e26148f8f3093398b50e1c842db", "1.0.1--r43hdfd78af_6": "sha256:24abe2bcffbca698a6948165de4747ff224bb53f12ed646f65618e352d9a2e93"}, "docker": "quay.io/biocontainers/r-wasabi", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-wasabi.
shpc-registry automated BioContainers addition for r-wasabi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-wasabi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-wasabi:1.0.1--r43hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-wasabi/1.0.1--r43hdfd78af_6
$ module help quay.io/biocontainers/r-wasabi/1.0.1--r43hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-wasabi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-wasabi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-wasabi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-wasabi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-wasabi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-wasabi-inspect-deffile:

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