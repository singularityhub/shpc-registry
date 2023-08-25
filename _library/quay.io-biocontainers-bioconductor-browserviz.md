---
layout: container
name:  "quay.io/biocontainers/bioconductor-browserviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-browserviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-browserviz/container.yaml"
updated_at: "2023-08-25 02:40:37.105874"
latest: "2.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-browserviz"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_0"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_1"
 - "2.10.0--r40_0"
 - "2.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-browserviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-browserviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-browserviz", "latest": {"2.22.0--r43hdfd78af_0": "sha256:89254d97bc5f96b272bd59b9f4200dca5a4050c5f73d4d79fcf16a5a29f68b24"}, "tags": {"2.8.0--r36_0": "sha256:eb8f0b2e7dece73aa89d9f8833eb7cae9c67273a94cb233b982a577df3700e89", "2.20.0--r42hdfd78af_0": "sha256:3b5760f07d154039ec3b77180b5b56d21a1233f7068caa63d172a463f0607a26", "2.16.0--r41hdfd78af_0": "sha256:6effce5687894620637c8b14ec289b5575521a4278feb9cbdcfc914d3dd98c61", "2.12.0--r40hdfd78af_1": "sha256:6d2979789295edf633e20ab7b876ce31acc91f7138334fce8ccdf46b1ee7bd42", "2.10.0--r40_0": "sha256:a26bd550294d83e409037b231a82ece65c01bff3152bb4607b8dc0f67853e859", "2.22.0--r43hdfd78af_0": "sha256:89254d97bc5f96b272bd59b9f4200dca5a4050c5f73d4d79fcf16a5a29f68b24"}, "docker": "quay.io/biocontainers/bioconductor-browserviz", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-browserviz.
shpc-registry automated BioContainers addition for bioconductor-browserviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-browserviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-browserviz:2.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-browserviz/2.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-browserviz/2.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-browserviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-browserviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-browserviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-browserviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-browserviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-browserviz-inspect-deffile:

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