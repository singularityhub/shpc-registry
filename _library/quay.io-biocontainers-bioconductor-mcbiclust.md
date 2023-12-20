---
layout: container
name:  "quay.io/biocontainers/bioconductor-mcbiclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mcbiclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mcbiclust/container.yaml"
updated_at: "2023-12-20 03:23:01.465357"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mcbiclust"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mcbiclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mcbiclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mcbiclust", "latest": {"1.24.0--r43hdfd78af_0": "sha256:4bd334d05dba584d2f0fc5207b6859c4a2f071186da4c5db0af1202a1601db5a"}, "tags": {"1.8.0--r36_1": "sha256:e07a66a816f36d4ebe38f3606aeb130401d420f4c485f485e92e74bb7fd99c60", "1.18.0--r41hdfd78af_0": "sha256:d392dda22d36fb05b508bbf17cabc10abd3b5c12f7e32d2d0613dd88dcce0dff", "1.16.0--r41hdfd78af_0": "sha256:e1f1224cb68e5f56a163e9a3eb3e4bb9d36e074d91a1796e5c2b5a2195fe12fa", "1.14.0--r40hdfd78af_1": "sha256:4e9f61f68c44e12e2c11edc03ceff6803c5b6d1e4c6459b14626d90c960c4585", "1.12.0--r40_0": "sha256:6d349b59306f38d1b3c4d18ed50f000be4be056d1fe41eec54bf8ac26553d48a", "1.10.0--r36_0": "sha256:95d7d6a2915ae26e3617387725c6ae7def06c52a4464e6657958f7bc30c6863a", "1.22.0--r42hdfd78af_0": "sha256:1d74e11587d2126bc0f020c3f913223c2292f21b3a75069d3ff41f681727e7df", "1.24.0--r43hdfd78af_0": "sha256:4bd334d05dba584d2f0fc5207b6859c4a2f071186da4c5db0af1202a1601db5a"}, "docker": "quay.io/biocontainers/bioconductor-mcbiclust", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mcbiclust.
shpc-registry automated BioContainers addition for bioconductor-mcbiclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mcbiclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mcbiclust:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mcbiclust/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mcbiclust/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mcbiclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mcbiclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mcbiclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mcbiclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mcbiclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mcbiclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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