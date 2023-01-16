---
layout: container
name:  "quay.io/biocontainers/bioconductor-linnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-linnorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-linnorm/container.yaml"
updated_at: "2023-01-16 03:10:49.094201"
latest: "2.22.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-linnorm"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36he1b5a44_1"
 - "2.22.0--r42hc247a5b_0"
 - "2.18.0--r41hc247a5b_2"
 - "2.16.0--r41h399db7b_0"
 - "2.14.0--r40h399db7b_1"
 - "2.12.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-linnorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-linnorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-linnorm", "latest": {"2.22.0--r42hc247a5b_0": "sha256:de22bcd924bf67b3869effda720f4f09363d1ba3fade69f0525b3a0d56b41082"}, "tags": {"2.8.0--r36he1b5a44_1": "sha256:8dbbbfb37496f8f8b225aae4f84b9507e82bae8c5a3154d3cc56f15dd349d2b2", "2.22.0--r42hc247a5b_0": "sha256:de22bcd924bf67b3869effda720f4f09363d1ba3fade69f0525b3a0d56b41082", "2.18.0--r41hc247a5b_2": "sha256:c2f5e8b06987edf508d11b168cadc6b3fcd4fd90402cb43819fcbd3b00471ed0", "2.16.0--r41h399db7b_0": "sha256:aa8e9b0352b8f16eada182ff143ab3e7c9e27940dbc8de234826e3c0846d281d", "2.14.0--r40h399db7b_1": "sha256:30db0d2f4c3a874f24c40a26ec74bf9083c2737c09fdb8082c9eb1d293ea723c", "2.12.0--r40h5f743cb_0": "sha256:a674c65e2be6fccfcc51cfe5ccd39d7fdd3ae2f338b891b5ff2ba69bd0a9eff3"}, "docker": "quay.io/biocontainers/bioconductor-linnorm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-linnorm.
shpc-registry automated BioContainers addition for bioconductor-linnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-linnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-linnorm:2.22.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-linnorm/2.22.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-linnorm/2.22.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-linnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-linnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-linnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-linnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-linnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-linnorm-inspect-deffile:

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