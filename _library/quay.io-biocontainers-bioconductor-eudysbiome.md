---
layout: container
name:  "quay.io/biocontainers/bioconductor-eudysbiome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eudysbiome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eudysbiome/container.yaml"
updated_at: "2024-03-04 03:36:03.456696"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eudysbiome"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-eudysbiome"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eudysbiome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eudysbiome", "latest": {"1.32.0--r43hdfd78af_0": "sha256:c50aafdb69c04de14886e9dc1db6689b4c2ddcbbc84a2b108380094a5798a070"}, "tags": {"1.8.0--r3.4.1_0": "sha256:fa4a3cd198ec3982251894fe99e5543c74924f92f9db23b0b829c0735916dbb5", "1.24.0--r41hdfd78af_0": "sha256:ea2d016933beeea37dccf757b65ad537d8c903a8639e56c8c5332bd5f6ce266f", "1.22.0--r41hdfd78af_0": "sha256:33f724bedd481e04e58da21ad10d58c86d0e3650cadb3e6096442fc5ce6f7d4f", "1.20.0--r40hdfd78af_1": "sha256:06fd96805210144b7b09d95305e5a44e161188238fdd8ea34d5e47e875544549", "1.18.0--r40_0": "sha256:27bb9a97b060dc9f4b94d22c9629e78d2e318fc62d51dc1554f2120e00ef2e6f", "1.16.0--r36_0": "sha256:352339e73fa7f14d3503f6938fed3fbc502aff9cd026d02b340d20201ac54219", "1.28.0--r42hdfd78af_0": "sha256:fd30a6fec5ade7828ee8c270a048332f92e358fd280856f9e020e06cd0eb68ac", "1.30.0--r43hdfd78af_0": "sha256:f1085e06ac6bcbfe8bd4e69490d3f52478400c77e37da90555786dc1540a8819", "1.32.0--r43hdfd78af_0": "sha256:c50aafdb69c04de14886e9dc1db6689b4c2ddcbbc84a2b108380094a5798a070"}, "docker": "quay.io/biocontainers/bioconductor-eudysbiome", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eudysbiome.
shpc-registry automated BioContainers addition for bioconductor-eudysbiome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eudysbiome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eudysbiome:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eudysbiome/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-eudysbiome/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eudysbiome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eudysbiome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eudysbiome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eudysbiome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eudysbiome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eudysbiome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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