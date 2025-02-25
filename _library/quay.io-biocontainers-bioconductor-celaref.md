---
layout: container
name:  "quay.io/biocontainers/bioconductor-celaref"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-celaref/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-celaref/container.yaml"
updated_at: "2025-02-25 03:33:41.944184"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-celaref"
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
description: "shpc-registry automated BioContainers addition for bioconductor-celaref"
config: {"url": "https://biocontainers.pro/tools/bioconductor-celaref", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-celaref", "latest": {"1.24.0--r44hdfd78af_0": "sha256:17f5910925e6db97763f978bd57ae81da8fddacd4c0e62388bcf954a04b4d9a3"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:64d3616ea70ba1d430d5be835ca3fb83564bc66cfb3c07da21801506f77beba2", "1.16.0--r42hdfd78af_0": "sha256:e06278d266dc91cbdb0f050d0f1d5edfa96b3b9e7248c02368e1c656c8a5c9f5", "1.12.0--r41hdfd78af_0": "sha256:658bea31c1ea8aa3e7dfb814129b47f118201a4d08f9340929ce18600006eb51", "1.10.0--r41hdfd78af_0": "sha256:d613d56a8bdc7a1d696956db04724cc5d0451d895b8375684aebd39275ff9cd5", "1.18.0--r43hdfd78af_0": "sha256:adf11843ff5bfa01494d3cec799ade75554530ac2250e3637238127529978e9a", "1.20.0--r43hdfd78af_0": "sha256:b2d39177bdd144379cea8601e2f264eaaf50fe59c0b5768dbd6b6a3f4307cda6", "1.24.0--r44hdfd78af_0": "sha256:17f5910925e6db97763f978bd57ae81da8fddacd4c0e62388bcf954a04b4d9a3"}, "docker": "quay.io/biocontainers/bioconductor-celaref", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-celaref.
shpc-registry automated BioContainers addition for bioconductor-celaref
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-celaref
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-celaref:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-celaref/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-celaref/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-celaref-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celaref-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celaref-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-celaref-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-celaref-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-celaref-inspect-deffile:

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