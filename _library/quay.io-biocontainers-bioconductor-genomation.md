---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomation/container.yaml"
updated_at: "2024-05-04 02:47:23.380249"
latest: "1.34.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomation"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.30.0--r42hc247a5b_0"
 - "1.26.0--r41hc247a5b_2"
 - "1.24.0--r41h399db7b_0"
 - "1.22.0--r40h399db7b_1"
 - "1.20.0--r40h5f743cb_0"
 - "1.30.0--r42hf17093f_1"
 - "1.32.0--r43hf17093f_0"
 - "1.34.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomation", "latest": {"1.34.0--r43hf17093f_0": "sha256:87e9eae6f9cd0ca53b1d56565832703fbef4d85da590568e69748d9b5386380b"}, "tags": {"1.8.0--r3.4.1_0": "sha256:f18c747ec80bbd097c90be45c60962c1a542442d64e991ce983faf32dec222dd", "1.30.0--r42hc247a5b_0": "sha256:a31cc30452e0d1b70f112d3831048d6a117ab237d7b5fe4f391b1f76b9629cf5", "1.26.0--r41hc247a5b_2": "sha256:7f617da58f0e66a4e649f588d5669f0ea464aa8e92b71dc65a386d9d85488c1f", "1.24.0--r41h399db7b_0": "sha256:d618028ef07b1164a35992b0e203c5c99fdf52accbbe14dbcd94bf726441add8", "1.22.0--r40h399db7b_1": "sha256:d0abbcdb74012d44aae24c4aca96b914aafb0f21bb8a34f1f9b84bcfcc8da76b", "1.20.0--r40h5f743cb_0": "sha256:d5c84a3d06acb61a4f2c6bc491db6588d935c16a7ad4155f8e8657bd4011c493", "1.30.0--r42hf17093f_1": "sha256:c5147d50a20b9ed6d3601c5e32431b1b5481513b8a3d5855884edc7134c52ced", "1.32.0--r43hf17093f_0": "sha256:18949e3c0c48a81698759cd2e72dfb92eb9d3cd41247a0771319c4e34bf7c773", "1.34.0--r43hf17093f_0": "sha256:87e9eae6f9cd0ca53b1d56565832703fbef4d85da590568e69748d9b5386380b"}, "docker": "quay.io/biocontainers/bioconductor-genomation", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomation.
shpc-registry automated BioContainers addition for bioconductor-genomation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomation:1.34.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomation/1.34.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-genomation/1.34.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomation-inspect-deffile:

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