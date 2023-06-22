---
layout: container
name:  "quay.io/biocontainers/bioconductor-rjmcmcnucleosomes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rjmcmcnucleosomes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rjmcmcnucleosomes/container.yaml"
updated_at: "2023-06-22 04:34:10.254967"
latest: "1.22.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rjmcmcnucleosomes"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_1"
 - "1.22.0--r42hc247a5b_0"
 - "1.18.0--r41hc247a5b_2"
 - "1.16.0--r41h399db7b_0"
 - "1.14.0--r40h399db7b_1"
 - "1.12.0--r40h5f743cb_0"
 - "1.22.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rjmcmcnucleosomes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rjmcmcnucleosomes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rjmcmcnucleosomes", "latest": {"1.22.0--r42hf17093f_1": "sha256:3afabd036eae16d2b0652b038c08220460d7d953ca4e16ea29b7db46a25cf1e6"}, "tags": {"1.8.0--r36he1b5a44_1": "sha256:58a8e7510fdbd9c7a8422e859fe0624cdb305b19fa7ffe8aca2d91d397512203", "1.22.0--r42hc247a5b_0": "sha256:49fc71f8d55a6910e6771f40a39186ae7632e1a8351d9121cc00754c301670cc", "1.18.0--r41hc247a5b_2": "sha256:46aeff41775d188f2d96b9f61992e60d88a7307185c2e01a87b7c350ea425907", "1.16.0--r41h399db7b_0": "sha256:c415b725b4d05172089fcca7502b9c59ccc1df0dac2389c09b1fce6d09cc89f2", "1.14.0--r40h399db7b_1": "sha256:4eae7ed93f481ccd614ff6758574b4fe5cad85863bad72b77f7bb74cd0920a0a", "1.12.0--r40h5f743cb_0": "sha256:0a7c877878de2f03533cb2d9c1aff6816383947126bbca9802f1f0e5b2a95d3e", "1.22.0--r42hf17093f_1": "sha256:3afabd036eae16d2b0652b038c08220460d7d953ca4e16ea29b7db46a25cf1e6"}, "docker": "quay.io/biocontainers/bioconductor-rjmcmcnucleosomes", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rjmcmcnucleosomes.
shpc-registry automated BioContainers addition for bioconductor-rjmcmcnucleosomes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rjmcmcnucleosomes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rjmcmcnucleosomes:1.22.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rjmcmcnucleosomes/1.22.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-rjmcmcnucleosomes/1.22.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rjmcmcnucleosomes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rjmcmcnucleosomes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rjmcmcnucleosomes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rjmcmcnucleosomes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rjmcmcnucleosomes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rjmcmcnucleosomes-inspect-deffile:

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