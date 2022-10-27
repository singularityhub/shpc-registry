---
layout: container
name:  "quay.io/biocontainers/fastq-anonymous"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-anonymous/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-anonymous/container.yaml"
updated_at: "2022-10-27 01:08:09.006444"
latest: "1.0.1--py_2"
container_url: "https://biocontainers.pro/tools/fastq-anonymous"
aliases:
 - "fastq-anonymous"
versions:
 - "1.0.1--py_2"
description: "shpc-registry automated BioContainers addition for fastq-anonymous"
config: {"url": "https://biocontainers.pro/tools/fastq-anonymous", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-anonymous", "latest": {"1.0.1--py_2": "sha256:c4d76ab8eb1e2cee558d8c5407d5ad7bbe264bf990bec8b4d84f0c78b4ce34fb"}, "tags": {"1.0.1--py_2": "sha256:c4d76ab8eb1e2cee558d8c5407d5ad7bbe264bf990bec8b4d84f0c78b4ce34fb"}, "docker": "quay.io/biocontainers/fastq-anonymous", "aliases": {"fastq-anonymous": "/usr/local/bin/fastq-anonymous"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-anonymous.
shpc-registry automated BioContainers addition for fastq-anonymous
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-anonymous
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-anonymous:1.0.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-anonymous/1.0.1--py_2
$ module help quay.io/biocontainers/fastq-anonymous/1.0.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-anonymous-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-anonymous-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-anonymous-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-anonymous-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-anonymous-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-anonymous-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-anonymous

```bash
$ singularity exec <container> /usr/local/bin/fastq-anonymous
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-anonymous   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-anonymous   -v ${PWD} -w ${PWD} <container> -c " $@"
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