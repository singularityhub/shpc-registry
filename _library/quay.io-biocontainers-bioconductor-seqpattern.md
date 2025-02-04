---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqpattern"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqpattern/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqpattern/container.yaml"
updated_at: "2025-02-04 03:10:35.504732"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqpattern"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.26.0--r41hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqpattern"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqpattern", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqpattern", "latest": {"1.38.0--r44hdfd78af_0": "sha256:fdae9eb3a69387df8817477e6266936d968cf437d067673f035b3a273c684536"}, "tags": {"1.8.0--r3.4.1_0": "sha256:404be8ff5daa4b3be370448266d99507a61897bcf6fdf60503e44193167a68e9", "1.30.0--r42hdfd78af_0": "sha256:bc61d040e3356d1ac7360dafea72c26b4fe1e2a53ca7f9a9e71915d627504569", "1.26.0--r41hdfd78af_0": "sha256:2c0b533d40f9437de35d51886d3d764b279b2662d933f2c598f483aeed75d0b9", "1.24.0--r41hdfd78af_0": "sha256:542af8ef436adbd47106d82448e23955c89fffc710b526f17d454bbc85a18d87", "1.22.0--r40hdfd78af_1": "sha256:e4b1f38c26b4e2c3ab70d7315f6b55363e2d8b7fb7448dd265690a1bafd81a68", "1.20.0--r40_0": "sha256:edc6ceb5bbf41b3fd173227e2547b19f2a7ff2e2bc1a82aeac78109018487649", "1.32.0--r43hdfd78af_0": "sha256:da5a2c4d90bf52449ee1fc1be800f419f99f7364b4cc5ed242e1adf23730470a", "1.34.0--r43hdfd78af_0": "sha256:d94b888118101ded859312f7da7e7ef5fbd7865c9372ec470de538c374eebc2c", "1.38.0--r44hdfd78af_0": "sha256:fdae9eb3a69387df8817477e6266936d968cf437d067673f035b3a273c684536"}, "docker": "quay.io/biocontainers/bioconductor-seqpattern", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqpattern.
shpc-registry automated BioContainers addition for bioconductor-seqpattern
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqpattern
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqpattern:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqpattern/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqpattern/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqpattern-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqpattern-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqpattern-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqpattern-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqpattern-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqpattern-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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