---
layout: container
name:  "quay.io/biocontainers/plasmidtron"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plasmidtron/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/plasmidtron/container.yaml"
updated_at: "2022-10-27 00:56:08.962276"
latest: "0.4.1--py_2"
container_url: "https://biocontainers.pro/tools/plasmidtron"
aliases:
 - "plasmidtron"
 - "plotkmers"
versions:
 - "0.4.1--py_2"
description: "shpc-registry automated BioContainers addition for plasmidtron"
config: {"url": "https://biocontainers.pro/tools/plasmidtron", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plasmidtron", "latest": {"0.4.1--py_2": "sha256:b5754dd6600d8d908ca70a64c400b63747026c23dac69f40db567d2a94fae548"}, "tags": {"0.4.1--py_2": "sha256:b5754dd6600d8d908ca70a64c400b63747026c23dac69f40db567d2a94fae548"}, "docker": "quay.io/biocontainers/plasmidtron", "aliases": {"plasmidtron": "/usr/local/bin/plasmidtron", "plotkmers": "/usr/local/bin/plotkmers"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plasmidtron.
shpc-registry automated BioContainers addition for plasmidtron
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plasmidtron
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plasmidtron:0.4.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plasmidtron/0.4.1--py_2
$ module help quay.io/biocontainers/plasmidtron/0.4.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasmidtron-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasmidtron-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasmidtron-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasmidtron-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasmidtron-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasmidtron-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plasmidtron

```bash
$ singularity exec <container> /usr/local/bin/plasmidtron
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidtron   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidtron   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotkmers

```bash
$ singularity exec <container> /usr/local/bin/plotkmers
$ podman run --it --rm --entrypoint /usr/local/bin/plotkmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotkmers   -v ${PWD} -w ${PWD} <container> -c " $@"
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