---
layout: container
name:  "quay.io/biocontainers/cmv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmv/container.yaml"
updated_at: "2023-09-16 02:42:19.265247"
latest: "1.0.8--1"
container_url: "https://biocontainers.pro/tools/cmv"
aliases:
 - "CMCV"
 - "CMCWStoCMCV"
 - "CMCtoHMMC"
 - "CMV"
 - "CMVJson"
 - "HMMCV"
 - "HMMCtoCMC"
 - "HMMV"
versions:
 - "1.0.8--1"
description: "shpc-registry automated BioContainers addition for cmv"
config: {"url": "https://biocontainers.pro/tools/cmv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cmv", "latest": {"1.0.8--1": "sha256:ed32fe1d4399560176fe846747850541dabab2c53a14bc0da88a1481f41ccaf2"}, "tags": {"1.0.8--1": "sha256:ed32fe1d4399560176fe846747850541dabab2c53a14bc0da88a1481f41ccaf2"}, "docker": "quay.io/biocontainers/cmv", "aliases": {"CMCV": "/usr/local/bin/CMCV", "CMCWStoCMCV": "/usr/local/bin/CMCWStoCMCV", "CMCtoHMMC": "/usr/local/bin/CMCtoHMMC", "CMV": "/usr/local/bin/CMV", "CMVJson": "/usr/local/bin/CMVJson", "HMMCV": "/usr/local/bin/HMMCV", "HMMCtoCMC": "/usr/local/bin/HMMCtoCMC", "HMMV": "/usr/local/bin/HMMV"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmv.
shpc-registry automated BioContainers addition for cmv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmv:1.0.8--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmv/1.0.8--1
$ module help quay.io/biocontainers/cmv/1.0.8--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CMCV

```bash
$ singularity exec <container> /usr/local/bin/CMCV
$ podman run --it --rm --entrypoint /usr/local/bin/CMCV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CMCV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CMCWStoCMCV

```bash
$ singularity exec <container> /usr/local/bin/CMCWStoCMCV
$ podman run --it --rm --entrypoint /usr/local/bin/CMCWStoCMCV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CMCWStoCMCV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CMCtoHMMC

```bash
$ singularity exec <container> /usr/local/bin/CMCtoHMMC
$ podman run --it --rm --entrypoint /usr/local/bin/CMCtoHMMC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CMCtoHMMC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CMV

```bash
$ singularity exec <container> /usr/local/bin/CMV
$ podman run --it --rm --entrypoint /usr/local/bin/CMV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CMV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CMVJson

```bash
$ singularity exec <container> /usr/local/bin/CMVJson
$ podman run --it --rm --entrypoint /usr/local/bin/CMVJson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CMVJson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HMMCV

```bash
$ singularity exec <container> /usr/local/bin/HMMCV
$ podman run --it --rm --entrypoint /usr/local/bin/HMMCV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HMMCV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HMMCtoCMC

```bash
$ singularity exec <container> /usr/local/bin/HMMCtoCMC
$ podman run --it --rm --entrypoint /usr/local/bin/HMMCtoCMC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HMMCtoCMC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HMMV

```bash
$ singularity exec <container> /usr/local/bin/HMMV
$ podman run --it --rm --entrypoint /usr/local/bin/HMMV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HMMV   -v ${PWD} -w ${PWD} <container> -c " $@"
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