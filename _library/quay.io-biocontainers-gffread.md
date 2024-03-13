---
layout: container
name:  "quay.io/biocontainers/gffread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gffread/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gffread/container.yaml"
updated_at: "2024-03-13 02:27:06.988758"
latest: "0.12.7--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/gffread"
aliases:
 - "gffread"
versions:
 - "0.9.9--1"
 - "0.12.7--hd03093a_1"
 - "0.11.7--h8b12597_0"
 - "0.9.12--0"
 - "0.12.7--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for gffread"
config: {"url": "https://biocontainers.pro/tools/gffread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gffread", "latest": {"0.12.7--hdcf5f25_3": "sha256:84214c0cd852ccd9995ce649269602e4cc4ef2f8b5d3920c7ee7b79050c07fc6"}, "tags": {"0.9.9--1": "sha256:419e1859e4fdd30217071a75fab40058e89aaaae142615d8102ac8985227e75f", "0.12.7--hd03093a_1": "sha256:f46049f79cc002aaa23c31eb30b4ee7037c76c1429217a15792b242e0dbf365d", "0.11.7--h8b12597_0": "sha256:90c4c2a33e2595b1788bf71e2db0d72fe6daa7e16893f9da81ccc4d8bb384457", "0.9.12--0": "sha256:8d14cc2f9d2b968bd7bfd92dde5800a2b10f14787547df8ad5e626ee69ff4154", "0.12.7--hdcf5f25_3": "sha256:84214c0cd852ccd9995ce649269602e4cc4ef2f8b5d3920c7ee7b79050c07fc6"}, "docker": "quay.io/biocontainers/gffread", "aliases": {"gffread": "/usr/local/bin/gffread"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gffread.
shpc-registry automated BioContainers addition for gffread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gffread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gffread:0.12.7--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gffread/0.12.7--hdcf5f25_3
$ module help quay.io/biocontainers/gffread/0.12.7--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gffread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gffread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gffread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gffread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gffread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gffread-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
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