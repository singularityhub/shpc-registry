---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsalightning"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsalightning/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsalightning/container.yaml"
updated_at: "2024-02-27 02:26:01.098158"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsalightning"
aliases:
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
description: "shpc-registry automated BioContainers addition for bioconductor-gsalightning"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsalightning", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsalightning", "latest": {"1.30.0--r43hdfd78af_0": "sha256:ef791dea9973ab71a4ee11fdc8cc8ad8dea0c9b2f5bc11976b14910975cb4be8"}, "tags": {"1.8.0--r341_0": "sha256:45e4ee7d38e318cbf614514c1adbd807f3b06f41722615a9c749ca8aa91c21aa", "1.26.0--r42hdfd78af_0": "sha256:360580432e0f8d4afd7d3b90e6d36d656ff7963069395e5adbec0f717d4c6a1a", "1.22.0--r41hdfd78af_0": "sha256:0684a4c38aa2da43d5e55d84a54cfe2fa2cda3f59760271c5a47ddc064eb5f77", "1.20.0--r41hdfd78af_0": "sha256:ba7762c156656cac4b6f3a7f7d84e96cf3019b3f06d27f9749fbdfd58ffac4b1", "1.18.0--r40hdfd78af_1": "sha256:cbed75a025313f457c73f352106cd10c9f91fe1eac97852a760e55f7abb56372", "1.16.0--r40_0": "sha256:fb4e74dec5d1a6e1091c702ae83fe35df3d6d62071ec7cf3b313fb565af497f4", "1.28.0--r43hdfd78af_0": "sha256:165042a2ae5a8d5ad2508edeb066100c39d22e8d209c1873cc8219310c637fb7", "1.30.0--r43hdfd78af_0": "sha256:ef791dea9973ab71a4ee11fdc8cc8ad8dea0c9b2f5bc11976b14910975cb4be8"}, "docker": "quay.io/biocontainers/bioconductor-gsalightning", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsalightning.
shpc-registry automated BioContainers addition for bioconductor-gsalightning
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsalightning
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsalightning:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsalightning/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsalightning/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsalightning-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsalightning-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsalightning-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsalightning-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsalightning-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsalightning-inspect-deffile:

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