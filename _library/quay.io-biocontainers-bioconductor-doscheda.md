---
layout: container
name:  "quay.io/biocontainers/bioconductor-doscheda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-doscheda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-doscheda/container.yaml"
updated_at: "2024-03-28 03:05:21.087571"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-doscheda"
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
description: "shpc-registry automated BioContainers addition for bioconductor-doscheda"
config: {"url": "https://biocontainers.pro/tools/bioconductor-doscheda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-doscheda", "latest": {"1.24.0--r43hdfd78af_0": "sha256:5424aa3ad6620d05b46e8b3b50efd55f8056321477dcbe006d07d211662c4eaf"}, "tags": {"1.8.0--r36_0": "sha256:823bfe1f4ad09bbeccbdbbd61392821b31ea6d196832eeca3c8145afd967574b", "1.20.0--r42hdfd78af_0": "sha256:e2f1b989a9fd0e72c2d356c58ae5d7f16b193ad8909bc2036d364f9ffa2298c7", "1.16.0--r41hdfd78af_0": "sha256:ec8d2c8f1d9d09ce1e8c40e83ba105034a4d7f5ac1ee5e183ee518ef4b6dad10", "1.14.0--r41hdfd78af_0": "sha256:772f4e79a8b3cbec7c9720155a1abe8733a37f14e1393e92f11a34f7abcb241f", "1.12.0--r40hdfd78af_1": "sha256:182c4ff88589b723e13117a5f715fa568e364a25cf2b42de58e50bc60cb612ec", "1.10.0--r40_0": "sha256:66e00ba8949e760a24ce8cf794cc175b8a152a54601a1d035e7f72403f83f068", "1.22.0--r43hdfd78af_0": "sha256:5340e6dc439cdd6e7c43625b96961e0edca9d29cdbfd277dacc9b55d640245c9", "1.24.0--r43hdfd78af_0": "sha256:5424aa3ad6620d05b46e8b3b50efd55f8056321477dcbe006d07d211662c4eaf"}, "docker": "quay.io/biocontainers/bioconductor-doscheda", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-doscheda.
shpc-registry automated BioContainers addition for bioconductor-doscheda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-doscheda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-doscheda:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-doscheda/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-doscheda/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-doscheda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-doscheda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-doscheda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-doscheda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-doscheda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-doscheda-inspect-deffile:

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