---
layout: container
name:  "quay.io/biocontainers/bioconductor-rexposome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rexposome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rexposome/container.yaml"
updated_at: "2023-04-10 03:08:48.987728"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rexposome"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.4--r40hdfd78af_0"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rexposome"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rexposome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rexposome", "latest": {"1.20.0--r42hdfd78af_0": "sha256:bb6cfad6921e1fb4b39a347ea9d76f7807da397c54498e524c9dc021e2094c01"}, "tags": {"1.8.0--r36_0": "sha256:1e066678d985a144c21471365066505781f4caebf8a3372b6d1d80b1ab43cad1", "1.20.0--r42hdfd78af_0": "sha256:bb6cfad6921e1fb4b39a347ea9d76f7807da397c54498e524c9dc021e2094c01", "1.16.0--r41hdfd78af_0": "sha256:eb02b2edba1a66b46ac6a243f0603ab1fd417e0e30b3f236917b5aafd32f7cb3", "1.14.0--r41hdfd78af_0": "sha256:d877cfae1ebecb95056c02fd5d20f3ed2f800e658fb94c68e73d0706e6116339", "1.12.4--r40hdfd78af_0": "sha256:c80ae4a5173250e6a80e0cf3940425a1832206da2018423b57c848fdb8c3803b", "1.10.0--r40_0": "sha256:f0428019ae4bc29b435a0169c5650bf1749ec0f419e078a3c542a797af880cbe"}, "docker": "quay.io/biocontainers/bioconductor-rexposome", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rexposome.
shpc-registry automated BioContainers addition for bioconductor-rexposome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rexposome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rexposome:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rexposome/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rexposome/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rexposome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rexposome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rexposome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rexposome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rexposome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rexposome-inspect-deffile:

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