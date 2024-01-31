---
layout: container
name:  "quay.io/biocontainers/bioconductor-qvalue"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qvalue/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qvalue/container.yaml"
updated_at: "2024-01-31 02:55:36.825237"
latest: "2.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qvalue"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.26.0--r41hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r40hdfd78af_1"
 - "2.20.0--r40_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qvalue"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qvalue", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qvalue", "latest": {"2.34.0--r43hdfd78af_0": "sha256:fb5e66ed475f69202689a5288ed0d96e4eaa95f4513a90c24d9baaa1e083e951"}, "tags": {"2.8.0--r3.4.1_0": "sha256:c8c30b6041ad9035bcdd9685ad6b35ec40afc6c617cdccb9f0d1299af2336703", "2.30.0--r42hdfd78af_0": "sha256:95383d3b0f3ef3c4034adfb9d6caecf6d3aec328aa25bf7466ba8cb90a625e30", "2.26.0--r41hdfd78af_0": "sha256:1a139231997e17fc976c5dafdefbf9416a64528aec86addbd15a2433a09176b1", "2.24.0--r41hdfd78af_0": "sha256:de2a74af76343fe7a5d0f1ca1ad5014438a713308fb44b89607135de29330832", "2.22.0--r40hdfd78af_1": "sha256:2cceccfa74a6ba76d5705eb57835cc06fb2b466bba1f74fd8f9c8d9655658cc2", "2.20.0--r40_0": "sha256:c5be808ae5a803d49e7538a753cf28fd22ddc1c747296bc1949583a336633289", "2.32.0--r43hdfd78af_0": "sha256:74aba1886906f7ea0ca615f89f18d8b1fa9fe0b632b894a619d0281f626a3023", "2.34.0--r43hdfd78af_0": "sha256:fb5e66ed475f69202689a5288ed0d96e4eaa95f4513a90c24d9baaa1e083e951"}, "docker": "quay.io/biocontainers/bioconductor-qvalue", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qvalue.
shpc-registry automated BioContainers addition for bioconductor-qvalue
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qvalue
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qvalue:2.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qvalue/2.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-qvalue/2.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qvalue-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qvalue-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qvalue-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qvalue-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qvalue-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qvalue-inspect-deffile:

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