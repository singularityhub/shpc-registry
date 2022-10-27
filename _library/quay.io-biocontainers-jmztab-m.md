---
layout: container
name:  "quay.io/biocontainers/jmztab-m"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jmztab-m/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jmztab-m/container.yaml"
updated_at: "2022-10-27 00:37:58.965451"
latest: "1.0.6--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/jmztab-m"
aliases:
 - "jmztab-m"
versions:
 - "1.0.6--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for jmztab-m"
config: {"url": "https://biocontainers.pro/tools/jmztab-m", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jmztab-m", "latest": {"1.0.6--hdfd78af_1": "sha256:038c0b53de2a3fe2691e269f04483075288dd493caa0931fe0dcc0a09abe0b4c"}, "tags": {"1.0.6--hdfd78af_1": "sha256:038c0b53de2a3fe2691e269f04483075288dd493caa0931fe0dcc0a09abe0b4c"}, "docker": "quay.io/biocontainers/jmztab-m", "aliases": {"jmztab-m": "/usr/local/bin/jmztab-m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jmztab-m.
shpc-registry automated BioContainers addition for jmztab-m
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jmztab-m
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jmztab-m:1.0.6--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jmztab-m/1.0.6--hdfd78af_1
$ module help quay.io/biocontainers/jmztab-m/1.0.6--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jmztab-m-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jmztab-m-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jmztab-m-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jmztab-m-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jmztab-m-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jmztab-m-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jmztab-m

```bash
$ singularity exec <container> /usr/local/bin/jmztab-m
$ podman run --it --rm --entrypoint /usr/local/bin/jmztab-m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmztab-m   -v ${PWD} -w ${PWD} <container> -c " $@"
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