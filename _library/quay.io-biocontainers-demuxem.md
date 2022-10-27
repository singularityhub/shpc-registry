---
layout: container
name:  "quay.io/biocontainers/demuxem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/demuxem/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/demuxem/container.yaml"
updated_at: "2022-10-27 00:24:25.868783"
latest: "0.1.7--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/demuxem"
aliases:
 - "demuxEM"
 - "pegasusio"
versions:
 - "0.1.7--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for demuxem"
config: {"url": "https://biocontainers.pro/tools/demuxem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for demuxem", "latest": {"0.1.7--pyhdfd78af_1": "sha256:a122f404ae5694e9232b18ae22014d9fd0011a28b1f350cea19986741184cbb5"}, "tags": {"0.1.7--pyhdfd78af_1": "sha256:a122f404ae5694e9232b18ae22014d9fd0011a28b1f350cea19986741184cbb5"}, "docker": "quay.io/biocontainers/demuxem", "aliases": {"demuxEM": "/usr/local/bin/demuxEM", "pegasusio": "/usr/local/bin/pegasusio"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/demuxem.
shpc-registry automated BioContainers addition for demuxem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/demuxem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/demuxem:0.1.7--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/demuxem/0.1.7--pyhdfd78af_1
$ module help quay.io/biocontainers/demuxem/0.1.7--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### demuxem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### demuxem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### demuxem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### demuxem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### demuxem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### demuxem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### demuxEM

```bash
$ singularity exec <container> /usr/local/bin/demuxEM
$ podman run --it --rm --entrypoint /usr/local/bin/demuxEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demuxEM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pegasusio

```bash
$ singularity exec <container> /usr/local/bin/pegasusio
$ podman run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
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