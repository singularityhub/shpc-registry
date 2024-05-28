---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqcombo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqcombo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqcombo/container.yaml"
updated_at: "2024-05-28 03:11:08.583654"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqcombo"
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
description: "shpc-registry automated BioContainers addition for bioconductor-seqcombo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqcombo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqcombo", "latest": {"1.24.0--r43hdfd78af_0": "sha256:5b11805017572e680173beaa7a92fd097643e2cfd5ca113eb7a31a75674bdbba"}, "tags": {"1.8.0--r36_0": "sha256:81f5724e630544521629ffe77a6ae164183ff8c1cb4f7f74b23c1278e506a508", "1.20.0--r42hdfd78af_0": "sha256:7226fc7c131f38941ae3bdaaae7e96d4adcc2ae4f5dc13a31d067046a49028ea", "1.16.0--r41hdfd78af_0": "sha256:c1d604dfe20dcd66b8342324739bbaf1c29dbec62d686fc7e010f701407d9874", "1.14.0--r41hdfd78af_0": "sha256:84f81a0eb5bd44d0e00d1178f39a35c8fda78c022f322fed326a888cb4131e85", "1.12.0--r40hdfd78af_1": "sha256:a835020466119f0694faae06d65ab8a43d92a13fbd9284e93a297afd827d1042", "1.10.0--r40_0": "sha256:77278b6d19eb12e0d82385845226c096da5ae248eddd02427e8459ac3d27f139", "1.22.0--r43hdfd78af_0": "sha256:706be535d8812d67d350767f8dd474691046774c82bd9572f3f94dfe41270cf2", "1.24.0--r43hdfd78af_0": "sha256:5b11805017572e680173beaa7a92fd097643e2cfd5ca113eb7a31a75674bdbba"}, "docker": "quay.io/biocontainers/bioconductor-seqcombo", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqcombo.
shpc-registry automated BioContainers addition for bioconductor-seqcombo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcombo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcombo:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqcombo/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqcombo/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqcombo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcombo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcombo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqcombo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqcombo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqcombo-inspect-deffile:

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