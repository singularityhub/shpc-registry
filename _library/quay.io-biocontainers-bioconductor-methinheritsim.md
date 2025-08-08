---
layout: container
name:  "quay.io/biocontainers/bioconductor-methinheritsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methinheritsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methinheritsim/container.yaml"
updated_at: "2025-08-08 04:29:15.735417"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methinheritsim"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methinheritsim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methinheritsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methinheritsim", "latest": {"1.28.0--r44hdfd78af_0": "sha256:db519fa53f808bd2be223e7f85c13495a436c6d6bfb1dca1d09da85b85eb46b4"}, "tags": {"1.8.0--r36_0": "sha256:ebe6a6996cea43d4054c7e529970c89bd3b9ff48847f3ec9382434b1b1226cb2", "1.20.0--r42hdfd78af_0": "sha256:38cdfdf1c617f2fe37d5cf2b5f6aa865b4a3a2bac325766a16a1055b7652a9f0", "1.16.0--r41hdfd78af_0": "sha256:ba8e869d560999a9373a1173b365a3372ea883c853bffc95b469e3649848f2c2", "1.14.0--r41hdfd78af_0": "sha256:bda8c47ee91a6b1388ca1d9fef04084d03417b40affebfc5776cf05c318b5587", "1.12.0--r40hdfd78af_1": "sha256:c0d94fb43fadbe67c08b413bbec5d258c068add230a12775041cae7689c05ba1", "1.10.0--r40_0": "sha256:d9e50c9b3da3b8aaf8cbae0da8c9697fca7ddba88288838fdafe8f770830858f", "1.22.0--r43hdfd78af_0": "sha256:c5abc158f545884f44ad82aa4b165b4c5bb0605f1c52ce13764b2e31730f5c76", "1.24.0--r43hdfd78af_0": "sha256:0d3e5f7c94b28d87b4f5400fc616e14cf2cbcdbf21de4db7d5de86ebe52476d1", "1.28.0--r44hdfd78af_0": "sha256:db519fa53f808bd2be223e7f85c13495a436c6d6bfb1dca1d09da85b85eb46b4"}, "docker": "quay.io/biocontainers/bioconductor-methinheritsim", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methinheritsim.
shpc-registry automated BioContainers addition for bioconductor-methinheritsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methinheritsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methinheritsim:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methinheritsim/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methinheritsim/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methinheritsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methinheritsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methinheritsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methinheritsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methinheritsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methinheritsim-inspect-deffile:

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