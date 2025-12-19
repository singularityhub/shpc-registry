---
layout: container
name:  "quay.io/biocontainers/kmer-counter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmer-counter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmer-counter/container.yaml"
updated_at: "2025-12-19 03:59:26.705470"
latest: "0.1.2--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/kmer-counter"
aliases:
 - "kmer-counter"
versions:
 - "0.1.2--h4349ce8_0"
description: "singularity registry hpc automated addition for kmer-counter"
config: {"url": "https://biocontainers.pro/tools/kmer-counter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmer-counter", "latest": {"0.1.2--h4349ce8_0": "sha256:b2927b1a68b82182113c60dc64a830b682953c33b56de5a191ad0f285f40aec9"}, "tags": {"0.1.2--h4349ce8_0": "sha256:b2927b1a68b82182113c60dc64a830b682953c33b56de5a191ad0f285f40aec9"}, "docker": "quay.io/biocontainers/kmer-counter", "aliases": {"kmer-counter": "/usr/local/bin/kmer-counter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmer-counter.
singularity registry hpc automated addition for kmer-counter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmer-counter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmer-counter:0.1.2--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmer-counter/0.1.2--h4349ce8_0
$ module help quay.io/biocontainers/kmer-counter/0.1.2--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmer-counter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmer-counter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmer-counter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmer-counter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmer-counter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmer-counter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmer-counter

```bash
$ singularity exec <container> /usr/local/bin/kmer-counter
$ podman run --it --rm --entrypoint /usr/local/bin/kmer-counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer-counter   -v ${PWD} -w ${PWD} <container> -c " $@"
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