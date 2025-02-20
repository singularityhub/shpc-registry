---
layout: container
name:  "quay.io/biocontainers/bioconductor-qdnaseq.mm10"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qdnaseq.mm10/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qdnaseq.mm10/container.yaml"
updated_at: "2025-02-20 03:35:19.568434"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qdnaseq.mm10"
aliases:
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_1"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_1"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qdnaseq.mm10"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qdnaseq.mm10", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qdnaseq.mm10", "latest": {"1.36.0--r44hdfd78af_0": "sha256:e5a037bee8f62d28f74f4b75aafd950c14147f9f58ccb33aaabff890605fe95f"}, "tags": {"1.8.0--r3.4.1_1": "sha256:2083914211afc4b5e49822fc8849a05b9f70b9e30e30791bf7cde03c80aa39b5", "1.28.0--r42hdfd78af_0": "sha256:e0593af5e2b4639b73424e72c698341d4e5848b9a3cfb75d99425c1ce00a7bdd", "1.24.0--r41hdfd78af_1": "sha256:dd7eb66a7b3572aa9be05b2b8391b661022fbc3916b5fe576da390e93e982712", "1.22.0--r41hdfd78af_0": "sha256:670d0cbfc21d36ad9be93f5054a1e92f20412f4561e600e9045d309df5c613f3", "1.20.0--r40hdfd78af_1": "sha256:904c8b25435ed233e00f382e371e99684a88e7d7e89e7d3f742824e5368bc04f", "1.18.0--r40_0": "sha256:44c75399d3dc415f6f0787a346a6bea803413465112780e7762ae09aaacb49dd", "1.30.0--r43hdfd78af_0": "sha256:42d1e5edc4a08f508132042a93bab2d0b8187970e6fca8dbf50261983443d702", "1.32.0--r43hdfd78af_0": "sha256:11a0c4b6e0a39c2b1d60fdc3d85bc2e67a9a657e958ec2c6402a7446dc19ed76", "1.36.0--r44hdfd78af_0": "sha256:e5a037bee8f62d28f74f4b75aafd950c14147f9f58ccb33aaabff890605fe95f"}, "docker": "quay.io/biocontainers/bioconductor-qdnaseq.mm10", "aliases": {"wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qdnaseq.mm10.
shpc-registry automated BioContainers addition for bioconductor-qdnaseq.mm10
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qdnaseq.mm10
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qdnaseq.mm10:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qdnaseq.mm10/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-qdnaseq.mm10/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qdnaseq.mm10-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qdnaseq.mm10-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qdnaseq.mm10-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qdnaseq.mm10-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qdnaseq.mm10-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qdnaseq.mm10-inspect-deffile:

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