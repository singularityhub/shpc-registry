---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirnameconverter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirnameconverter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirnameconverter/container.yaml"
updated_at: "2024-11-22 03:18:13.044184"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirnameconverter"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirnameconverter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirnameconverter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirnameconverter", "latest": {"1.30.0--r43hdfd78af_0": "sha256:1ef4fe31a7638331e52fd4464e969bdcc25f3d8bc0a93096554f6da17d6b60f9"}, "tags": {"1.8.0--r341_0": "sha256:c7b8f79045cb73db947d10bc9ac503ebb5d7faff6407038679f2a76988841f1f", "1.26.0--r42hdfd78af_0": "sha256:a5e6e1f07807caea248f4870134a01667f5aeb947d2edf647da83ed77e01929f", "1.22.0--r41hdfd78af_0": "sha256:36419bb27fda220a7bb7dc60ca8ebd79ff4072fea7bf73cf4f34992ca0520d1e", "1.20.0--r41hdfd78af_0": "sha256:48765810bf9acc0635e8641079a2012549379bd2c40725efa263c8683323714f", "1.18.0--r40hdfd78af_1": "sha256:8cc9918935f3a5d561c4f00b5483bfaabb6e8faaae9bb824834473e6a120f1ea", "1.16.0--r40_0": "sha256:ff1f8c2dfa8d6307e3dbe1f6f57a271ebc489371a412188cd42c06cd5b11e564", "1.28.0--r43hdfd78af_0": "sha256:389ca3ceb8499323948849ea93d8351d1381a1501c94f22ff46c524f966b4c0d", "1.30.0--r43hdfd78af_0": "sha256:1ef4fe31a7638331e52fd4464e969bdcc25f3d8bc0a93096554f6da17d6b60f9"}, "docker": "quay.io/biocontainers/bioconductor-mirnameconverter", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirnameconverter.
shpc-registry automated BioContainers addition for bioconductor-mirnameconverter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnameconverter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnameconverter:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirnameconverter/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirnameconverter/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirnameconverter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnameconverter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnameconverter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirnameconverter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirnameconverter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirnameconverter-inspect-deffile:

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