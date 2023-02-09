---
layout: container
name:  "quay.io/biocontainers/bioconductor-jaspar2016"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-jaspar2016/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-jaspar2016/container.yaml"
updated_at: "2023-02-09 00:00:08.423510"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-jaspar2016"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.25.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_1"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-jaspar2016"
config: {"url": "https://biocontainers.pro/tools/bioconductor-jaspar2016", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-jaspar2016", "latest": {"1.26.0--r42hdfd78af_0": "sha256:13dd0ce9b13f1580afcf8fd65511dfaa15edaa976dd920f9edac92c9e3c244d1"}, "tags": {"1.8.0--r341_0": "sha256:61efef25d5a530838035d8467e1e9f5d27ce253f768684723a457ab90c6827ca", "1.26.0--r42hdfd78af_0": "sha256:13dd0ce9b13f1580afcf8fd65511dfaa15edaa976dd920f9edac92c9e3c244d1", "1.25.0--r42hdfd78af_0": "sha256:88ac9d26c142c44470ce526647abf9ce51bc7640cb999f5ecfcdd6fc1baa1472", "1.22.0--r41hdfd78af_1": "sha256:a3f4ea0f91aad1350c4e1c1bd1fc2558708b79f1e3901110df32fa2f97ec7e2e", "1.20.0--r41hdfd78af_0": "sha256:2aa951ebd48fe9247260845578753615a371cdda98772946b58e8a37c8b8d935", "1.18.0--r40hdfd78af_1": "sha256:53f7cec9409364fe80495ed2b040637bd51f25187f4549e24f291465606019d0"}, "docker": "quay.io/biocontainers/bioconductor-jaspar2016", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-jaspar2016.
shpc-registry automated BioContainers addition for bioconductor-jaspar2016
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-jaspar2016
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-jaspar2016:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-jaspar2016/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-jaspar2016/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-jaspar2016-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jaspar2016-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jaspar2016-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-jaspar2016-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-jaspar2016-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-jaspar2016-inspect-deffile:

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