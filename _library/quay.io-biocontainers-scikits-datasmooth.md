---
layout: container
name:  "quay.io/biocontainers/scikits-datasmooth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scikits-datasmooth/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scikits-datasmooth/container.yaml"
updated_at: "2022-10-27 00:48:37.956297"
latest: "0.7.1--pyh145b6a8_2"
container_url: "https://biocontainers.pro/tools/scikits-datasmooth"
aliases:
 - "dsdp5"
versions:
 - "0.7.1--pyh145b6a8_2"
description: "shpc-registry automated BioContainers addition for scikits-datasmooth"
config: {"url": "https://biocontainers.pro/tools/scikits-datasmooth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scikits-datasmooth", "latest": {"0.7.1--pyh145b6a8_2": "sha256:9f2779cc2c518231acd1812cca517886e14fb01642b86bdfc4b848b283dd99f0"}, "tags": {"0.7.1--pyh145b6a8_2": "sha256:9f2779cc2c518231acd1812cca517886e14fb01642b86bdfc4b848b283dd99f0"}, "docker": "quay.io/biocontainers/scikits-datasmooth", "aliases": {"dsdp5": "/usr/local/bin/dsdp5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scikits-datasmooth.
shpc-registry automated BioContainers addition for scikits-datasmooth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scikits-datasmooth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scikits-datasmooth:0.7.1--pyh145b6a8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scikits-datasmooth/0.7.1--pyh145b6a8_2
$ module help quay.io/biocontainers/scikits-datasmooth/0.7.1--pyh145b6a8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scikits-datasmooth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scikits-datasmooth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scikits-datasmooth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scikits-datasmooth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scikits-datasmooth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scikits-datasmooth-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dsdp5

```bash
$ singularity exec <container> /usr/local/bin/dsdp5
$ podman run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
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