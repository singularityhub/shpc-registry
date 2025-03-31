---
layout: container
name:  "quay.io/biocontainers/bioconductor-multiomicsviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multiomicsviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multiomicsviz/container.yaml"
updated_at: "2025-03-31 03:22:21.095171"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multiomicsviz"
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
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multiomicsviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multiomicsviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multiomicsviz", "latest": {"1.24.0--r43hdfd78af_0": "sha256:bb2f00f003637bb1a92d5ca67487c327d9e98580d3647eb8267baa4efa12f8d9"}, "tags": {"1.8.0--r36_1": "sha256:85d4a4cc6b4b54694bc762f9653b3686b79da8b06fe16d5cd338bd1b7f8448ac", "1.22.0--r42hdfd78af_0": "sha256:e266038bb958a2801633ebd7b71f5f6c5dcb497e3345587b75715848eaa1526e", "1.18.0--r41hdfd78af_0": "sha256:42f8e0d9db5b10ff2335b5b4487b50462eb2b5748a688b3a1c5480542da89516", "1.16.0--r41hdfd78af_0": "sha256:4a2d4e0fc09c70b2c4162dbde957a22d8e46311326cfcca18e2babc328e874b9", "1.14.0--r40hdfd78af_1": "sha256:fe597954cc4f3e24ed286a8674c382126a580f59fccf001695fc127d4ba045d4", "1.12.0--r40_0": "sha256:e6d41ca7fbdcf2899e720de39d20ad633c83c0547a1d4cda56647f13c9b559d0", "1.24.0--r43hdfd78af_0": "sha256:bb2f00f003637bb1a92d5ca67487c327d9e98580d3647eb8267baa4efa12f8d9"}, "docker": "quay.io/biocontainers/bioconductor-multiomicsviz", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multiomicsviz.
shpc-registry automated BioContainers addition for bioconductor-multiomicsviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multiomicsviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multiomicsviz:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multiomicsviz/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multiomicsviz/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multiomicsviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiomicsviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiomicsviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multiomicsviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multiomicsviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multiomicsviz-inspect-deffile:

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