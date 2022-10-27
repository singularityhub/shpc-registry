---
layout: container
name:  "quay.io/biocontainers/unifrac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unifrac/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/unifrac/container.yaml"
updated_at: "2022-10-27 01:15:46.104571"
latest: "1.1.1--py310h79ef01b_1"
container_url: "https://biocontainers.pro/tools/unifrac"
aliases:
 - "bp"
 - "faithpd"
 - "ssu"
versions:
 - "1.1.1--py310h79ef01b_1"
description: "shpc-registry automated BioContainers addition for unifrac"
config: {"url": "https://biocontainers.pro/tools/unifrac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unifrac", "latest": {"1.1.1--py310h79ef01b_1": "sha256:c5df3127503ce3bad527b4d9316fe4b17edaca6fb7533330d7dcb3c730857b48"}, "tags": {"1.1.1--py310h79ef01b_1": "sha256:c5df3127503ce3bad527b4d9316fe4b17edaca6fb7533330d7dcb3c730857b48"}, "docker": "quay.io/biocontainers/unifrac", "aliases": {"bp": "/usr/local/bin/bp", "faithpd": "/usr/local/bin/faithpd", "ssu": "/usr/local/bin/ssu"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unifrac.
shpc-registry automated BioContainers addition for unifrac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unifrac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unifrac:1.1.1--py310h79ef01b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unifrac/1.1.1--py310h79ef01b_1
$ module help quay.io/biocontainers/unifrac/1.1.1--py310h79ef01b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unifrac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unifrac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unifrac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unifrac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unifrac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unifrac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp

```bash
$ singularity exec <container> /usr/local/bin/bp
$ podman run --it --rm --entrypoint /usr/local/bin/bp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faithpd

```bash
$ singularity exec <container> /usr/local/bin/faithpd
$ podman run --it --rm --entrypoint /usr/local/bin/faithpd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faithpd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssu

```bash
$ singularity exec <container> /usr/local/bin/ssu
$ podman run --it --rm --entrypoint /usr/local/bin/ssu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssu   -v ${PWD} -w ${PWD} <container> -c " $@"
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