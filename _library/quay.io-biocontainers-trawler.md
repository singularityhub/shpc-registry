---
layout: container
name:  "quay.io/biocontainers/trawler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trawler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trawler/container.yaml"
updated_at: "2025-05-26 12:22:11.498929"
latest: "2.0--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/trawler"
aliases:
 - "trawler"
 - "dvipdf"
 - "eps2eps"
 - "gs"
 - "gsbj"
 - "gsdj"
 - "gsdj500"
 - "gslj"
 - "gslp"
 - "gsnd"
 - "lprsetup.sh"
versions:
 - "2.0--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for trawler"
config: {"url": "https://biocontainers.pro/tools/trawler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trawler", "latest": {"2.0--hdfd78af_4": "sha256:5877fcd3393731f9b63bf852bfcdf8ec3268feccf8d212bbc81399bad14b743c"}, "tags": {"2.0--hdfd78af_4": "sha256:5877fcd3393731f9b63bf852bfcdf8ec3268feccf8d212bbc81399bad14b743c"}, "docker": "quay.io/biocontainers/trawler", "aliases": {"trawler": "/usr/local/bin/trawler", "dvipdf": "/usr/local/bin/dvipdf", "eps2eps": "/usr/local/bin/eps2eps", "gs": "/usr/local/bin/gs", "gsbj": "/usr/local/bin/gsbj", "gsdj": "/usr/local/bin/gsdj", "gsdj500": "/usr/local/bin/gsdj500", "gslj": "/usr/local/bin/gslj", "gslp": "/usr/local/bin/gslp", "gsnd": "/usr/local/bin/gsnd", "lprsetup.sh": "/usr/local/bin/lprsetup.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trawler.
shpc-registry automated BioContainers addition for trawler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trawler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trawler:2.0--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trawler/2.0--hdfd78af_4
$ module help quay.io/biocontainers/trawler/2.0--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trawler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trawler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trawler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trawler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trawler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trawler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trawler

```bash
$ singularity exec <container> /usr/local/bin/trawler
$ podman run --it --rm --entrypoint /usr/local/bin/trawler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trawler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dvipdf

```bash
$ singularity exec <container> /usr/local/bin/dvipdf
$ podman run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eps2eps

```bash
$ singularity exec <container> /usr/local/bin/eps2eps
$ podman run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gs

```bash
$ singularity exec <container> /usr/local/bin/gs
$ podman run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsbj

```bash
$ singularity exec <container> /usr/local/bin/gsbj
$ podman run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj

```bash
$ singularity exec <container> /usr/local/bin/gsdj
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj500

```bash
$ singularity exec <container> /usr/local/bin/gsdj500
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj500   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj500   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gslj

```bash
$ singularity exec <container> /usr/local/bin/gslj
$ podman run --it --rm --entrypoint /usr/local/bin/gslj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gslj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gslp

```bash
$ singularity exec <container> /usr/local/bin/gslp
$ podman run --it --rm --entrypoint /usr/local/bin/gslp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gslp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnd

```bash
$ singularity exec <container> /usr/local/bin/gsnd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lprsetup.sh

```bash
$ singularity exec <container> /usr/local/bin/lprsetup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lprsetup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lprsetup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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