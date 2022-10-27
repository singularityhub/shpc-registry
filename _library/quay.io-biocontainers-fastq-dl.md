---
layout: container
name:  "quay.io/biocontainers/fastq-dl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-dl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-dl/container.yaml"
updated_at: "2022-10-27 00:59:59.548031"
latest: "1.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/fastq-dl"
aliases:
 - "executor"
 - "fastq-dl"
versions:
 - "1.1.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for fastq-dl"
config: {"url": "https://biocontainers.pro/tools/fastq-dl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-dl", "latest": {"1.1.1--hdfd78af_0": "sha256:6fdff94f1566200bf2b37f354aa3ceba5075e893f85e3eca2581197cdbd7d72b"}, "tags": {"1.1.1--hdfd78af_0": "sha256:6fdff94f1566200bf2b37f354aa3ceba5075e893f85e3eca2581197cdbd7d72b"}, "docker": "quay.io/biocontainers/fastq-dl", "aliases": {"executor": "/usr/local/bin/executor", "fastq-dl": "/usr/local/bin/fastq-dl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-dl.
shpc-registry automated BioContainers addition for fastq-dl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-dl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-dl:1.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-dl/1.1.1--hdfd78af_0
$ module help quay.io/biocontainers/fastq-dl/1.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-dl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-dl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-dl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-dl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-dl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-dl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-dl

```bash
$ singularity exec <container> /usr/local/bin/fastq-dl
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-dl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-dl   -v ${PWD} -w ${PWD} <container> -c " $@"
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