---
layout: container
name:  "quay.io/biocontainers/bioconductor-wrench"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-wrench/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-wrench/container.yaml"
updated_at: "2024-03-13 02:52:42.544842"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-wrench"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-wrench"
config: {"url": "https://biocontainers.pro/tools/bioconductor-wrench", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-wrench", "latest": {"1.20.0--r43hdfd78af_0": "sha256:15e5adb53cb2e17536695ec38b811fb650a3e413ebf904bc28a69837bfdc4042"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:af5b9eee8db39b7e4fcee50f87e3e34ab81596582aeb60d6247877732181794b", "1.16.0--r42hdfd78af_0": "sha256:98a2bfd15aba33a714b8bee66879dda5ed30e2bb3b6a5b76615f2e6f09a1e34d", "1.12.0--r41hdfd78af_0": "sha256:a24cf5a0bd9202dae56e7f735f2802de6ad10d6d343855f5ee2b99c672b0417b", "1.10.0--r41hdfd78af_0": "sha256:199c071acf8c4c38317845970cedd0e6e977c7db2fa4d4ffcab528af4ac88f9e", "1.18.0--r43hdfd78af_0": "sha256:11f3bffa02a96629a9f28d8ee445b6d91f37e4e2440ee23105d971a3d09c6c62", "1.20.0--r43hdfd78af_0": "sha256:15e5adb53cb2e17536695ec38b811fb650a3e413ebf904bc28a69837bfdc4042"}, "docker": "quay.io/biocontainers/bioconductor-wrench", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-wrench.
shpc-registry automated BioContainers addition for bioconductor-wrench
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-wrench
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-wrench:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-wrench/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-wrench/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-wrench-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wrench-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wrench-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-wrench-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-wrench-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-wrench-inspect-deffile:

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