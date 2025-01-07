---
layout: container
name:  "quay.io/biocontainers/bioconductor-anf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anf/container.yaml"
updated_at: "2025-01-07 03:41:50.539847"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anf"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.13.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-anf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anf", "latest": {"1.28.0--r44hdfd78af_0": "sha256:272f2a24e40f4a863c8663bf58169863db046dd474905bc0ed58395dafc4379c"}, "tags": {"1.8.0--r36_0": "sha256:b424740cc517d537475f65bd4b39f2b9fedc5604c99e7bd10c7547575a718d3e", "1.20.0--r42hdfd78af_0": "sha256:945af4fb86a1368d469cc96f668e99e751649a7e75cdf0e2451cbef7ca3d7b01", "1.16.0--r41hdfd78af_0": "sha256:2273e38add583c5333b956d1d9c60e335e739e5116be33e5123dabb64eced26c", "1.13.0--r41hdfd78af_0": "sha256:570439ac75198fb517eb206a4e3f2b3b9fb686fd16a0fcda137608268451ce27", "1.12.0--r40hdfd78af_1": "sha256:2c72a4d8a333bd0f0aa007faebff725ad8dc8f9306c5fb6a3831f564b85bea05", "1.10.0--r40_0": "sha256:88af65098da5757a9166720e58338ba1845141949342d3a1296d8358d68c09bc", "1.22.0--r43hdfd78af_0": "sha256:02d99b575617684a862ce59091bebfa1d275759195a3e4c90ce4a1b1896bc3eb", "1.28.0--r44hdfd78af_0": "sha256:272f2a24e40f4a863c8663bf58169863db046dd474905bc0ed58395dafc4379c"}, "docker": "quay.io/biocontainers/bioconductor-anf", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anf.
shpc-registry automated BioContainers addition for bioconductor-anf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anf:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anf/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anf/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anf-inspect-deffile:

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