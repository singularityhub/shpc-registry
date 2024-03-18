---
layout: container
name:  "quay.io/biocontainers/bioconductor-isomirs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-isomirs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-isomirs/container.yaml"
updated_at: "2024-03-18 23:29:30.120280"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-isomirs"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.1--r40hdfd78af_0"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-isomirs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-isomirs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-isomirs", "latest": {"1.30.0--r43hdfd78af_0": "sha256:351367e1ecb33b3e6cddf5e9b40cb4c6197628ad5cbb7bda5bc97fa310f62c96"}, "tags": {"1.8.0--r341_0": "sha256:fb4cddf8f3350e118dd1005c53d22ddd0d1cdfeddd9676b3307a9246ead47487", "1.26.0--r42hdfd78af_0": "sha256:b60a14faeb298f34e987c0811df6c163a60121469793271221ae034fe5237dc9", "1.22.0--r41hdfd78af_0": "sha256:c636315357650362f16fd1f2468d69197db2233448f618c9ad18e87697b8898f", "1.20.0--r41hdfd78af_0": "sha256:e02d2984d9fbbd46392c0cf03a3bec44bea18be8dac8f9c37aee1d2256d0aaea", "1.18.1--r40hdfd78af_0": "sha256:458a7a523ccdbcf9bd5be997fd0c87c9561a111dd6371de68152f4fb96f5c58b", "1.16.0--r40_0": "sha256:623435a757494e761ac71d84d98354033f8ceeb809362a1b72754d75faa3086f", "1.28.0--r43hdfd78af_0": "sha256:c90453feda86498b879c69356afc0382e9f8adaace8cceaae45952c99f01fd78", "1.30.0--r43hdfd78af_0": "sha256:351367e1ecb33b3e6cddf5e9b40cb4c6197628ad5cbb7bda5bc97fa310f62c96"}, "docker": "quay.io/biocontainers/bioconductor-isomirs", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-isomirs.
shpc-registry automated BioContainers addition for bioconductor-isomirs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-isomirs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-isomirs:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-isomirs/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-isomirs/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-isomirs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isomirs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isomirs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-isomirs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-isomirs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-isomirs-inspect-deffile:

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