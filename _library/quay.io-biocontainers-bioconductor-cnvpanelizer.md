---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvpanelizer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvpanelizer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvpanelizer/container.yaml"
updated_at: "2023-12-27 03:02:47.296306"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvpanelizer"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.18.0--r36_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvpanelizer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvpanelizer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvpanelizer", "latest": {"1.34.0--r43hdfd78af_0": "sha256:171af82fb14b89d9135c02568369d78ede36d6414329f5d8617a09fab353d4bd"}, "tags": {"1.8.0--r3.4.1_0": "sha256:f77929b5625af7599624cec042d5e04a334424acf75c75531050b53d594272bb", "1.30.0--r42hdfd78af_0": "sha256:b2a04bb9207ad5f3a4b9e6f6a304fce6a23bc5cf0d814b85b1fc2df1944d2418", "1.24.0--r41hdfd78af_0": "sha256:39394c7f627fc34a0b78e1961eb32a94627511c5124f8ad7c7a60a16fa38eda7", "1.22.0--r40hdfd78af_1": "sha256:b041c4554d2cd666c8017132e9be33033bd4a425c60c1908d75ecef9f9575047", "1.20.0--r40_0": "sha256:ab992494693f27272ec0f31ca88e569487baaf88370fa2584fb290dc94e50e21", "1.18.0--r36_0": "sha256:6dd8c14e98d5b995d1ffdcebc571130e17071f8d580262f8665d7e48be056b13", "1.32.0--r43hdfd78af_0": "sha256:497eb805fc21b5e5f3c2223b524e46b363222585976539393382f44ec12aa403", "1.34.0--r43hdfd78af_0": "sha256:171af82fb14b89d9135c02568369d78ede36d6414329f5d8617a09fab353d4bd"}, "docker": "quay.io/biocontainers/bioconductor-cnvpanelizer", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvpanelizer.
shpc-registry automated BioContainers addition for bioconductor-cnvpanelizer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvpanelizer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvpanelizer:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvpanelizer/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvpanelizer/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvpanelizer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvpanelizer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvpanelizer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvpanelizer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvpanelizer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvpanelizer-inspect-deffile:

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