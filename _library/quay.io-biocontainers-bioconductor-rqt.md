---
layout: container
name:  "quay.io/biocontainers/bioconductor-rqt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rqt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rqt/container.yaml"
updated_at: "2023-05-16 03:10:17.537290"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rqt"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.19.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rqt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rqt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rqt", "latest": {"1.24.0--r42hdfd78af_0": "sha256:d76d9ca02e8a4f6d9608fa3c06a36816cb13bfad7f74ae4b1914deb5384a01de"}, "tags": {"1.8.0--r351_0": "sha256:35f270f2e3410f1de191a80e5b43210119c3600aff929ba78369d309edc4a2e5", "1.24.0--r42hdfd78af_0": "sha256:d76d9ca02e8a4f6d9608fa3c06a36816cb13bfad7f74ae4b1914deb5384a01de", "1.19.0--r41hdfd78af_0": "sha256:7d027c0d928be31929e962eec927ac01efe1b3daf43c957372022ddeba8386e1", "1.18.0--r41hdfd78af_0": "sha256:f5cf4c52d89c0b28968802b65de8018a3dd4755e7013d5503aa2127f5ea8bf31", "1.16.0--r40hdfd78af_1": "sha256:990c4aaf707d1386f7de92ba6c50d66c2008b2b44ddcd5900ee7d222d7bd6337", "1.14.0--r40_0": "sha256:922777ac2bbef25ce397f9fb8f3e037e5a8ed43c2299df279dbd0b6b1435688c"}, "docker": "quay.io/biocontainers/bioconductor-rqt", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rqt.
shpc-registry automated BioContainers addition for bioconductor-rqt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rqt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rqt:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rqt/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rqt/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rqt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rqt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rqt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rqt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rqt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rqt-inspect-deffile:

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