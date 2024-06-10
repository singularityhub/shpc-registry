---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcgh"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcgh/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcgh/container.yaml"
updated_at: "2024-06-10 03:02:52.008021"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcgh"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcgh"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcgh", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcgh", "latest": {"1.32.0--r43hdfd78af_0": "sha256:e525dff17fb77c1beb25ba6689ffe68149836dfc181b6b36887a6a74b4730647"}, "tags": {"1.8.1--r3.4.1_0": "sha256:1ff2407f3fcbdf9d117e44459b083b155a6d043d477adc794f47c1ce66f71634", "1.24.0--r41hdfd78af_0": "sha256:afc3cf7d32766dd1b8737df79ae31f3aded8fe1ac0b62fb6079f4daa1290f98e", "1.22.0--r41hdfd78af_0": "sha256:0ddf7b9c5829de449ce6e04ae9211f6951358e188854ed029a0cf8b9b9175391", "1.20.0--r40hdfd78af_1": "sha256:deda850dba3f07ba9d94030a2fb90a1c4a6cd602fc0b6e4d31af8b5572746323", "1.18.0--r40_0": "sha256:77a74237b619c561e0858e7ccb6397b76f5df8c287b719b9268eb6bc8d79410e", "1.16.0--r36_0": "sha256:c8d5e6d31fd1f3dac1b0eb51e26c84266a504792cec0c6e00dcf714db7317ad1", "1.28.0--r42hdfd78af_0": "sha256:646aa94ad0b8d2ebfa333d437d5310798c7976b0f7b9fcfe76a4da840f85776f", "1.30.0--r43hdfd78af_0": "sha256:550c773129f502b90830f2f3c62f3243147a1b258c9e3a29abaa4c55f97a057e", "1.32.0--r43hdfd78af_0": "sha256:e525dff17fb77c1beb25ba6689ffe68149836dfc181b6b36887a6a74b4730647"}, "docker": "quay.io/biocontainers/bioconductor-rcgh", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcgh.
shpc-registry automated BioContainers addition for bioconductor-rcgh
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcgh
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcgh:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcgh/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcgh/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcgh-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcgh-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcgh-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcgh-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcgh-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcgh-inspect-deffile:

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