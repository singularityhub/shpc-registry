---
layout: container
name:  "quay.io/biocontainers/bioconductor-blimatestingdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-blimatestingdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-blimatestingdata/container.yaml"
updated_at: "2023-04-16 03:13:00.494308"
latest: "1.17.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-blimatestingdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-blimatestingdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-blimatestingdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-blimatestingdata", "latest": {"1.17.0--r42hdfd78af_0": "sha256:8d1a247e0f4f0b7393219b19729ee6ae0b2974091000dc6d26416da8920dfe7a"}, "tags": {"1.9.0--r40_0": "sha256:e49df655d63121d55ccb57e7725b0f4f5ccf83f14ea8b409b8e0499398947cc2", "1.17.0--r42hdfd78af_0": "sha256:8d1a247e0f4f0b7393219b19729ee6ae0b2974091000dc6d26416da8920dfe7a", "1.14.0--r41hdfd78af_1": "sha256:8976e75b6078c9ff1e95213fd4d531b0fe6fcfc191e459988e1e32b914702540", "1.12.0--r41hdfd78af_0": "sha256:a618b20908033aa4b83f5ab9fddc3cc6081904084161b94311a2a01b6fd2c1fe", "1.10.0--r40hdfd78af_1": "sha256:1d7818236eaa808f4430a97ca17be81bdc533f87e7848650f439d2439dac64b4"}, "docker": "quay.io/biocontainers/bioconductor-blimatestingdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-blimatestingdata.
shpc-registry automated BioContainers addition for bioconductor-blimatestingdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-blimatestingdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-blimatestingdata:1.17.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-blimatestingdata/1.17.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-blimatestingdata/1.17.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-blimatestingdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blimatestingdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blimatestingdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-blimatestingdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-blimatestingdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-blimatestingdata-inspect-deffile:

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