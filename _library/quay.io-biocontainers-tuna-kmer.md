---
layout: container
name:  "quay.io/biocontainers/tuna-kmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tuna-kmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tuna-kmer/container.yaml"
updated_at: "2026-11-06 09:15:56.328032"
latest: "1.4.0--h3be2455_0"
container_url: "https://biocontainers.pro/tools/tuna-kmer"
aliases:
 - "tuna"
versions:
 - "1.4.0--h3be2455_0"
description: "singularity registry hpc automated addition for tuna-kmer"
config: {"url": "https://biocontainers.pro/tools/tuna-kmer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tuna-kmer", "latest": {"1.4.0--h3be2455_0": "sha256:64105b340715f84dd1500d9405b15da31d0f0134eab3c8af14f0434de076cb7e"}, "tags": {"1.4.0--h3be2455_0": "sha256:64105b340715f84dd1500d9405b15da31d0f0134eab3c8af14f0434de076cb7e"}, "docker": "quay.io/biocontainers/tuna-kmer", "aliases": {"tuna": "/usr/local/bin/tuna"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tuna-kmer.
singularity registry hpc automated addition for tuna-kmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tuna-kmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tuna-kmer:1.4.0--h3be2455_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tuna-kmer/1.4.0--h3be2455_0
$ module help quay.io/biocontainers/tuna-kmer/1.4.0--h3be2455_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tuna-kmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tuna-kmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tuna-kmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tuna-kmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tuna-kmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tuna-kmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tuna

```bash
$ singularity exec <container> /usr/local/bin/tuna
$ podman run --it --rm --entrypoint /usr/local/bin/tuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tuna   -v ${PWD} -w ${PWD} <container> -c " $@"
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