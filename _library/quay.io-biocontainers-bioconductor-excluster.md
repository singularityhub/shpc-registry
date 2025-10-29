---
layout: container
name:  "quay.io/biocontainers/bioconductor-excluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-excluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-excluster/container.yaml"
updated_at: "2025-10-29 03:56:54.531109"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-excluster"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-excluster"
config: {"url": "https://biocontainers.pro/tools/bioconductor-excluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-excluster", "latest": {"1.24.0--r44hdfd78af_0": "sha256:e777b718683be0e5ae4f730698b6120fde67281b6304009ab3677768ee9e3f46"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:693874ace269138376d5ccbf52b092859c749abbae99a13729db0774e05932fb", "1.16.0--r42hdfd78af_0": "sha256:c65ef281330c9f63e60b390f834f096294698adc6300e213a17623d0758e2d55", "1.12.0--r41hdfd78af_0": "sha256:6380dc978f4ca7a9fc2ea2f09b839de1dbc6a12f67a1a00cbb53a2bf6a74b25b", "1.10.0--r41hdfd78af_0": "sha256:50a4347c8d51b2f710991cb9b9008663bb35937c239e0d457f580df33eee5da4", "1.18.0--r43hdfd78af_0": "sha256:f65a944878310afa6d5c4ec5d72d20efd90b7d8367760d744a6f70c9352b18e7", "1.20.0--r43hdfd78af_0": "sha256:9531a798091492afda44ccaab74f2fa027574bf2f80762930c5c36f6a0cd9c36", "1.24.0--r44hdfd78af_0": "sha256:e777b718683be0e5ae4f730698b6120fde67281b6304009ab3677768ee9e3f46"}, "docker": "quay.io/biocontainers/bioconductor-excluster", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-excluster.
shpc-registry automated BioContainers addition for bioconductor-excluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-excluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-excluster:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-excluster/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-excluster/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-excluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-excluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-excluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-excluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-excluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-excluster-inspect-deffile:

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