---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.mmu.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.mmu.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.mmu.eg.db/container.yaml"
updated_at: "2025-09-24 03:20:37.127713"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.mmu.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.mmu.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.mmu.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.mmu.eg.db", "latest": {"3.20.0--r44hdfd78af_0": "sha256:20814b5462d243a343db19bcdb345c64d431a023574a776f29e170a5746d49f4"}, "tags": {"3.8.2--r36_1": "sha256:40a9f3b230061070afa6c8549136fc20c12c637e060e92bf07f769724da70688", "3.16.0--r42hdfd78af_0": "sha256:053239843dc385e5deeecf7674ecaa4d6ca8ab773bb2c5590174920f691f545c", "3.14.0--r41hdfd78af_1": "sha256:0920cda5d679a5b3287579dc8e10ca55e5a05a23ab04297c62bdbffc98f2d3b5", "3.13.0--r41hdfd78af_0": "sha256:c47da896aa89a292a16543b54e03f8b2b93611f4f3ac5119844e008ceab58628", "3.12.0--r40hdfd78af_1": "sha256:98f8866fdabe68ded7c82a148fc1bf19cf6894765de3151484ba7b56716304b5", "3.11.1--r40_0": "sha256:8824034e0936d0e5654bf1a051b6403b1ce3d3a6a9dfe24f0c1c919bbfb45bb1", "3.17.0--r43hdfd78af_0": "sha256:127d00ef5c929a35b66f84683b165993f8ff77ae00a710a7d343dabb2d270d97", "3.18.0--r43hdfd78af_0": "sha256:67323d3463e3e31bfd3e13b70208c9064d6c04d11e716942375996fe6f674c7b", "3.20.0--r44hdfd78af_0": "sha256:20814b5462d243a343db19bcdb345c64d431a023574a776f29e170a5746d49f4"}, "docker": "quay.io/biocontainers/bioconductor-org.mmu.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.mmu.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.mmu.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.mmu.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.mmu.eg.db:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.mmu.eg.db/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.mmu.eg.db/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.mmu.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.mmu.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.mmu.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.mmu.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.mmu.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.mmu.eg.db-inspect-deffile:

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