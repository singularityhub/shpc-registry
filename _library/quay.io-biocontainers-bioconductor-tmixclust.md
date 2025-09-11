---
layout: container
name:  "quay.io/biocontainers/bioconductor-tmixclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tmixclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tmixclust/container.yaml"
updated_at: "2025-09-11 05:05:33.820395"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tmixclust"
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
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tmixclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tmixclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tmixclust", "latest": {"1.28.0--r44hdfd78af_0": "sha256:b26cad0478ba2b86d19e50977448003e0b8fd1c88ef6ea78c6f217551ea3b506"}, "tags": {"1.8.0--r36_0": "sha256:8971c204008a64e797a795dea3dc11582bd9ba732aad994a5bf78d439ec6fd31", "1.20.0--r42hdfd78af_0": "sha256:3cb6666f454c041e0155a5e262afec272ba72c322809e5de438bd315c4731219", "1.16.0--r41hdfd78af_0": "sha256:8a3e04b8551849c0bb66312eff0111fe753ad94faf287374053869c2c8c9ca20", "1.14.0--r41hdfd78af_0": "sha256:f0b3fbf2185fbb6656f2128a8fe28b189b16c49c310e944e33508ea0de887c63", "1.12.0--r40hdfd78af_1": "sha256:b4e755eb8dd6845216d15e6b12dd73665c3615b21c38cb843d41c524353f817c", "1.10.0--r40_0": "sha256:5eae0204de3c54ee9a28740cfaf1fe7d2ead3b8c83996fe700452f02de3e31fb", "1.22.0--r43hdfd78af_0": "sha256:3b7961e159e79f214ac621053095df2aba0cd40e6f3ad690a4f4b326165c3a32", "1.24.0--r43hdfd78af_0": "sha256:65bb66474799a31ac3aa7c29f8c0f77e40015eb8f284d966457d4aaa8b181d14", "1.28.0--r44hdfd78af_0": "sha256:b26cad0478ba2b86d19e50977448003e0b8fd1c88ef6ea78c6f217551ea3b506"}, "docker": "quay.io/biocontainers/bioconductor-tmixclust", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tmixclust.
shpc-registry automated BioContainers addition for bioconductor-tmixclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tmixclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tmixclust:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tmixclust/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tmixclust/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tmixclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tmixclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tmixclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tmixclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tmixclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tmixclust-inspect-deffile:

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