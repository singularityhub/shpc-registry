---
layout: container
name:  "quay.io/biocontainers/emboss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/emboss/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/emboss/container.yaml"
updated_at: "2022-10-29 05:56:45.103207"
latest: "6.6.0--haa49230_5"
container_url: "https://biocontainers.pro/tools/emboss"
aliases:
 - "2to3-3.7"
 - "_aaindexextract"
 - "_abiview"
 - "_acdc"
 - "_acdpretty"
 - "_acdtable"
 - "_acdtrace"
 - "_acdvalid"
 - "_antigenic"
 - "_backtranambig"
versions:
 - "6.6.0--haa49230_5"
description: "shpc-registry automated BioContainers addition for emboss"
config: {"url": "https://biocontainers.pro/tools/emboss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for emboss", "latest": {"6.6.0--haa49230_5": "sha256:51a26af4f2349bcb017855d7e797bcdb787e9177b3067ff439ccdeac550991ab"}, "tags": {"6.6.0--haa49230_5": "sha256:51a26af4f2349bcb017855d7e797bcdb787e9177b3067ff439ccdeac550991ab"}, "docker": "quay.io/biocontainers/emboss", "aliases": {"2to3-3.7": "/usr/local/bin/2to3-3.7", "_aaindexextract": "/usr/local/bin/_aaindexextract", "_abiview": "/usr/local/bin/_abiview", "_acdc": "/usr/local/bin/_acdc", "_acdpretty": "/usr/local/bin/_acdpretty", "_acdtable": "/usr/local/bin/_acdtable", "_acdtrace": "/usr/local/bin/_acdtrace", "_acdvalid": "/usr/local/bin/_acdvalid", "_antigenic": "/usr/local/bin/_antigenic", "_backtranambig": "/usr/local/bin/_backtranambig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/emboss.
shpc-registry automated BioContainers addition for emboss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/emboss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/emboss:6.6.0--haa49230_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/emboss/6.6.0--haa49230_5
$ module help quay.io/biocontainers/emboss/6.6.0--haa49230_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### emboss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### emboss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### emboss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### emboss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### emboss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### emboss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/_aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _abiview

```bash
$ singularity exec <container> /usr/local/bin/_abiview
$ podman run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdc

```bash
$ singularity exec <container> /usr/local/bin/_acdc
$ podman run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdpretty

```bash
$ singularity exec <container> /usr/local/bin/_acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtable

```bash
$ singularity exec <container> /usr/local/bin/_acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtrace

```bash
$ singularity exec <container> /usr/local/bin/_acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdvalid

```bash
$ singularity exec <container> /usr/local/bin/_acdvalid
$ podman run --it --rm --entrypoint /usr/local/bin/_acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _antigenic

```bash
$ singularity exec <container> /usr/local/bin/_antigenic
$ podman run --it --rm --entrypoint /usr/local/bin/_antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _backtranambig

```bash
$ singularity exec <container> /usr/local/bin/_backtranambig
$ podman run --it --rm --entrypoint /usr/local/bin/_backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
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