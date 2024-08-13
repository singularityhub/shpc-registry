---
layout: container
name:  "quay.io/biocontainers/bioconductor-regioner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-regioner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-regioner/container.yaml"
updated_at: "2024-08-13 03:19:16.917093"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-regioner"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r3.4.1_0"
 - "1.26.0--r41hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.18.0--r36_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-regioner"
config: {"url": "https://biocontainers.pro/tools/bioconductor-regioner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-regioner", "latest": {"1.34.0--r43hdfd78af_0": "sha256:731f52715342ae820a37c9391ff73cb398e8642f22f8f954ec96b0e066d71668"}, "tags": {"1.8.1--r3.4.1_0": "sha256:09c82a98bea7461fcec17074793e7f39ac6f7e5161825e8853f967d7ea8a6533", "1.26.0--r41hdfd78af_0": "sha256:79002fdd61e933c68af16e0dbd2ed4d0bbbea65c84c2c7484672f771bac8953f", "1.24.0--r41hdfd78af_0": "sha256:8b62dc5851ccb9c446021a0c334644f022b4387d6be009975ad68ac0b7f7f942", "1.22.0--r40hdfd78af_1": "sha256:c6cd83c832b748f2f3925ce9e10c069aae66183beb3cc24d691fd5cc0de7ae29", "1.20.0--r40_0": "sha256:94e61b3e171e43cef5f5bed8a144ba7fdfaa279452998bd8e236fcd87dc1af2d", "1.18.0--r36_0": "sha256:ff65881bb7e2f1ba51b2d314e7088e03dbba08beb4e874467e21b15189d9325d", "1.30.0--r42hdfd78af_0": "sha256:0011f174b2b47df9f9c2a6afb4886ccc240002464aede5573aa097d91e8f4a69", "1.32.0--r43hdfd78af_0": "sha256:5673629ba963c69e81400bf0fab900f8236839b4ca80f65d8445da0fde18a13e", "1.34.0--r43hdfd78af_0": "sha256:731f52715342ae820a37c9391ff73cb398e8642f22f8f954ec96b0e066d71668"}, "docker": "quay.io/biocontainers/bioconductor-regioner", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-regioner.
shpc-registry automated BioContainers addition for bioconductor-regioner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-regioner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-regioner:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-regioner/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-regioner/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-regioner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regioner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regioner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-regioner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-regioner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-regioner-inspect-deffile:

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