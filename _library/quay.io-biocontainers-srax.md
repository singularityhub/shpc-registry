---
layout: container
name:  "quay.io/biocontainers/srax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/srax/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/srax/container.yaml"
updated_at: "2022-10-27 01:08:05.553457"
latest: "1.5--pl5321ha8f3691_2"
container_url: "https://biocontainers.pro/tools/srax"
aliases:
 - "envpath"
 - "sraX"
versions:
 - "1.5--pl5321ha8f3691_2"
description: "shpc-registry automated BioContainers addition for srax"
config: {"url": "https://biocontainers.pro/tools/srax", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for srax", "latest": {"1.5--pl5321ha8f3691_2": "sha256:6f521a8ef2406b1bf0e8bbda74fe02236859f3a3454692a808ac40366914b816"}, "tags": {"1.5--pl5321ha8f3691_2": "sha256:6f521a8ef2406b1bf0e8bbda74fe02236859f3a3454692a808ac40366914b816"}, "docker": "quay.io/biocontainers/srax", "aliases": {"envpath": "/usr/local/bin/envpath", "sraX": "/usr/local/bin/sraX"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/srax.
shpc-registry automated BioContainers addition for srax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/srax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/srax:1.5--pl5321ha8f3691_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/srax/1.5--pl5321ha8f3691_2
$ module help quay.io/biocontainers/srax/1.5--pl5321ha8f3691_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### srax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### srax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### srax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### srax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### srax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### srax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### envpath

```bash
$ singularity exec <container> /usr/local/bin/envpath
$ podman run --it --rm --entrypoint /usr/local/bin/envpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/envpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sraX

```bash
$ singularity exec <container> /usr/local/bin/sraX
$ podman run --it --rm --entrypoint /usr/local/bin/sraX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sraX   -v ${PWD} -w ${PWD} <container> -c " $@"
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