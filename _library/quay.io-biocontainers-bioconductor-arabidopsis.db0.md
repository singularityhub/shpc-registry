---
layout: container
name:  "quay.io/biocontainers/bioconductor-arabidopsis.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-arabidopsis.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-arabidopsis.db0/container.yaml"
updated_at: "2022-11-12 00:43:41.074774"
latest: "3.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-arabidopsis.db0"
aliases:
 - ".bioconductor-arabidopsis.db0-post-link.sh"
 - ".bioconductor-arabidopsis.db0-pre-unlink.sh"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.3--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-arabidopsis.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-arabidopsis.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-arabidopsis.db0", "latest": {"3.16.0--r42hdfd78af_0": "sha256:9148533900346c853ac0c5b193b2fd30855c00b96918d66a65e2da9818444ca1"}, "tags": {"3.8.2--r36_1": "sha256:2374b9481e328e2f39d0691a62d7642d5fd395067d270dc7df6caf5b1129d7ed", "3.16.0--r42hdfd78af_0": "sha256:9148533900346c853ac0c5b193b2fd30855c00b96918d66a65e2da9818444ca1", "3.14.0--r41hdfd78af_1": "sha256:ac25886096c75ea625e59da226e44da4703e391d56cd5b4045ed691660cea32a", "3.13.0--r41hdfd78af_0": "sha256:d4012a22367305c36c03c83ff8b2fced1f4fe781635c372ad4d7164a80a78450", "3.12.0--r40hdfd78af_1": "sha256:1c2690fbc1523617c774eec74a5b2ced1000cb334e2f4c61d6cb1e4c8123257e", "3.11.3--r40_0": "sha256:bce2e406e5acf1d132e9a79e12777799ab49567ca95816d1c0d65889d5e23330"}, "docker": "quay.io/biocontainers/bioconductor-arabidopsis.db0", "aliases": {".bioconductor-arabidopsis.db0-post-link.sh": "/usr/local/bin/.bioconductor-arabidopsis.db0-post-link.sh", ".bioconductor-arabidopsis.db0-pre-unlink.sh": "/usr/local/bin/.bioconductor-arabidopsis.db0-pre-unlink.sh", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-arabidopsis.db0.
shpc-registry automated BioContainers addition for bioconductor-arabidopsis.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-arabidopsis.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-arabidopsis.db0:3.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-arabidopsis.db0/3.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-arabidopsis.db0/3.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-arabidopsis.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arabidopsis.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arabidopsis.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-arabidopsis.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-arabidopsis.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-arabidopsis.db0-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-arabidopsis.db0-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-arabidopsis.db0-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-arabidopsis.db0-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-arabidopsis.db0-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-arabidopsis.db0-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-arabidopsis.db0-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-arabidopsis.db0-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-arabidopsis.db0-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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