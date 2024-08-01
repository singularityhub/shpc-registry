---
layout: container
name:  "quay.io/biocontainers/bioconductor-inspect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-inspect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-inspect/container.yaml"
updated_at: "2024-08-01 03:12:07.187521"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-inspect"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-inspect"
config: {"url": "https://biocontainers.pro/tools/bioconductor-inspect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-inspect", "latest": {"1.30.0--r43hdfd78af_0": "sha256:f79b8b6a694239c0ca94cd49f6859c2c9dcf0fc28621dbb4ae214592d104765d"}, "tags": {"1.8.0--r3.4.1_0": "sha256:2651d5f9d3fd19fd79d07cb5069775b14174e0b6c8dcd589c94db21e78af1c31", "1.28.0--r42hdfd78af_0": "sha256:941b2c4e234805980a7c354fbaf6c5e242b38814fb7084654f3465c4a5259a5a", "1.24.0--r41hdfd78af_0": "sha256:937f2e9ac96c857ad28bcbbe64375cd6b8b04578727f73ad13c1a1ebc00a921d", "1.22.0--r41hdfd78af_0": "sha256:4e8810e2d7cd7b99cc0269596a67e5f7b059a072716442bae3ad27c8719985a4", "1.20.0--r40hdfd78af_1": "sha256:86ab678d02a5142f7736a72606e2b499c126472abee96838dc5570dfb4aca491", "1.18.0--r40_0": "sha256:1b7a0d6f42a7c75b47683cf2877cbac918d847dc651cd8cc738db67adb97fa46", "1.30.0--r43hdfd78af_0": "sha256:f79b8b6a694239c0ca94cd49f6859c2c9dcf0fc28621dbb4ae214592d104765d"}, "docker": "quay.io/biocontainers/bioconductor-inspect", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-inspect.
shpc-registry automated BioContainers addition for bioconductor-inspect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-inspect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-inspect:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-inspect/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-inspect/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-inspect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-inspect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-inspect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-inspect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-inspect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-inspect-inspect-deffile:

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