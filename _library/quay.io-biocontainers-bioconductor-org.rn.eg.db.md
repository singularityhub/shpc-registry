---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.rn.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.rn.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.rn.eg.db/container.yaml"
updated_at: "2023-02-15 02:59:55.921900"
latest: "3.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.rn.eg.db"
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
description: "shpc-registry automated BioContainers addition for bioconductor-org.rn.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.rn.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.rn.eg.db", "latest": {"3.16.0--r42hdfd78af_0": "sha256:2c4f10b41265fbbec870798fb0748cae06b37e840f89958810ca0282925fb9bb"}, "tags": {"3.8.2--r36_1": "sha256:c0df9c788b54a4434fc6b92d0287189aa36efaf3e0e3dd8e06be70b55c73a5e9", "3.16.0--r42hdfd78af_0": "sha256:2c4f10b41265fbbec870798fb0748cae06b37e840f89958810ca0282925fb9bb", "3.14.0--r41hdfd78af_1": "sha256:20e1fda5bd7c3565e2d9a1a1cad08a3df5eece8fa375274d96bb36fa178a6eaf", "3.13.0--r41hdfd78af_0": "sha256:b61f570a25386a92cd38c8ea83aaad5eaea8d771e3dbbee259930b6bcc76712d", "3.12.0--r40hdfd78af_1": "sha256:599df2d97ff6b178349dc93832cf09a9e51c3aef99959af7d5c1962fe97de2bc", "3.11.1--r40_0": "sha256:b2e3f5e5d0ae9fcfbf86254814564aee732986387853b1ca4fda9b7c137c37bc"}, "docker": "quay.io/biocontainers/bioconductor-org.rn.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.rn.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.rn.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.rn.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.rn.eg.db:3.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.rn.eg.db/3.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.rn.eg.db/3.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.rn.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.rn.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.rn.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.rn.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.rn.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.rn.eg.db-inspect-deffile:

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