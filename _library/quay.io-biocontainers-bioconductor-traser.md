---
layout: container
name:  "quay.io/biocontainers/bioconductor-traser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-traser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-traser/container.yaml"
updated_at: "2023-11-05 03:01:52.508652"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-traser"
aliases:
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-traser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-traser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-traser", "latest": {"1.30.0--r43hdfd78af_0": "sha256:2c52ad6871291d9b038df98819a50cf8d4edcb583e0772ca3289093042941e1a"}, "tags": {"1.8.0--r3.4.1_0": "sha256:ef34ce7232f1b369501761674307c246e138205bff7afa7c5321c499e25c5dba", "1.24.0--r41hdfd78af_0": "sha256:a7214d0ae44704a9abfaa3d02fa231ca98186444704affa2b83c275df633d3b4", "1.22.0--r41hdfd78af_0": "sha256:612bb0000c4ee21ce6aaaa9d32bcd2c393b369b0a1ef58c21d98850052551380", "1.20.0--r40hdfd78af_1": "sha256:3c88e3e7e4313f49fcced32ad42d3941ce077dde5c542c30ea61eb5a805b8d09", "1.18.0--r40_0": "sha256:f24446943ac9218413ec3c59872f7bf0b7f17c516879d14f23dcfeb0f3e4faf9", "1.16.0--r36_0": "sha256:3b9d3d6f146db353c00e59d67f7867e20e6f9425f53f81ef86f2046d03f468cf", "1.28.0--r42hdfd78af_0": "sha256:e55b5e0a4784897e009c48a9a09470922aa320a1f71662fbb4f9fe0b3547d4f8", "1.30.0--r43hdfd78af_0": "sha256:2c52ad6871291d9b038df98819a50cf8d4edcb583e0772ca3289093042941e1a"}, "docker": "quay.io/biocontainers/bioconductor-traser", "aliases": {"wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-traser.
shpc-registry automated BioContainers addition for bioconductor-traser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-traser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-traser:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-traser/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-traser/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-traser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-traser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-traser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-traser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-traser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-traser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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