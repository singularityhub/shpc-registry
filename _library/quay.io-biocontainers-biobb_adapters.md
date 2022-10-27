---
layout: container
name:  "quay.io/biocontainers/biobb_adapters"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_adapters/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_adapters/container.yaml"
updated_at: "2022-10-27 00:20:15.139873"
latest: "3.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_adapters"
aliases:
 - "black-primer"
versions:
 - "3.7.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_adapters"
config: {"url": "https://biocontainers.pro/tools/biobb_adapters", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_adapters", "latest": {"3.7.0--pyhdfd78af_0": "sha256:4d8ee7daa23a452321524f2ad7c6f3cadc41bc490670a6d02bfdf03afb990c85"}, "tags": {"3.7.0--pyhdfd78af_0": "sha256:4d8ee7daa23a452321524f2ad7c6f3cadc41bc490670a6d02bfdf03afb990c85"}, "docker": "quay.io/biocontainers/biobb_adapters", "aliases": {"black-primer": "/usr/local/bin/black-primer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_adapters.
shpc-registry automated BioContainers addition for biobb_adapters
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_adapters
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_adapters:3.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_adapters/3.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_adapters/3.7.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_adapters-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_adapters-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_adapters-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_adapters-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_adapters-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_adapters-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
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