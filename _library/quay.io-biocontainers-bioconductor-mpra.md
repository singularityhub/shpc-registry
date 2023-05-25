---
layout: container
name:  "quay.io/biocontainers/bioconductor-mpra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mpra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mpra/container.yaml"
updated_at: "2023-05-25 03:09:03.853564"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mpra"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.1--r40hdfd78af_0"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mpra"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mpra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mpra", "latest": {"1.20.0--r42hdfd78af_0": "sha256:043c74a580b900e45e90da149280e04ed3bc43d6c35d86595b3c100dc4110035"}, "tags": {"1.8.0--r36_0": "sha256:c8db0d743f9f17a7fc4e11e4ba5d85d6b7da891e646f90e2f2f0983cd1a8e102", "1.20.0--r42hdfd78af_0": "sha256:043c74a580b900e45e90da149280e04ed3bc43d6c35d86595b3c100dc4110035", "1.16.0--r41hdfd78af_0": "sha256:0292f1526d3fca2e1938687211ea51ddd97fff5b85e6dcea91b5bfcecf71f49a", "1.14.0--r41hdfd78af_0": "sha256:4a0b675262dbe5b94d23d615e659929bfed7536df8de23b204510e8701e0ae3d", "1.12.1--r40hdfd78af_0": "sha256:42afc419e2b683256eabc6a7e044620bbcba2941d58ae6d82392f48dc81a207e", "1.10.0--r40_0": "sha256:dd193ed1b9b3f4d6b4b6e3c818f3fc2413ebd3b0a639d66bf2d59018f834e116"}, "docker": "quay.io/biocontainers/bioconductor-mpra", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mpra.
shpc-registry automated BioContainers addition for bioconductor-mpra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mpra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mpra:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mpra/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mpra/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mpra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mpra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mpra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mpra-inspect-deffile:

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