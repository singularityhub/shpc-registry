---
layout: container
name:  "quay.io/biocontainers/idba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/idba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/idba/container.yaml"
updated_at: "2022-10-27 01:03:44.760380"
latest: "1.1.3--1"
container_url: "https://biocontainers.pro/tools/idba"
aliases:
 - "autoheader.bak"
 - "autom4te.bak"
 - "autoreconf.bak"
 - "autoscan.bak"
 - "autoupdate.bak"
 - "ifnames.bak"
versions:
 - "1.1.3--1"
description: "shpc-registry automated BioContainers addition for idba"
config: {"url": "https://biocontainers.pro/tools/idba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for idba", "latest": {"1.1.3--1": "sha256:51291ffeeecc6afab8d56bf33dffd0c2cb5e24d8a545a5ea93bb795d6af12fa0"}, "tags": {"1.1.3--1": "sha256:51291ffeeecc6afab8d56bf33dffd0c2cb5e24d8a545a5ea93bb795d6af12fa0"}, "docker": "quay.io/biocontainers/idba", "aliases": {"autoheader.bak": "/usr/local/bin/autoheader.bak", "autom4te.bak": "/usr/local/bin/autom4te.bak", "autoreconf.bak": "/usr/local/bin/autoreconf.bak", "autoscan.bak": "/usr/local/bin/autoscan.bak", "autoupdate.bak": "/usr/local/bin/autoupdate.bak", "ifnames.bak": "/usr/local/bin/ifnames.bak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/idba.
shpc-registry automated BioContainers addition for idba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/idba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/idba:1.1.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/idba/1.1.3--1
$ module help quay.io/biocontainers/idba/1.1.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### idba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### idba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### idba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### idba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### idba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### idba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autoheader.bak

```bash
$ singularity exec <container> /usr/local/bin/autoheader.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autom4te.bak

```bash
$ singularity exec <container> /usr/local/bin/autom4te.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoreconf.bak

```bash
$ singularity exec <container> /usr/local/bin/autoreconf.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoscan.bak

```bash
$ singularity exec <container> /usr/local/bin/autoscan.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoupdate.bak

```bash
$ singularity exec <container> /usr/local/bin/autoupdate.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifnames.bak

```bash
$ singularity exec <container> /usr/local/bin/ifnames.bak
$ podman run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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