---
layout: container
name:  "quay.io/biocontainers/cap3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cap3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cap3/container.yaml"
updated_at: "2025-03-08 02:37:34.395802"
latest: "10.2011--h779adbc_3"
container_url: "https://biocontainers.pro/tools/cap3"
aliases:
 - "cap3"
 - "formcon"
versions:
 - "10.2011--h779adbc_3"
description: "shpc-registry automated BioContainers addition for cap3"
config: {"url": "https://biocontainers.pro/tools/cap3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cap3", "latest": {"10.2011--h779adbc_3": "sha256:f86b860ece986c5691fdce2ed35bb4046527f9eb2af7236b1053e070d0b7a750"}, "tags": {"10.2011--h779adbc_3": "sha256:f86b860ece986c5691fdce2ed35bb4046527f9eb2af7236b1053e070d0b7a750"}, "docker": "quay.io/biocontainers/cap3", "aliases": {"cap3": "/usr/local/bin/cap3", "formcon": "/usr/local/bin/formcon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cap3.
shpc-registry automated BioContainers addition for cap3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cap3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cap3:10.2011--h779adbc_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cap3/10.2011--h779adbc_3
$ module help quay.io/biocontainers/cap3/10.2011--h779adbc_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cap3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cap3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cap3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cap3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cap3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cap3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cap3

```bash
$ singularity exec <container> /usr/local/bin/cap3
$ podman run --it --rm --entrypoint /usr/local/bin/cap3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cap3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formcon

```bash
$ singularity exec <container> /usr/local/bin/formcon
$ podman run --it --rm --entrypoint /usr/local/bin/formcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formcon   -v ${PWD} -w ${PWD} <container> -c " $@"
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