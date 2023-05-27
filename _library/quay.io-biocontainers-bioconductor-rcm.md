---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcm/container.yaml"
updated_at: "2023-05-27 02:42:59.887606"
latest: "1.14.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcm"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcm", "latest": {"1.14.0--r42hdfd78af_0": "sha256:6262c0267014dfc5a86f9c72e31270c8a37cb212a7f8ba92f11537cf57430f46"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:263433e17b0cddcf498a4a2fb5c5c057772a5d38dd34ac07a03bf390e414972c", "1.10.0--r41hdfd78af_0": "sha256:fd8d5378df940bc50f974f4df5be7246fe05ae5a914a5f17a07c6d0cc98e391a", "1.14.0--r42hdfd78af_0": "sha256:6262c0267014dfc5a86f9c72e31270c8a37cb212a7f8ba92f11537cf57430f46"}, "docker": "quay.io/biocontainers/bioconductor-rcm", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcm.
shpc-registry automated BioContainers addition for bioconductor-rcm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcm:1.14.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcm/1.14.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcm/1.14.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcm-inspect-deffile:

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