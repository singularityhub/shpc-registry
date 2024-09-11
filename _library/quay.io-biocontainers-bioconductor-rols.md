---
layout: container
name:  "quay.io/biocontainers/bioconductor-rols"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rols/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rols/container.yaml"
updated_at: "2024-09-11 02:49:06.482155"
latest: "2.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rols"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.2--r341_0"
 - "2.26.0--r42hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.2--r40hdfd78af_0"
 - "2.16.1--r40_0"
 - "2.28.0--r43hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rols"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rols", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rols", "latest": {"2.30.0--r43hdfd78af_0": "sha256:3a011a6225129dadcb2d9b32e62e25ff998614fd4fb12046668231457fb0f27f"}, "tags": {"2.8.2--r341_0": "sha256:325eed9b691ade85e7bccec2216d7e22c38faa3f9e33bf71400b268ae68fe6c4", "2.26.0--r42hdfd78af_0": "sha256:1b74fe430bacae217946f52c63b2fd0ee4c59cf7157839e2c07857416f856c9b", "2.22.0--r41hdfd78af_0": "sha256:dfbc05d2c14f0343b960dd7764f5f7297c5a0690db3d5ddd9a36e0a400952161", "2.20.0--r41hdfd78af_0": "sha256:403e87a216af715dd50bf40f589c9cc3ceed763eb9eaa7b2c2b5964e2b5ca4f8", "2.18.2--r40hdfd78af_0": "sha256:bf74681963376a6960f71e775b5a3ba16fa61382934d1fdb4b93f085fd3c9b86", "2.16.1--r40_0": "sha256:3ba947c91d8032f10b41d9d7619db1eb933cc418c9d81b93dddbaf9cd01bc65a", "2.28.0--r43hdfd78af_0": "sha256:55d719216fa0311be3ca2f1880e273b032d22bcc3f111e8850dd60d29530f6c3", "2.30.0--r43hdfd78af_0": "sha256:3a011a6225129dadcb2d9b32e62e25ff998614fd4fb12046668231457fb0f27f"}, "docker": "quay.io/biocontainers/bioconductor-rols", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rols.
shpc-registry automated BioContainers addition for bioconductor-rols
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rols
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rols:2.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rols/2.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rols/2.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rols-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rols-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rols-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rols-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rols-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rols-inspect-deffile:

```bash
$ singularity inspect -d <container>
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