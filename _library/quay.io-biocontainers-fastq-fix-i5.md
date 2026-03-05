---
layout: container
name:  "quay.io/biocontainers/fastq-fix-i5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-fix-i5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-fix-i5/container.yaml"
updated_at: "2026-03-05 00:30:48.978510"
latest: "1.0.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/fastq-fix-i5"
aliases:
 - "fastq-fix-i5"
versions:
 - "1.0.0--h4349ce8_0"
description: "singularity registry hpc automated addition for fastq-fix-i5"
config: {"url": "https://biocontainers.pro/tools/fastq-fix-i5", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastq-fix-i5", "latest": {"1.0.0--h4349ce8_0": "sha256:10ff0eb48ce3fa5ce3cc0111bad23a29713fdfd1aeace51141b7fd0b22daf9fe"}, "tags": {"1.0.0--h4349ce8_0": "sha256:10ff0eb48ce3fa5ce3cc0111bad23a29713fdfd1aeace51141b7fd0b22daf9fe"}, "docker": "quay.io/biocontainers/fastq-fix-i5", "aliases": {"fastq-fix-i5": "/usr/local/bin/fastq-fix-i5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-fix-i5.
singularity registry hpc automated addition for fastq-fix-i5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-fix-i5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-fix-i5:1.0.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-fix-i5/1.0.0--h4349ce8_0
$ module help quay.io/biocontainers/fastq-fix-i5/1.0.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-fix-i5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-fix-i5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-fix-i5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-fix-i5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-fix-i5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-fix-i5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-fix-i5

```bash
$ singularity exec <container> /usr/local/bin/fastq-fix-i5
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-fix-i5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-fix-i5   -v ${PWD} -w ${PWD} <container> -c " $@"
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