---
layout: container
name:  "quay.io/biocontainers/dnp-corrprofile"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnp-corrprofile/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnp-corrprofile/container.yaml"
updated_at: "2023-07-16 04:02:45.939273"
latest: "1.0--h6a68c12_5"
container_url: "https://biocontainers.pro/tools/dnp-corrprofile"
aliases:
 - "dnp-corrprofile"
versions:
 - "1.0--hf1761c0_3"
 - "1.0--h6a68c12_5"
description: "shpc-registry automated BioContainers addition for dnp-corrprofile"
config: {"url": "https://biocontainers.pro/tools/dnp-corrprofile", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnp-corrprofile", "latest": {"1.0--h6a68c12_5": "sha256:255292c3da7dfe9ebb710a2adf84452950e31135d1f03b8e65dcc7f068dfd3c1"}, "tags": {"1.0--hf1761c0_3": "sha256:01696c8f88bcfd50f0b5fa3f83b15edd58799af1c07b9654090394b5a46e4257", "1.0--h6a68c12_5": "sha256:255292c3da7dfe9ebb710a2adf84452950e31135d1f03b8e65dcc7f068dfd3c1"}, "docker": "quay.io/biocontainers/dnp-corrprofile", "aliases": {"dnp-corrprofile": "/usr/local/bin/dnp-corrprofile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnp-corrprofile.
shpc-registry automated BioContainers addition for dnp-corrprofile
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnp-corrprofile
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnp-corrprofile:1.0--h6a68c12_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnp-corrprofile/1.0--h6a68c12_5
$ module help quay.io/biocontainers/dnp-corrprofile/1.0--h6a68c12_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnp-corrprofile-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnp-corrprofile-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnp-corrprofile-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnp-corrprofile-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnp-corrprofile-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnp-corrprofile-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnp-corrprofile

```bash
$ singularity exec <container> /usr/local/bin/dnp-corrprofile
$ podman run --it --rm --entrypoint /usr/local/bin/dnp-corrprofile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnp-corrprofile   -v ${PWD} -w ${PWD} <container> -c " $@"
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