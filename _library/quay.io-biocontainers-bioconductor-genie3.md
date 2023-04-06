---
layout: container
name:  "quay.io/biocontainers/bioconductor-genie3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genie3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genie3/container.yaml"
updated_at: "2023-04-06 03:18:11.285930"
latest: "1.20.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genie3"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_0"
 - "1.20.0--r42hc0cfd56_0"
 - "1.16.0--r41hc0cfd56_2"
 - "1.14.0--r41hd029910_0"
 - "1.12.0--r40hd029910_1"
 - "1.10.0--r40h037d062_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genie3"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genie3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genie3", "latest": {"1.20.0--r42hc0cfd56_0": "sha256:08a2a6bb2f2134705f1279614eb8ca6565062ccb061c093a9b02277ede85da95"}, "tags": {"1.8.0--r36h516909a_0": "sha256:329e18138e2cc4eb4d826fb8dbbb896b6e9308229c996c617d8e8eca6eb689ce", "1.20.0--r42hc0cfd56_0": "sha256:08a2a6bb2f2134705f1279614eb8ca6565062ccb061c093a9b02277ede85da95", "1.16.0--r41hc0cfd56_2": "sha256:6f2cb996ffa0df0631822d00517d27fe139d17f2a79fe53c9d18c79d7286c2ff", "1.14.0--r41hd029910_0": "sha256:7b7d2ff41a4aa0a74648475604541f236f03bc2b310ed60fdb627e8043581e5f", "1.12.0--r40hd029910_1": "sha256:5b70b078a4f7d2abf17897b3dd56cd61b5bc7f3c9842d093fd7d8d2f248f753b", "1.10.0--r40h037d062_0": "sha256:726f864a10998dd519dd6978004ce08aa3c1b3f9ecfe53abc2cb36a109472171"}, "docker": "quay.io/biocontainers/bioconductor-genie3", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genie3.
shpc-registry automated BioContainers addition for bioconductor-genie3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genie3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genie3:1.20.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genie3/1.20.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-genie3/1.20.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genie3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genie3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genie3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genie3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genie3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genie3-inspect-deffile:

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