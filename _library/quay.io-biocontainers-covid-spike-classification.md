---
layout: container
name:  "quay.io/biocontainers/covid-spike-classification"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/covid-spike-classification/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/covid-spike-classification/container.yaml"
updated_at: "2022-10-27 00:36:22.413993"
latest: "0.6.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/covid-spike-classification"
aliases:
 - "covid-spike-classification"
 - "tracy"
versions:
 - "0.6.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for covid-spike-classification"
config: {"url": "https://biocontainers.pro/tools/covid-spike-classification", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for covid-spike-classification", "latest": {"0.6.4--pyhdfd78af_0": "sha256:291de9e23eabe10ef356d8c5f6449dc9d1a8dfc9dff52d4f58b8ab4209f624da"}, "tags": {"0.6.4--pyhdfd78af_0": "sha256:291de9e23eabe10ef356d8c5f6449dc9d1a8dfc9dff52d4f58b8ab4209f624da"}, "docker": "quay.io/biocontainers/covid-spike-classification", "aliases": {"covid-spike-classification": "/usr/local/bin/covid-spike-classification", "tracy": "/usr/local/bin/tracy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/covid-spike-classification.
shpc-registry automated BioContainers addition for covid-spike-classification
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/covid-spike-classification
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/covid-spike-classification:0.6.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/covid-spike-classification/0.6.4--pyhdfd78af_0
$ module help quay.io/biocontainers/covid-spike-classification/0.6.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### covid-spike-classification-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### covid-spike-classification-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### covid-spike-classification-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### covid-spike-classification-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### covid-spike-classification-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### covid-spike-classification-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### covid-spike-classification

```bash
$ singularity exec <container> /usr/local/bin/covid-spike-classification
$ podman run --it --rm --entrypoint /usr/local/bin/covid-spike-classification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covid-spike-classification   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tracy

```bash
$ singularity exec <container> /usr/local/bin/tracy
$ podman run --it --rm --entrypoint /usr/local/bin/tracy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tracy   -v ${PWD} -w ${PWD} <container> -c " $@"
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