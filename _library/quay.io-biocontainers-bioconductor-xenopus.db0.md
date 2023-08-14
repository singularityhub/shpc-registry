---
layout: container
name:  "quay.io/biocontainers/bioconductor-xenopus.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xenopus.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xenopus.db0/container.yaml"
updated_at: "2023-08-14 02:54:30.130646"
latest: "3.17.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xenopus.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xenopus.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xenopus.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xenopus.db0", "latest": {"3.17.0--r43hdfd78af_0": "sha256:353d5514ec5475288c7af5608d511a4f8763e126f8ab62f82b62dd440dd090dd"}, "tags": {"3.8.2--r36_1": "sha256:9f8841c32eaedabe3730a3b994a0c7efdaf6a50ad9f928d5312cd59fdad70e43", "3.16.0--r42hdfd78af_0": "sha256:5087b86101a1e17d2d6e7fc3217e8fd5a7647b543674cafb841d1c928c01805e", "3.14.0--r41hdfd78af_1": "sha256:ddcbd59e8ecc1365c047a378af40ad11a8dc7c866aebe64a42e66a678d3e9f15", "3.13.0--r41hdfd78af_0": "sha256:7cedd90b5ded499adca5e3a2b6a906a9f51f2f804a536459e0c04e77b293f6c9", "3.12.0--r40hdfd78af_1": "sha256:4f20a23a5fab42a94b58e562a87f77cc90513a89226866002290f604565328da", "3.11.2--r40_0": "sha256:3591f1b157e15b2668f5279b965864337ccea69177a3a55bfe28baa7efda9e18", "3.17.0--r43hdfd78af_0": "sha256:353d5514ec5475288c7af5608d511a4f8763e126f8ab62f82b62dd440dd090dd"}, "docker": "quay.io/biocontainers/bioconductor-xenopus.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xenopus.db0.
shpc-registry automated BioContainers addition for bioconductor-xenopus.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xenopus.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xenopus.db0:3.17.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xenopus.db0/3.17.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-xenopus.db0/3.17.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xenopus.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xenopus.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xenopus.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xenopus.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xenopus.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xenopus.db0-inspect-deffile:

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