---
layout: container
name:  "quay.io/biocontainers/bioconductor-imas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-imas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-imas/container.yaml"
updated_at: "2025-04-01 03:39:45.480673"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-imas"
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
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-imas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-imas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-imas", "latest": {"1.30.0--r44hdfd78af_0": "sha256:84df4ddc56be682c24b98d7af6564502393240598b4d1ba96bbe58968d3cc9ea"}, "tags": {"1.8.0--r36_1": "sha256:e97fa9665a1e25f6bb705407d9e29673b673cee3328e7fbcb00d576f37319133", "1.22.0--r42hdfd78af_0": "sha256:34e2c0656425c56de9bdddee2d928c2017cf13f90397c0a6b598b1a2d960b3a6", "1.18.0--r41hdfd78af_0": "sha256:06150ae9f7d4ab913617eaab17ae519beea5e1d54a0e6f36bbdbf0e0512db47c", "1.16.0--r41hdfd78af_0": "sha256:a133014525b84f3985e64c8f9397e443dd15dec0e7ec9ea0951673c47c0728fc", "1.14.0--r40hdfd78af_1": "sha256:fe362ec80284a85676c6be51cdfaee085c28814fae9cb042f85b0730b786223e", "1.12.0--r40_0": "sha256:dd39a73e10d34ae2f471f23464096527de25566150a2eb6d0a31e030272ae62f", "1.24.0--r43hdfd78af_0": "sha256:8a27331a9fae9a0f4fec76b2030d427eaa9e06d05e448b3e390f59adc84b6995", "1.26.0--r43hdfd78af_0": "sha256:a5336ed77e8e8d292c69178da90cf31bfa7d8332407e1d262b3d6bf72323c9ac", "1.30.0--r44hdfd78af_0": "sha256:84df4ddc56be682c24b98d7af6564502393240598b4d1ba96bbe58968d3cc9ea"}, "docker": "quay.io/biocontainers/bioconductor-imas", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-imas.
shpc-registry automated BioContainers addition for bioconductor-imas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-imas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-imas:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-imas/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-imas/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-imas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-imas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-imas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-imas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-imas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-imas-inspect-deffile:

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