---
layout: container
name:  "quay.io/biocontainers/bioconductor-vulcan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vulcan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vulcan/container.yaml"
updated_at: "2024-01-20 03:04:15.109072"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vulcan"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vulcan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vulcan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vulcan", "latest": {"1.24.0--r43hdfd78af_0": "sha256:055a3ee58813caa5f880e9a979e1e17e25365521972ecca3012662ce3b42f2e2"}, "tags": {"1.8.0--r36_0": "sha256:dec800733e2d58db8d4888ea9ac8e2ca6dd09001f1d8873475e95f58a9b6e838", "1.20.0--r42hdfd78af_0": "sha256:48e303c264a5fa0416bf43e5e2eba76f86cacaaa0f5b3c4c9d076b594314897f", "1.16.0--r41hdfd78af_0": "sha256:98a2c25ce6312d7a0ea618228b7cea28b614181e6e739bc868205e8390bc529e", "1.14.0--r41hdfd78af_0": "sha256:29ab195df8a1d90cc4a0068cfcf9c331414b150fe08bf08c7355d0d1e6cc8255", "1.10.0--r40_0": "sha256:e316542d5ff5c62b2644ceda1b0af6d805b1158d0e9a7cf8a2f5f9be3ad2a046", "1.22.0--r43hdfd78af_0": "sha256:cc501f3ee3159717630b92826b261197ed1667547f2a261018ac21f3fc4f8a7b", "1.24.0--r43hdfd78af_0": "sha256:055a3ee58813caa5f880e9a979e1e17e25365521972ecca3012662ce3b42f2e2"}, "docker": "quay.io/biocontainers/bioconductor-vulcan", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vulcan.
shpc-registry automated BioContainers addition for bioconductor-vulcan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vulcan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vulcan:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vulcan/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-vulcan/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vulcan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vulcan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vulcan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vulcan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vulcan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vulcan-inspect-deffile:

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