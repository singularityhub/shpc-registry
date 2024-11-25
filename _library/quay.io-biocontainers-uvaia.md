---
layout: container
name:  "quay.io/biocontainers/uvaia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uvaia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/uvaia/container.yaml"
updated_at: "2024-11-25 04:01:33.023134"
latest: "2.0.1--h8bd2d3b_2"
container_url: "https://biocontainers.pro/tools/uvaia"
aliases:
 - "uvaia"
 - "uvaia_legacy"
 - "uvaiaball"
 - "uvaiaclust"
 - "uvaialign"
versions:
 - "2.0.1--hc308579_0"
 - "2.0.1--h8bd2d3b_2"
description: "shpc-registry automated BioContainers addition for uvaia"
config: {"url": "https://biocontainers.pro/tools/uvaia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for uvaia", "latest": {"2.0.1--h8bd2d3b_2": "sha256:851e6c97b98a3e2d271e86332d449bb94da82c4e2606f1dc8291cfe6acebfb13"}, "tags": {"2.0.1--hc308579_0": "sha256:de75ff534bbc25d266e2af1c439b3d9ed0837b63db06e4cc74bb1450b669fb4c", "2.0.1--h8bd2d3b_2": "sha256:851e6c97b98a3e2d271e86332d449bb94da82c4e2606f1dc8291cfe6acebfb13"}, "docker": "quay.io/biocontainers/uvaia", "aliases": {"uvaia": "/usr/local/bin/uvaia", "uvaia_legacy": "/usr/local/bin/uvaia_legacy", "uvaiaball": "/usr/local/bin/uvaiaball", "uvaiaclust": "/usr/local/bin/uvaiaclust", "uvaialign": "/usr/local/bin/uvaialign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/uvaia.
shpc-registry automated BioContainers addition for uvaia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uvaia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uvaia:2.0.1--h8bd2d3b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uvaia/2.0.1--h8bd2d3b_2
$ module help quay.io/biocontainers/uvaia/2.0.1--h8bd2d3b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uvaia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uvaia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uvaia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uvaia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uvaia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uvaia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uvaia

```bash
$ singularity exec <container> /usr/local/bin/uvaia
$ podman run --it --rm --entrypoint /usr/local/bin/uvaia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvaia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvaia_legacy

```bash
$ singularity exec <container> /usr/local/bin/uvaia_legacy
$ podman run --it --rm --entrypoint /usr/local/bin/uvaia_legacy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvaia_legacy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvaiaball

```bash
$ singularity exec <container> /usr/local/bin/uvaiaball
$ podman run --it --rm --entrypoint /usr/local/bin/uvaiaball   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvaiaball   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvaiaclust

```bash
$ singularity exec <container> /usr/local/bin/uvaiaclust
$ podman run --it --rm --entrypoint /usr/local/bin/uvaiaclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvaiaclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvaialign

```bash
$ singularity exec <container> /usr/local/bin/uvaialign
$ podman run --it --rm --entrypoint /usr/local/bin/uvaialign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvaialign   -v ${PWD} -w ${PWD} <container> -c " $@"
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