---
layout: container
name:  "quay.io/biocontainers/pbsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbsv/container.yaml"
updated_at: "2024-03-02 02:52:32.657980"
latest: "2.9.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pbsv"
aliases:
 - "pbsv"
versions:
 - "2.8.0--h9ee0642_0"
 - "2.9.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for pbsv"
config: {"url": "https://biocontainers.pro/tools/pbsv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbsv", "latest": {"2.9.0--h9ee0642_0": "sha256:254daba162bc2773ea0d8427fadcc74ab517f8f59427da0b955aa2cf8f53c07b"}, "tags": {"2.8.0--h9ee0642_0": "sha256:627c8685f240bbf0d5cc7bf1b0180457c23588d25efcffc72461b8c23fb830e5", "2.9.0--h9ee0642_0": "sha256:254daba162bc2773ea0d8427fadcc74ab517f8f59427da0b955aa2cf8f53c07b"}, "docker": "quay.io/biocontainers/pbsv", "aliases": {"pbsv": "/usr/local/bin/pbsv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbsv.
shpc-registry automated BioContainers addition for pbsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbsv:2.9.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbsv/2.9.0--h9ee0642_0
$ module help quay.io/biocontainers/pbsv/2.9.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbsv

```bash
$ singularity exec <container> /usr/local/bin/pbsv
$ podman run --it --rm --entrypoint /usr/local/bin/pbsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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