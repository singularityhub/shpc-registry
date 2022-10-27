---
layout: container
name:  "quay.io/biocontainers/pipelign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pipelign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pipelign/container.yaml"
updated_at: "2022-10-27 00:50:35.747926"
latest: "0.2--py_2"
container_url: "https://biocontainers.pro/tools/pipelign"
aliases:
 - "gb2fas"
 - "pipelign"
versions:
 - "0.2--py_2"
description: "shpc-registry automated BioContainers addition for pipelign"
config: {"url": "https://biocontainers.pro/tools/pipelign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pipelign", "latest": {"0.2--py_2": "sha256:2cd5d54114c6fcaad221e955d439da300aee7838bf7c0e5775f9e56a5c665d7a"}, "tags": {"0.2--py_2": "sha256:2cd5d54114c6fcaad221e955d439da300aee7838bf7c0e5775f9e56a5c665d7a"}, "docker": "quay.io/biocontainers/pipelign", "aliases": {"gb2fas": "/usr/local/bin/gb2fas", "pipelign": "/usr/local/bin/pipelign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pipelign.
shpc-registry automated BioContainers addition for pipelign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pipelign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pipelign:0.2--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pipelign/0.2--py_2
$ module help quay.io/biocontainers/pipelign/0.2--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pipelign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pipelign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pipelign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pipelign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pipelign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pipelign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gb2fas

```bash
$ singularity exec <container> /usr/local/bin/gb2fas
$ podman run --it --rm --entrypoint /usr/local/bin/gb2fas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gb2fas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pipelign

```bash
$ singularity exec <container> /usr/local/bin/pipelign
$ podman run --it --rm --entrypoint /usr/local/bin/pipelign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pipelign   -v ${PWD} -w ${PWD} <container> -c " $@"
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