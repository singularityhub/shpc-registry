---
layout: container
name:  "quay.io/biocontainers/bioconductor-sights"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sights/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sights/container.yaml"
updated_at: "2024-07-21 03:18:20.917913"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sights"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sights"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sights", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sights", "latest": {"1.28.0--r43hdfd78af_0": "sha256:7bf39acaf0152ccc6ee30b007a85499c0abfb95232fb818b2cde7d36d55ea0d6"}, "tags": {"1.8.1--r351_0": "sha256:e38d89c641d36ad9272e5f12b6a91255230602caa3b5e4c430387191c85b28f1", "1.24.0--r42hdfd78af_0": "sha256:ea47e6b15eddc8f2a7c14abc58d9dfa6b16ecc9ee2ddf7d93dba3cc4f79abdec", "1.20.0--r41hdfd78af_0": "sha256:af9f04e124b09310a2b0fc037e6b908e2d093814e58eb48dbd0735c2e37c2d05", "1.18.0--r41hdfd78af_0": "sha256:5099145b74cd2e7eb4040eefb6bda019ab5bc4a756df7a45882f41a87bd27ed4", "1.16.0--r40hdfd78af_1": "sha256:de403c25b509823b592f3ef3b673f8a0ed0a6faaaaf831e9fd65ec659288c54b", "1.14.0--r40_0": "sha256:f70278485266dfede0cd679ee50892639ea365da8a196761435004374df56f5e", "1.26.0--r43hdfd78af_0": "sha256:b165a75ee2960e3288945005d5807ec9fd0c7ecbd7fd84a09c7d52588ab4a44f", "1.28.0--r43hdfd78af_0": "sha256:7bf39acaf0152ccc6ee30b007a85499c0abfb95232fb818b2cde7d36d55ea0d6"}, "docker": "quay.io/biocontainers/bioconductor-sights", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sights.
shpc-registry automated BioContainers addition for bioconductor-sights
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sights
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sights:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sights/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sights/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sights-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sights-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sights-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sights-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sights-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sights-inspect-deffile:

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