---
layout: container
name:  "quay.io/biocontainers/bioconductor-splinter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splinter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splinter/container.yaml"
updated_at: "2024-10-22 03:11:30.870289"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splinter"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splinter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splinter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splinter", "latest": {"1.28.0--r43hdfd78af_0": "sha256:57172f193bbc1b9fe3d2864b98170b9978db02e8c82df110ffe5c933bb9d063d"}, "tags": {"1.8.0--r351_0": "sha256:c38e403bf1229591653d70da2445fc0d56c9e8b1987f91f2415492a8fb3871a9", "1.20.0--r41hdfd78af_0": "sha256:ad008728365feb5816e826de1885ce8ad0438b30db2d38739ec01865ae34949f", "1.18.0--r41hdfd78af_0": "sha256:1f9b8e7eed0db1d248195bbe9343633c6c680c507ec0a06049b01cb214460521", "1.16.0--r40hdfd78af_1": "sha256:45f6342d17068c1a2f8acee83651a332ac06aaecd477043d18ba740ee7f11fdb", "1.14.0--r40_0": "sha256:435ec40960c26aa7947c55a2177e7d5d0508519656b7ae59c7331e12c9d9f412", "1.12.0--r36_0": "sha256:2bd0a4d1d8fece539482910e65a50d9b5d5ea9f8be8fe048ebd07305e2d00f5f", "1.24.0--r42hdfd78af_0": "sha256:06e01d64a0ac949eb2a1fad87f7152cadc7e815fc667df329f5e26d326f359ba", "1.26.0--r43hdfd78af_0": "sha256:78206912620dbfd360f1343c7ae51f595c189ced5f2edb68f986ac85ac04cfea", "1.28.0--r43hdfd78af_0": "sha256:57172f193bbc1b9fe3d2864b98170b9978db02e8c82df110ffe5c933bb9d063d"}, "docker": "quay.io/biocontainers/bioconductor-splinter", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splinter.
shpc-registry automated BioContainers addition for bioconductor-splinter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splinter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splinter:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splinter/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-splinter/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splinter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splinter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splinter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splinter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splinter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splinter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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