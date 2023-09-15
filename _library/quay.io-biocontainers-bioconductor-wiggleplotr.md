---
layout: container
name:  "quay.io/biocontainers/bioconductor-wiggleplotr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-wiggleplotr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-wiggleplotr/container.yaml"
updated_at: "2023-09-15 02:59:35.363426"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-wiggleplotr"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.1--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-wiggleplotr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-wiggleplotr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-wiggleplotr", "latest": {"1.24.0--r43hdfd78af_0": "sha256:a0e11cfbf2a898950c3f6d81ec753493e44779bfc326a7004af5eadcab4d2569"}, "tags": {"1.8.0--r36_1": "sha256:4ef14dec7eb0e3b31934c99b9ca2cf2f4cf293bf32cfbe2c474f74ae73456e8b", "1.18.0--r41hdfd78af_0": "sha256:9612426d56cb83bb1bf208e4844bf40d4e8ed6e07a31b60bf6503ab9a24a4566", "1.16.0--r41hdfd78af_0": "sha256:758384c0ace6cf1e807b2d9f84e788d283a30dce3914f53b7747ffcd795a6dac", "1.14.0--r40hdfd78af_1": "sha256:b9ab0bf7439b854913da3650985e1c884c88286b06a9eeadd34f219d340b5eba", "1.12.0--r40_0": "sha256:cc29183ffb30e927d3edd6f1fef42afff35d48ad053aaeb07afac5c317e6a9d3", "1.10.1--r36_0": "sha256:0445bf8243475db9cd87c403fb437bd5cf1e8176558a55c56deba4e4cbfb1875", "1.22.0--r42hdfd78af_0": "sha256:d7d5332df2d006e116ef369b66b5a927356c998e87329f49b87eade0fc986590", "1.24.0--r43hdfd78af_0": "sha256:a0e11cfbf2a898950c3f6d81ec753493e44779bfc326a7004af5eadcab4d2569"}, "docker": "quay.io/biocontainers/bioconductor-wiggleplotr", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-wiggleplotr.
shpc-registry automated BioContainers addition for bioconductor-wiggleplotr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-wiggleplotr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-wiggleplotr:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-wiggleplotr/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-wiggleplotr/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-wiggleplotr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wiggleplotr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wiggleplotr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-wiggleplotr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-wiggleplotr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-wiggleplotr-inspect-deffile:

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