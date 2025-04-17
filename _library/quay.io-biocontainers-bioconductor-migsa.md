---
layout: container
name:  "quay.io/biocontainers/bioconductor-migsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-migsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-migsa/container.yaml"
updated_at: "2025-04-17 03:21:58.828403"
latest: "1.21.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-migsa"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.21.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-migsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-migsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-migsa", "latest": {"1.21.0--r42hdfd78af_0": "sha256:77e9b26b21f7ae516ea6ab6a326bed2dea38791e85231ca8ee0c0d31f7ad3bc1"}, "tags": {"1.8.1--r36_0": "sha256:cc3f02fa84b8aa3403a2e27651ad95b02d23c848e74c1248d00140174f867e4b", "1.18.0--r41hdfd78af_0": "sha256:8c5d5dbde924de917a439a1c7e49f80620f7bf01fcd209e03be152b3eac7de5c", "1.16.0--r41hdfd78af_0": "sha256:b79b132721ea1c44246e721d6f1ea107be26be55017477eab90bbee98905faa2", "1.14.1--r40hdfd78af_1": "sha256:5d374308f2735e1f91de1b15b61300fb0899af31dd468ba9a45d2df63619282e", "1.12.0--r40_0": "sha256:6c94371eea2fd9f04d3209d3f695ee2b6a541ca928bc878cf54c6378460edcdc", "1.10.0--r36_0": "sha256:ea4e8bb1c4aaaa2a75768a4c3853faf6c8ad4df18c939b577446ffeb581296b0", "1.21.0--r42hdfd78af_0": "sha256:77e9b26b21f7ae516ea6ab6a326bed2dea38791e85231ca8ee0c0d31f7ad3bc1"}, "docker": "quay.io/biocontainers/bioconductor-migsa", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-migsa.
shpc-registry automated BioContainers addition for bioconductor-migsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-migsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-migsa:1.21.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-migsa/1.21.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-migsa/1.21.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-migsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-migsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-migsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-migsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-migsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-migsa-inspect-deffile:

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