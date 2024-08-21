---
layout: container
name:  "quay.io/biocontainers/dsrc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dsrc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dsrc/container.yaml"
updated_at: "2024-08-21 03:11:23.163600"
latest: "2015.06.04--hdcf5f25_8"
container_url: "https://biocontainers.pro/tools/dsrc"
aliases:
 - "dsrc"
versions:
 - "2015.06.04--h7ff8a90_4"
 - "2015.06.04--h21ec9f0_6"
 - "2015.06.04--hdcf5f25_7"
 - "2015.06.04--hdcf5f25_8"
description: "shpc-registry automated BioContainers addition for dsrc"
config: {"url": "https://biocontainers.pro/tools/dsrc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dsrc", "latest": {"2015.06.04--hdcf5f25_8": "sha256:fe1b0e162e2c62abe7368a76b8ac7877b29e1888ace6f668de527072e6d15b85"}, "tags": {"2015.06.04--h7ff8a90_4": "sha256:c09ee47a183d8abed7ca2de63e23f2e1e02e185328a5096e786ddd75109964ef", "2015.06.04--h21ec9f0_6": "sha256:09f329357fc3b7ad457bc67b7eaba8dfbcaa5af18891d2a71643792cfefefaaf", "2015.06.04--hdcf5f25_7": "sha256:e5887fa5b0862c813e0702aa037999862ab114208eb92574828fbebe53eb93e8", "2015.06.04--hdcf5f25_8": "sha256:fe1b0e162e2c62abe7368a76b8ac7877b29e1888ace6f668de527072e6d15b85"}, "docker": "quay.io/biocontainers/dsrc", "aliases": {"dsrc": "/usr/local/bin/dsrc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dsrc.
shpc-registry automated BioContainers addition for dsrc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dsrc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dsrc:2015.06.04--hdcf5f25_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dsrc/2015.06.04--hdcf5f25_8
$ module help quay.io/biocontainers/dsrc/2015.06.04--hdcf5f25_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dsrc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dsrc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dsrc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dsrc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dsrc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dsrc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dsrc

```bash
$ singularity exec <container> /usr/local/bin/dsrc
$ podman run --it --rm --entrypoint /usr/local/bin/dsrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsrc   -v ${PWD} -w ${PWD} <container> -c " $@"
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