---
layout: container
name:  "quay.io/biocontainers/bioconductor-runibic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-runibic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-runibic/container.yaml"
updated_at: "2025-05-01 07:02:48.740358"
latest: "1.28.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-runibic"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_2"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.0--r43hf17093f_0"
 - "1.24.0--r43hf17093f_0"
 - "1.28.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-runibic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-runibic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-runibic", "latest": {"1.28.0--r44he5774e6_0": "sha256:2a57db60741dfa1b91880e36dcd25721605a37854914b1d009e6483f7af25ba7"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:0fa71ee906438a830492f301425edf7d284973f5cce6b632025ea10e1be29604", "1.16.0--r41hc247a5b_2": "sha256:80766744c07408dd179b4edcb9dd566d7f7a81a753f173c183c0ababd2370185", "1.14.0--r41h399db7b_0": "sha256:eec762a931dba9b3b0481c8516caee881487b1df2c92b2d74df743aa021c8cc4", "1.12.0--r40h399db7b_2": "sha256:e2dd761bbc8117dac107c5c26a76dff7922510073ed7c91b5fafe0da2b65bd76", "1.10.0--r40h5f743cb_0": "sha256:f09b69920db043e2e8199a3f38e193c93c039903b9b615bc92f74011a1a85e45", "1.20.0--r42hc247a5b_0": "sha256:a0c469426d05dda24e347dae5d73fb777f31a9c063a4885ff6af5e7701dd806f", "1.20.0--r42hf17093f_1": "sha256:526e6ee6451d908af28b85ad1136accf154bfa33bbf2b9456bc3f1c7d0eeac51", "1.22.0--r43hf17093f_0": "sha256:5e990d7c126ef92cec8bde42673b87434c164842cdd4d2e9c7799b3d05d4d479", "1.24.0--r43hf17093f_0": "sha256:f75fbcf18d92ad1b9801d24b204b2d0b6a74eea69ac73fd1975fca7848a3159f", "1.28.0--r44he5774e6_0": "sha256:2a57db60741dfa1b91880e36dcd25721605a37854914b1d009e6483f7af25ba7"}, "docker": "quay.io/biocontainers/bioconductor-runibic", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-runibic.
shpc-registry automated BioContainers addition for bioconductor-runibic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-runibic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-runibic:1.28.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-runibic/1.28.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-runibic/1.28.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-runibic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-runibic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-runibic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-runibic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-runibic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-runibic-inspect-deffile:

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