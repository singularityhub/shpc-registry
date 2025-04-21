---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocpkgtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocpkgtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocpkgtools/container.yaml"
updated_at: "2025-04-21 05:09:57.463324"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocpkgtools"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.2--r41hdfd78af_0"
 - "1.10.1--r41hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocpkgtools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocpkgtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocpkgtools", "latest": {"1.24.0--r44hdfd78af_0": "sha256:42984a3954407f8180006f9a7399bbeb31d88696b8c6d1e379f4eecf47a03a34"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:ecbc83a379477d4a85568dc85519909c88658dbec73432c8fb73c5dc6a6fd78c", "1.16.0--r42hdfd78af_0": "sha256:03024cab5b73d7f197dac31e27c3c9eb8c4cd46ac5c04991473339f1d513bfa4", "1.12.2--r41hdfd78af_0": "sha256:27bc1249bd8ec5f58868648f7d457d44da14f38a5e1e26024eacebd8baa1b4c5", "1.10.1--r41hdfd78af_0": "sha256:6c7076e10bc9a42a1d0a1b25394ceac05e1949d82ac09bac115816ae8c6c1e1d", "1.20.0--r43hdfd78af_0": "sha256:e7f614f32edba04103b015e9a8952ba28fc1a93e3325edb79fb6392681f885ad", "1.24.0--r44hdfd78af_0": "sha256:42984a3954407f8180006f9a7399bbeb31d88696b8c6d1e379f4eecf47a03a34"}, "docker": "quay.io/biocontainers/bioconductor-biocpkgtools", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocpkgtools.
shpc-registry automated BioContainers addition for bioconductor-biocpkgtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocpkgtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocpkgtools:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocpkgtools/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocpkgtools/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocpkgtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocpkgtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocpkgtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocpkgtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocpkgtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocpkgtools-inspect-deffile:

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