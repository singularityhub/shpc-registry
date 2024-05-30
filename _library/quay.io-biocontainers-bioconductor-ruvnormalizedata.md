---
layout: container
name:  "quay.io/biocontainers/bioconductor-ruvnormalizedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ruvnormalizedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ruvnormalizedata/container.yaml"
updated_at: "2024-05-30 04:44:24.358254"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ruvnormalizedata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "c89"
 - "c99"
versions:
 - "1.9.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_2"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ruvnormalizedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ruvnormalizedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ruvnormalizedata", "latest": {"1.22.0--r43hdfd78af_0": "sha256:f24ce0985e8c5700c201d37897bfe61fbd45697d0abe87f93da06e38c7e407f1"}, "tags": {"1.9.0--r40_0": "sha256:4b15987c70b5671eeadabaf0c3ebd13791d861887572b665502f4bf6d6ee4455", "1.18.0--r42hdfd78af_0": "sha256:badc5587f31d6fa7baf3952eb831e9caba98faa79dabb1ad070319b7f06da27a", "1.14.0--r41hdfd78af_1": "sha256:5bbb3805bd6f68b86814eebc9c93a8dbb924a1aa6bd179aa521ae0662a1a0405", "1.12.0--r41hdfd78af_0": "sha256:33ac9c2eb64ffa6bda4316088c420deaa442a523bddcf1bed099c590ace5940b", "1.10.0--r40hdfd78af_2": "sha256:ac61c3c2208f6f95737b17e8817aed786036deac5d715f97a13dabc7db1548a5", "1.20.0--r43hdfd78af_0": "sha256:beb38022344f57562bea232bb7929b1276483968b3b43feb6db20909b3536ee4", "1.22.0--r43hdfd78af_0": "sha256:f24ce0985e8c5700c201d37897bfe61fbd45697d0abe87f93da06e38c7e407f1"}, "docker": "quay.io/biocontainers/bioconductor-ruvnormalizedata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ruvnormalizedata.
shpc-registry automated BioContainers addition for bioconductor-ruvnormalizedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ruvnormalizedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ruvnormalizedata:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ruvnormalizedata/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ruvnormalizedata/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ruvnormalizedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ruvnormalizedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ruvnormalizedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ruvnormalizedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ruvnormalizedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ruvnormalizedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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