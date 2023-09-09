---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipenrich"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipenrich/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipenrich/container.yaml"
updated_at: "2023-09-09 03:02:21.446402"
latest: "2.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipenrich"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.22.0--r42hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.0--r40_0"
 - "2.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipenrich"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipenrich", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipenrich", "latest": {"2.24.0--r43hdfd78af_0": "sha256:32eaa4397a5a8df86918ca36646360e8a24ff1886d46b487d2f9339f251cc721"}, "tags": {"2.8.0--r36_1": "sha256:d088e500242b19e18854a58de16092b9244596318478b3aa54f8bd7a0e2506b2", "2.22.0--r42hdfd78af_0": "sha256:a5b321933a875f6f46c84dcd83333ab6a07d0ddf05a85ba4ad956fd9089e9f89", "2.18.0--r41hdfd78af_0": "sha256:7d1b70693aced1fce38b0b62721a6f7178e3330d27f4c08f3b957745c4dd60cf", "2.16.0--r41hdfd78af_0": "sha256:c392ce8569b9fbd8fff75f28eda793f68dd849348f1416828d7cb25da0af5d47", "2.14.0--r40hdfd78af_1": "sha256:634b9441031687bce922c58f93ec1c6a9da63d9ea11a40902f25987ecebecaf6", "2.12.0--r40_0": "sha256:39e39b1d2c297aa0e821f8fcee6bcd769aa9b650ef6c0e130b3b06e4d08a3bed", "2.24.0--r43hdfd78af_0": "sha256:32eaa4397a5a8df86918ca36646360e8a24ff1886d46b487d2f9339f251cc721"}, "docker": "quay.io/biocontainers/bioconductor-chipenrich", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipenrich.
shpc-registry automated BioContainers addition for bioconductor-chipenrich
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipenrich
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipenrich:2.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipenrich/2.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipenrich/2.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipenrich-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipenrich-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipenrich-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipenrich-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipenrich-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipenrich-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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