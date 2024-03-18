---
layout: container
name:  "quay.io/biocontainers/bioconductor-protgenerics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-protgenerics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-protgenerics/container.yaml"
updated_at: "2024-03-18 23:38:26.481251"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-protgenerics"
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
description: "shpc-registry automated BioContainers addition for bioconductor-protgenerics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-protgenerics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-protgenerics", "latest": {"1.34.0--r43hdfd78af_0": "sha256:f6823d7b78edbd5aa1dba32098d5e7436a4edd1d980542c1003538c9ca0a661d"}, "tags": {"1.8.0--r3.4.1_0": "sha256:28f0dd18fdb0526851afb31b5e4db6ff686c921bd4ebf3c172e892c7010de8e4", "1.30.0--r42hdfd78af_0": "sha256:f282c900756f5bd0a246dc8a25ee86970b46356e93c30450c7cbac724e4eb6ce", "1.26.0--r41hdfd78af_0": "sha256:7eb96d7afba23d123e5b8896b7d0362858940c3956285b34fe60297ff11c307a", "1.24.0--r41hdfd78af_0": "sha256:44b4b6661cb75ab392a2a97ef130baf4d2eeae7744546ed8819a99d7a07d2556", "1.22.0--r40hdfd78af_1": "sha256:65b8cabe5dd0a0fdfde4a6b6fa4f038a8f62a8b02bcad60eda27bf3ae7f82ee1", "1.20.0--r40_0": "sha256:bc94a1adc8f46c1aa4bd145c08a60bfc0dca7800f167d08bc68ec7e800c1ac8a", "1.32.0--r43hdfd78af_0": "sha256:0a5a7b1fa9290b11764aaf311ddb3039fcfce4ff491fe705922a1a00e5bac49f", "1.34.0--r43hdfd78af_0": "sha256:f6823d7b78edbd5aa1dba32098d5e7436a4edd1d980542c1003538c9ca0a661d"}, "docker": "quay.io/biocontainers/bioconductor-protgenerics", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-protgenerics.
shpc-registry automated BioContainers addition for bioconductor-protgenerics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-protgenerics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-protgenerics:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-protgenerics/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-protgenerics/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-protgenerics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-protgenerics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-protgenerics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-protgenerics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-protgenerics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-protgenerics-inspect-deffile:

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