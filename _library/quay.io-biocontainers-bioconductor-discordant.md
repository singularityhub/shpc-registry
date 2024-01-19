---
layout: container
name:  "quay.io/biocontainers/bioconductor-discordant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-discordant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-discordant/container.yaml"
updated_at: "2024-01-19 02:31:40.866941"
latest: "1.26.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-discordant"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_1"
 - "1.22.0--r42hc247a5b_0"
 - "1.18.0--r41hc0cfd56_2"
 - "1.16.0--r41hd029910_0"
 - "1.14.0--r40hd029910_1"
 - "1.12.0--r40h037d062_0"
 - "1.22.0--r42hf17093f_1"
 - "1.24.0--r43hf17093f_0"
 - "1.26.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-discordant"
config: {"url": "https://biocontainers.pro/tools/bioconductor-discordant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-discordant", "latest": {"1.26.0--r43hf17093f_0": "sha256:2d074cda624956db8053dfca60d81a26d11448f5822d8883906d29ead2143bb0"}, "tags": {"1.8.0--r36h516909a_1": "sha256:858d2dacc35d4146066f13d871a6c3a06af47c844d06be0fd268c8dfff287cc3", "1.22.0--r42hc247a5b_0": "sha256:cb1f5726b49430ef8b847643f091f0f2bd5d01e8e88f803d92d0e8e49df9e06a", "1.18.0--r41hc0cfd56_2": "sha256:6405ea7cccad492e2d1ab380147b897f7929d3a878015c87de8c99379849b67c", "1.16.0--r41hd029910_0": "sha256:2c3cf0ddd5ca642db0e6b1901fd4003144a9504571e2ea9d1fe46765ddb0750c", "1.14.0--r40hd029910_1": "sha256:d7b9ef3fad53a4a89f38b7597895ca937798d1a3c7fd93dfaa3d5e6f6205dd22", "1.12.0--r40h037d062_0": "sha256:c56617eca802ccc279cc08c317d5e8f25065921b82c23953a7aca00b082c23ba", "1.22.0--r42hf17093f_1": "sha256:ef717164bc6bc655efdcfd3ab4be5619e6192868f00807b8460f7995aaa18343", "1.24.0--r43hf17093f_0": "sha256:240b9fbc69324a83192340b1ee7b06e7c1b78fbb3cebf0865473281f48894049", "1.26.0--r43hf17093f_0": "sha256:2d074cda624956db8053dfca60d81a26d11448f5822d8883906d29ead2143bb0"}, "docker": "quay.io/biocontainers/bioconductor-discordant", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-discordant.
shpc-registry automated BioContainers addition for bioconductor-discordant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-discordant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-discordant:1.26.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-discordant/1.26.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-discordant/1.26.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-discordant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-discordant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-discordant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-discordant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-discordant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-discordant-inspect-deffile:

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