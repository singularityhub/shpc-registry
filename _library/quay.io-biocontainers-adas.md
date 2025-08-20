---
layout: container
name:  "quay.io/biocontainers/adas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/adas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/adas/container.yaml"
updated_at: "2025-08-20 03:23:04.316285"
latest: "0.1.3--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/adas"
aliases:
 - "adas-build"
 - "adas-chain"
 - "adas-insert"
 - "adas-knn"
 - "adas-search"
 - "usearch"
versions:
 - "0.1.3--h3ab6199_0"
description: "singularity registry hpc automated addition for adas"
config: {"url": "https://biocontainers.pro/tools/adas", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for adas", "latest": {"0.1.3--h3ab6199_0": "sha256:d64f28f6bcb567cef430e78bf80e741d7fbfd723fb533f17db6283e3a5294792"}, "tags": {"0.1.3--h3ab6199_0": "sha256:d64f28f6bcb567cef430e78bf80e741d7fbfd723fb533f17db6283e3a5294792"}, "docker": "quay.io/biocontainers/adas", "aliases": {"adas-build": "/usr/local/bin/adas-build", "adas-chain": "/usr/local/bin/adas-chain", "adas-insert": "/usr/local/bin/adas-insert", "adas-knn": "/usr/local/bin/adas-knn", "adas-search": "/usr/local/bin/adas-search", "usearch": "/usr/local/bin/usearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/adas.
singularity registry hpc automated addition for adas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/adas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/adas:0.1.3--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/adas/0.1.3--h3ab6199_0
$ module help quay.io/biocontainers/adas/0.1.3--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adas-build

```bash
$ singularity exec <container> /usr/local/bin/adas-build
$ podman run --it --rm --entrypoint /usr/local/bin/adas-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adas-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adas-chain

```bash
$ singularity exec <container> /usr/local/bin/adas-chain
$ podman run --it --rm --entrypoint /usr/local/bin/adas-chain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adas-chain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adas-insert

```bash
$ singularity exec <container> /usr/local/bin/adas-insert
$ podman run --it --rm --entrypoint /usr/local/bin/adas-insert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adas-insert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adas-knn

```bash
$ singularity exec <container> /usr/local/bin/adas-knn
$ podman run --it --rm --entrypoint /usr/local/bin/adas-knn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adas-knn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adas-search

```bash
$ singularity exec <container> /usr/local/bin/adas-search
$ podman run --it --rm --entrypoint /usr/local/bin/adas-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adas-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### usearch

```bash
$ singularity exec <container> /usr/local/bin/usearch
$ podman run --it --rm --entrypoint /usr/local/bin/usearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/usearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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