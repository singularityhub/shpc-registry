---
layout: container
name:  "quay.io/biocontainers/jcast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jcast/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jcast/container.yaml"
updated_at: "2022-10-27 00:42:28.896183"
latest: "0.3.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/jcast"
aliases:
 - "jcast"
versions:
 - "0.3.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for jcast"
config: {"url": "https://biocontainers.pro/tools/jcast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jcast", "latest": {"0.3.5--pyhdfd78af_0": "sha256:156feea982fbb615a4e8faf42f7a679e77db75fdfced049083ef718b20899514"}, "tags": {"0.3.5--pyhdfd78af_0": "sha256:156feea982fbb615a4e8faf42f7a679e77db75fdfced049083ef718b20899514"}, "docker": "quay.io/biocontainers/jcast", "aliases": {"jcast": "/usr/local/bin/jcast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jcast.
shpc-registry automated BioContainers addition for jcast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jcast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jcast:0.3.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jcast/0.3.5--pyhdfd78af_0
$ module help quay.io/biocontainers/jcast/0.3.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jcast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jcast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jcast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jcast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jcast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jcast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jcast

```bash
$ singularity exec <container> /usr/local/bin/jcast
$ podman run --it --rm --entrypoint /usr/local/bin/jcast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jcast   -v ${PWD} -w ${PWD} <container> -c " $@"
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