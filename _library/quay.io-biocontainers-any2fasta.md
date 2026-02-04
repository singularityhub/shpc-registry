---
layout: container
name:  "quay.io/biocontainers/any2fasta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/any2fasta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/any2fasta/container.yaml"
updated_at: "2026-02-04 04:39:18.865310"
latest: "0.8.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/any2fasta"
aliases:
 - "any2fasta"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "0.4.2--hdfd78af_3"
 - "0.8.1--hdfd78af_0"
 - "0.6.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for any2fasta"
config: {"url": "https://biocontainers.pro/tools/any2fasta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for any2fasta", "latest": {"0.8.1--hdfd78af_0": "sha256:e616df15d7233d1e97f450de33e9a64ab0f2b9a501570de749eb3aa3fc70bf06"}, "tags": {"0.4.2--hdfd78af_3": "sha256:50441698f1f483b4139562d3d5a47ad7e67f926737c265e3bf5b31211ffe1620", "0.8.1--hdfd78af_0": "sha256:e616df15d7233d1e97f450de33e9a64ab0f2b9a501570de749eb3aa3fc70bf06", "0.6.2--hdfd78af_0": "sha256:81945d3a7241901bfb1e763bb42aa3eb9b7bd5bc98738b56f18ac2fb5605db95"}, "docker": "quay.io/biocontainers/any2fasta", "aliases": {"any2fasta": "/usr/local/bin/any2fasta", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/any2fasta.
shpc-registry automated BioContainers addition for any2fasta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/any2fasta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/any2fasta:0.8.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/any2fasta/0.8.1--hdfd78af_0
$ module help quay.io/biocontainers/any2fasta/0.8.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### any2fasta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### any2fasta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### any2fasta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### any2fasta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### any2fasta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### any2fasta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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