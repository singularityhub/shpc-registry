---
layout: container
name:  "quay.io/biocontainers/bioconductor-egsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-egsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-egsea/container.yaml"
updated_at: "2023-09-26 03:26:57.951999"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-egsea"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.1--r40hdfd78af_0"
 - "1.16.0--r40_0"
 - "1.14.0--r36_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-egsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-egsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-egsea", "latest": {"1.28.0--r43hdfd78af_0": "sha256:e3f73091954a5cbe4f3c579b23b5eda2744f1f678cc9b1521ed30f99c1402175"}, "tags": {"1.8.0--r341_0": "sha256:9d66d5cdd12359f3eba096d362d4dea82cb1866ad49752cbf941182593256651", "1.22.0--r41hdfd78af_0": "sha256:109b5ffd7231b60d85d54e0a7b81a7eb2b3ace3b9b09ad824cd4f7a0d5566d68", "1.20.0--r41hdfd78af_0": "sha256:1bd456133816ddafea56d0a645fb0c1ad6c9df0d84cdae9315e2ef3bec933561", "1.18.1--r40hdfd78af_0": "sha256:e772f4360f0cd31d9e9ea4abaefb8392acf4df6be507b73f06a445a767cb9953", "1.16.0--r40_0": "sha256:b0bf39ca994bb478a0de4d62c122dab948447eb8e7d0c4f5b623a28239693b1b", "1.14.0--r36_1": "sha256:ecbae1aead3dcd33267ae4e51a8d91dbc03d275ab07a3fdafd780a8036a70d42", "1.26.0--r42hdfd78af_0": "sha256:df5ca30bd492c2ebf865b26735928075b669ce5c37606d54d64a83f2649714bb", "1.28.0--r43hdfd78af_0": "sha256:e3f73091954a5cbe4f3c579b23b5eda2744f1f678cc9b1521ed30f99c1402175"}, "docker": "quay.io/biocontainers/bioconductor-egsea", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-egsea.
shpc-registry automated BioContainers addition for bioconductor-egsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-egsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-egsea:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-egsea/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-egsea/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-egsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-egsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-egsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-egsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-egsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-egsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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