---
layout: container
name:  "quay.io/biocontainers/stoatydive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stoatydive/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stoatydive/container.yaml"
updated_at: "2022-10-27 00:46:11.892510"
latest: "1.1.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/stoatydive"
aliases:
 - "StoatyDive.py"
versions:
 - "1.1.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for stoatydive"
config: {"url": "https://biocontainers.pro/tools/stoatydive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stoatydive", "latest": {"1.1.1--pyh5e36f6f_0": "sha256:2e6a174b1d40c76d91b16beb617b5d854711d1b9b7dc88f2ec9f47dfaa8298e6"}, "tags": {"1.1.1--pyh5e36f6f_0": "sha256:2e6a174b1d40c76d91b16beb617b5d854711d1b9b7dc88f2ec9f47dfaa8298e6"}, "docker": "quay.io/biocontainers/stoatydive", "aliases": {"StoatyDive.py": "/usr/local/bin/StoatyDive.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stoatydive.
shpc-registry automated BioContainers addition for stoatydive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stoatydive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stoatydive:1.1.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stoatydive/1.1.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/stoatydive/1.1.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stoatydive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stoatydive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stoatydive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stoatydive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stoatydive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stoatydive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### StoatyDive.py

```bash
$ singularity exec <container> /usr/local/bin/StoatyDive.py
$ podman run --it --rm --entrypoint /usr/local/bin/StoatyDive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StoatyDive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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