---
layout: container
name:  "quay.io/biocontainers/mars"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mars/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mars/container.yaml"
updated_at: "2022-10-27 00:43:12.368044"
latest: "1.2.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mars"
aliases:
 - "MARS_step1"
 - "MARS_step2"
versions:
 - "1.2.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mars"
config: {"url": "https://biocontainers.pro/tools/mars", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mars", "latest": {"1.2.4--pyhdfd78af_0": "sha256:e42b55e9d6f677e881fe31bafd4dba176b5fe9c178192121b93265662f991d46"}, "tags": {"1.2.4--pyhdfd78af_0": "sha256:e42b55e9d6f677e881fe31bafd4dba176b5fe9c178192121b93265662f991d46"}, "docker": "quay.io/biocontainers/mars", "aliases": {"MARS_step1": "/usr/local/bin/MARS_step1", "MARS_step2": "/usr/local/bin/MARS_step2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mars.
shpc-registry automated BioContainers addition for mars
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mars
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mars:1.2.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mars/1.2.4--pyhdfd78af_0
$ module help quay.io/biocontainers/mars/1.2.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mars-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mars-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mars-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mars-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mars-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mars-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MARS_step1

```bash
$ singularity exec <container> /usr/local/bin/MARS_step1
$ podman run --it --rm --entrypoint /usr/local/bin/MARS_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MARS_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MARS_step2

```bash
$ singularity exec <container> /usr/local/bin/MARS_step2
$ podman run --it --rm --entrypoint /usr/local/bin/MARS_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MARS_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
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