---
layout: container
name:  "quay.io/biocontainers/bioconductor-difflogo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-difflogo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-difflogo/container.yaml"
updated_at: "2024-05-30 04:41:42.983295"
latest: "2.26.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-difflogo"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.22.0--r42hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.11.0--r40_0"
 - "2.24.0--r43hdfd78af_0"
 - "2.26.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-difflogo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-difflogo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-difflogo", "latest": {"2.26.0--r43hdfd78af_1": "sha256:05fb38858c0bc3b04a1272585bf59f0abc72822c58983ec59ac234a139625d86"}, "tags": {"2.8.0--r36_1": "sha256:2fa21a4507faff14c778cc317ef76d29490339ebbfc0966bc744122a390c5249", "2.22.0--r42hdfd78af_0": "sha256:e7c8fdd165289f70c5443ea54c7b2f9abe37a5ba36cd9ca2a49b2f321a3e12b0", "2.18.0--r41hdfd78af_0": "sha256:a56d9732f4d6961a4071825f080f8a6456415cdec88be6f2d0d48a898c921843", "2.16.0--r41hdfd78af_0": "sha256:2a45f03963b62e1e6428d7b5db5c31018848e93bc241de785b75de1d47aa67f3", "2.14.0--r40hdfd78af_1": "sha256:8d8869ea6e22726579b90eae9cc4eee19b08f72f33dcb9d172a1ba3c4b1dab82", "2.11.0--r40_0": "sha256:9b6dfd9734f84230e2c977cd2d0537edf11297c95ae64300379d049a78cb1a33", "2.24.0--r43hdfd78af_0": "sha256:f233c77c1fd555a6e926dbf42d867e4b46d26470a95d6dff2988aead6d9d2244", "2.26.0--r43hdfd78af_1": "sha256:05fb38858c0bc3b04a1272585bf59f0abc72822c58983ec59ac234a139625d86"}, "docker": "quay.io/biocontainers/bioconductor-difflogo", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-difflogo.
shpc-registry automated BioContainers addition for bioconductor-difflogo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-difflogo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-difflogo:2.26.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-difflogo/2.26.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-difflogo/2.26.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-difflogo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-difflogo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-difflogo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-difflogo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-difflogo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-difflogo-inspect-deffile:

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