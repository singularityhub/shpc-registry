---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtcgatoolbox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtcgatoolbox/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtcgatoolbox/container.yaml"
updated_at: "2025-07-26 03:49:50.334404"
latest: "2.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtcgatoolbox"
aliases:
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r40hdfd78af_1"
 - "2.18.0--r40_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.32.1--r43hdfd78af_0"
 - "2.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtcgatoolbox"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtcgatoolbox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtcgatoolbox", "latest": {"2.36.0--r44hdfd78af_0": "sha256:a1e6399133e979c2653e688c3316bee3af07e9fe97888120cc69b2d59e6fb8c6"}, "tags": {"2.8.0--r3.4.1_0": "sha256:c08515862e3e32320d9a1eb245cc88b2f571dd9ad5277144dc2cecb743c5f14f", "2.28.0--r42hdfd78af_0": "sha256:b607be1c28d7ec011878a7c051993b349dac9022eab7e0d6ff213666c452da99", "2.24.0--r41hdfd78af_0": "sha256:ac679ad5b70c486b0839f5896eb85970c73ffa68b8c65576e96070be05227bde", "2.22.0--r41hdfd78af_0": "sha256:1b1470bf3486a1ce9568a3ab976d238ed96b50c28b79616d4db2ec02c0e77c7e", "2.20.0--r40hdfd78af_1": "sha256:d71a899bd1537901bddcbb0d620addf0e5c2316950de0ac76555f1004f6a3fc0", "2.18.0--r40_0": "sha256:d846e47d435129c86a19e210b63d7b0f3054cca01f66bd37d83a8c1ae49a2310", "2.30.0--r43hdfd78af_0": "sha256:a3b3580ccca004227abe55b7250b89109467cf3cf62a85c73619e44fe9e6f13a", "2.32.1--r43hdfd78af_0": "sha256:e1547803af3d78a05351b7ab2a7d39a41e44501d3658cb393990b21948187f3e", "2.36.0--r44hdfd78af_0": "sha256:a1e6399133e979c2653e688c3316bee3af07e9fe97888120cc69b2d59e6fb8c6"}, "docker": "quay.io/biocontainers/bioconductor-rtcgatoolbox", "aliases": {"wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtcgatoolbox.
shpc-registry automated BioContainers addition for bioconductor-rtcgatoolbox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcgatoolbox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcgatoolbox:2.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtcgatoolbox/2.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtcgatoolbox/2.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtcgatoolbox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcgatoolbox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcgatoolbox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtcgatoolbox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtcgatoolbox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtcgatoolbox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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