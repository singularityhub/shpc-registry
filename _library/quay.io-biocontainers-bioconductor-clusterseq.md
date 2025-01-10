---
layout: container
name:  "quay.io/biocontainers/bioconductor-clusterseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clusterseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clusterseq/container.yaml"
updated_at: "2025-01-10 03:13:52.538590"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clusterseq"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clusterseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clusterseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clusterseq", "latest": {"1.30.0--r44hdfd78af_0": "sha256:d8430f393fc38feea9fffbd100b9890136d9806d02a70dbb5fb7bd31d956e503"}, "tags": {"1.8.0--r36_1": "sha256:030cfabe5c27d78d8c89f074ffa0e23ccb97ba02a1e9faf7746aef3d4356e3ae", "1.22.0--r42hdfd78af_0": "sha256:55541cfc3de629aa929604a37daf2a83a09047198cebc411e028e35dd4972135", "1.18.0--r41hdfd78af_0": "sha256:f54c4fa2cbbef5de2fdcab4da90e08dbd3eace034ea2d8c2ecda32dac9e10349", "1.16.0--r41hdfd78af_0": "sha256:000c6472a1f03e668dcc6608469cac1bcd7792e7ebe90e8121b39220561dc399", "1.14.0--r40hdfd78af_1": "sha256:32f6d44329aa187ada5c0b9e01cfae7e80fc84fe77c9a64a417ea2413e44ae1f", "1.12.0--r40_0": "sha256:b0774a1eb34b99dca952d6410cde233e602cd74075d8e7acff3da437ed20f9e1", "1.26.0--r43hdfd78af_0": "sha256:c624208d3ee9a79896be7c2c08ddcb99721c85e3e748de8bd0c981a1c4b80d06", "1.30.0--r44hdfd78af_0": "sha256:d8430f393fc38feea9fffbd100b9890136d9806d02a70dbb5fb7bd31d956e503"}, "docker": "quay.io/biocontainers/bioconductor-clusterseq", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clusterseq.
shpc-registry automated BioContainers addition for bioconductor-clusterseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clusterseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clusterseq:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clusterseq/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clusterseq/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clusterseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clusterseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clusterseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clusterseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clusterseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clusterseq-inspect-deffile:

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