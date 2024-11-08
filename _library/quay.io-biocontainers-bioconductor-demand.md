---
layout: container
name:  "quay.io/biocontainers/bioconductor-demand"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-demand/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-demand/container.yaml"
updated_at: "2024-11-08 03:26:28.592120"
latest: "1.32.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-demand"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-demand"
config: {"url": "https://biocontainers.pro/tools/bioconductor-demand", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-demand", "latest": {"1.32.0--r43hdfd78af_1": "sha256:54e58ccd87f7b63a7a0d173c39c5116c77969efef58240036029a222626bd1f8"}, "tags": {"1.8.0--r3.4.1_0": "sha256:f813869970b5cc6592f04a4dea4b01cfb9610cd958006fc342ca6b16f4cb946c", "1.28.0--r42hdfd78af_0": "sha256:6fb6f4d2c5faf5dc749dff18ec69e82dab523a9ce43d2f5687f16377d7e188ac", "1.24.0--r41hdfd78af_0": "sha256:fe0e4c0f9e9ac23894725477652ff0f1ef83468eb934e5e760d56b947cb9e379", "1.22.0--r41hdfd78af_0": "sha256:28c8f70bd4f944f6b786bcc7936f08b9f5c7a5e4caf82b2bde4e0d1dc0e1a329", "1.20.0--r40hdfd78af_1": "sha256:963b60007d545683108957b98e5ec1e6a9cc594adc796e20e80f94662ca14ce9", "1.18.0--r40_0": "sha256:c42beef5799a8d9ce4f2676326c87f04f64314394c27c96f90a4ff678578cccf", "1.30.0--r43hdfd78af_0": "sha256:ff24221c7099f943774cc29ed1d2c88625452794a704204238753efa1c4307d5", "1.32.0--r43hdfd78af_1": "sha256:54e58ccd87f7b63a7a0d173c39c5116c77969efef58240036029a222626bd1f8"}, "docker": "quay.io/biocontainers/bioconductor-demand", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-demand.
shpc-registry automated BioContainers addition for bioconductor-demand
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-demand
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-demand:1.32.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-demand/1.32.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-demand/1.32.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-demand-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-demand-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-demand-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-demand-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-demand-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-demand-inspect-deffile:

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