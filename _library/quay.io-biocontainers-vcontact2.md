---
layout: container
name:  "quay.io/biocontainers/vcontact2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcontact2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vcontact2/container.yaml"
updated_at: "2022-10-27 00:54:13.333438"
latest: "0.9.19--py_0"
container_url: "https://biocontainers.pro/tools/vcontact2"
aliases:
 - "vcontact2"
 - "vcontact2_gene2genome"
versions:
 - "0.9.19--py_0"
description: "shpc-registry automated BioContainers addition for vcontact2"
config: {"url": "https://biocontainers.pro/tools/vcontact2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcontact2", "latest": {"0.9.19--py_0": "sha256:b7fc2478c774c86f23d20abe29695eda84c030fbbce367cc7b566f379659db67"}, "tags": {"0.9.19--py_0": "sha256:b7fc2478c774c86f23d20abe29695eda84c030fbbce367cc7b566f379659db67"}, "docker": "quay.io/biocontainers/vcontact2", "aliases": {"vcontact2": "/usr/local/bin/vcontact2", "vcontact2_gene2genome": "/usr/local/bin/vcontact2_gene2genome"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcontact2.
shpc-registry automated BioContainers addition for vcontact2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcontact2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcontact2:0.9.19--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcontact2/0.9.19--py_0
$ module help quay.io/biocontainers/vcontact2/0.9.19--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcontact2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcontact2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcontact2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcontact2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcontact2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcontact2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcontact2

```bash
$ singularity exec <container> /usr/local/bin/vcontact2
$ podman run --it --rm --entrypoint /usr/local/bin/vcontact2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcontact2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcontact2_gene2genome

```bash
$ singularity exec <container> /usr/local/bin/vcontact2_gene2genome
$ podman run --it --rm --entrypoint /usr/local/bin/vcontact2_gene2genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcontact2_gene2genome   -v ${PWD} -w ${PWD} <container> -c " $@"
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