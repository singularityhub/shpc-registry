---
layout: container
name:  "quay.io/biocontainers/doit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/doit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/doit/container.yaml"
updated_at: "2022-10-27 00:26:52.798211"
latest: "0.29.0--py27_0"
container_url: "https://biocontainers.pro/tools/doit"
aliases:
 - "doit"
 - "smtpd.pyc"
versions:
 - "0.29.0--py27_0"
description: "shpc-registry automated BioContainers addition for doit"
config: {"url": "https://biocontainers.pro/tools/doit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for doit", "latest": {"0.29.0--py27_0": "sha256:059b2d00052bb6b732894de31449273a2a879141c82cbe4019d95ef899759ed9"}, "tags": {"0.29.0--py27_0": "sha256:059b2d00052bb6b732894de31449273a2a879141c82cbe4019d95ef899759ed9"}, "docker": "quay.io/biocontainers/doit", "aliases": {"doit": "/usr/local/bin/doit", "smtpd.pyc": "/usr/local/bin/smtpd.pyc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/doit.
shpc-registry automated BioContainers addition for doit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/doit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/doit:0.29.0--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/doit/0.29.0--py27_0
$ module help quay.io/biocontainers/doit/0.29.0--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### doit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### doit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### doit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### doit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### doit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### doit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### doit

```bash
$ singularity exec <container> /usr/local/bin/doit
$ podman run --it --rm --entrypoint /usr/local/bin/doit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.pyc

```bash
$ singularity exec <container> /usr/local/bin/smtpd.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
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