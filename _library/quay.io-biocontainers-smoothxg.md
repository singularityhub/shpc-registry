---
layout: container
name:  "quay.io/biocontainers/smoothxg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smoothxg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smoothxg/container.yaml"
updated_at: "2022-12-12 03:21:58.238875"
latest: "0.6.7--hfb1f815_1"
container_url: "https://biocontainers.pro/tools/smoothxg"
aliases:
 - "smoothxg"
versions:
 - "0.6.5--hfb1f815_2"
 - "0.6.7--hfb1f815_1"
description: "shpc-registry automated BioContainers addition for smoothxg"
config: {"url": "https://biocontainers.pro/tools/smoothxg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smoothxg", "latest": {"0.6.7--hfb1f815_1": "sha256:0d752f242a36a696064edd84137b62fa7416645c324be5c1f30f4d69b8754189"}, "tags": {"0.6.5--hfb1f815_2": "sha256:c4c82cbbf83b65d767c3f6af2b8a6fb5894ddb828d75d1a7f94da3224b2299ea", "0.6.7--hfb1f815_1": "sha256:0d752f242a36a696064edd84137b62fa7416645c324be5c1f30f4d69b8754189"}, "docker": "quay.io/biocontainers/smoothxg", "aliases": {"smoothxg": "/usr/local/bin/smoothxg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smoothxg.
shpc-registry automated BioContainers addition for smoothxg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smoothxg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smoothxg:0.6.7--hfb1f815_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smoothxg/0.6.7--hfb1f815_1
$ module help quay.io/biocontainers/smoothxg/0.6.7--hfb1f815_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smoothxg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smoothxg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smoothxg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smoothxg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smoothxg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smoothxg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smoothxg

```bash
$ singularity exec <container> /usr/local/bin/smoothxg
$ podman run --it --rm --entrypoint /usr/local/bin/smoothxg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smoothxg   -v ${PWD} -w ${PWD} <container> -c " $@"
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