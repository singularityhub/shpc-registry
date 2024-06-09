---
layout: container
name:  "quay.io/biocontainers/bioconductor-gwasurvivr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gwasurvivr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gwasurvivr/container.yaml"
updated_at: "2024-06-09 03:14:08.415497"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gwasurvivr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gwasurvivr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gwasurvivr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gwasurvivr", "latest": {"1.20.0--r43hdfd78af_0": "sha256:bd980d97404d2c88e3b42eeaae467dce53be986b70654359f0b5f6193837e96e"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:b785e7a00fc9992cf568d2e5cc2c0527f24293614cd7173f72f1c0ff3ee0a32f", "1.16.0--r42hdfd78af_0": "sha256:ec67b943b1c83b682fbf40b48978aefe97bb7db75a5d3c7d62505bf2c0cbf6be", "1.12.0--r41hdfd78af_0": "sha256:de529a1d2202f53a0149ccdae05fbbc9cec0af18c9a035052181a93874561df1", "1.10.0--r41hdfd78af_0": "sha256:8afe932e972ae29ccb82a90b9b72ea384d7027a395d0900b4b90acc45732052a", "1.18.0--r43hdfd78af_0": "sha256:3206ae383f89b837722a68f5854697415947dd17b97d337347333c7df68b0854", "1.20.0--r43hdfd78af_0": "sha256:bd980d97404d2c88e3b42eeaae467dce53be986b70654359f0b5f6193837e96e"}, "docker": "quay.io/biocontainers/bioconductor-gwasurvivr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gwasurvivr.
shpc-registry automated BioContainers addition for bioconductor-gwasurvivr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gwasurvivr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gwasurvivr:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gwasurvivr/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gwasurvivr/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gwasurvivr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gwasurvivr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gwasurvivr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gwasurvivr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gwasurvivr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gwasurvivr-inspect-deffile:

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