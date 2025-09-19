---
layout: container
name:  "quay.io/biocontainers/foldmason"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/foldmason/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/foldmason/container.yaml"
updated_at: "2025-09-19 03:10:54.213398"
latest: "3.954d202--h5021889_0"
container_url: "https://biocontainers.pro/tools/foldmason"
aliases:
 - "foldmason"
 - "aria2c"
 - "gawk-5.3.0"
 - "gawkbug"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
versions:
 - "1.763a428--pl5321hb365157_0"
 - "2.7bd21ed--pl5321h5021889_0"
 - "3.954d202--h5021889_0"
description: "singularity registry hpc automated addition for foldmason"
config: {"url": "https://biocontainers.pro/tools/foldmason", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for foldmason", "latest": {"3.954d202--h5021889_0": "sha256:b3ea6f3d06ffc1835f212c0e519397b8f14a3b37ed9e19e5ec1cdf05b4eb9781"}, "tags": {"1.763a428--pl5321hb365157_0": "sha256:7c1d4d0b6cbf5ec112228712fb09b31ef36ee4c863e9a8bf5bb846c4fe72b1aa", "2.7bd21ed--pl5321h5021889_0": "sha256:8c381feabb35ee7cb15acd683d0e34a6351245d1988d021a118b1811bd0e8515", "3.954d202--h5021889_0": "sha256:b3ea6f3d06ffc1835f212c0e519397b8f14a3b37ed9e19e5ec1cdf05b4eb9781"}, "docker": "quay.io/biocontainers/foldmason", "aliases": {"foldmason": "/usr/local/bin/foldmason", "aria2c": "/usr/local/bin/aria2c", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "gawkbug": "/usr/local/bin/gawkbug", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/foldmason.
singularity registry hpc automated addition for foldmason
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/foldmason
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/foldmason:3.954d202--h5021889_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/foldmason/3.954d202--h5021889_0
$ module help quay.io/biocontainers/foldmason/3.954d202--h5021889_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### foldmason-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### foldmason-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### foldmason-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### foldmason-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### foldmason-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### foldmason-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### foldmason

```bash
$ singularity exec <container> /usr/local/bin/foldmason
$ podman run --it --rm --entrypoint /usr/local/bin/foldmason   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldmason   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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