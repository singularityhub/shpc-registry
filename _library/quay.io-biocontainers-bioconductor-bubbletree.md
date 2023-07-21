---
layout: container
name:  "quay.io/biocontainers/bioconductor-bubbletree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bubbletree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bubbletree/container.yaml"
updated_at: "2023-07-21 03:26:44.517156"
latest: "2.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bubbletree"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_1"
 - "2.28.0--r42hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r40hdfd78af_1"
 - "2.18.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bubbletree"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bubbletree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bubbletree", "latest": {"2.28.0--r42hdfd78af_0": "sha256:04c161353e7062a4aea9f7fe57e5a7a768d7914a7de670ad04eb8dd50b293a96"}, "tags": {"2.8.0--r3.4.1_1": "sha256:56ec8558a11756a965cd4a986c572020d91f929b7f3d38c6ce1bbc55f21f0aca", "2.28.0--r42hdfd78af_0": "sha256:04c161353e7062a4aea9f7fe57e5a7a768d7914a7de670ad04eb8dd50b293a96", "2.24.0--r41hdfd78af_0": "sha256:c15ff884f5a9c55322770791a016b7bb0d5fc86aac3d886dee4fc408d097afaf", "2.22.0--r41hdfd78af_0": "sha256:00b0413b1c999908c7dc34b0ebc44b3ccf911c2ec0b87134aed178aa45fbff84", "2.20.0--r40hdfd78af_1": "sha256:6cb36450630d116440fa3eff2654aec3d39a3f61f4f9d2e5eba451032d308c14", "2.18.0--r40_0": "sha256:12419db5c1cc89c0fcb2fa599af8eacac33f899d64bbae80965e147af285efff"}, "docker": "quay.io/biocontainers/bioconductor-bubbletree", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bubbletree.
shpc-registry automated BioContainers addition for bioconductor-bubbletree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bubbletree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bubbletree:2.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bubbletree/2.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bubbletree/2.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bubbletree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bubbletree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bubbletree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bubbletree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bubbletree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bubbletree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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