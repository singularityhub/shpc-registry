---
layout: container
name:  "quay.io/biocontainers/mmdb2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmdb2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmdb2/container.yaml"
updated_at: "2025-12-19 03:45:36.225834"
latest: "2.0.22--h5ca1c30_2"
container_url: "https://biocontainers.pro/tools/mmdb2"
aliases:
 - "x86_64-conda-linux-gnu-pkg-config"
 - "pkg-config"
 - "pkg-config.bin"
versions:
 - "2.0.22--h5ca1c30_1"
 - "2.0.22--h5ca1c30_2"
description: "singularity registry hpc automated addition for mmdb2"
config: {"url": "https://biocontainers.pro/tools/mmdb2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mmdb2", "latest": {"2.0.22--h5ca1c30_2": "sha256:cf2c61d4cf9f1ebde5becdb494cbcdff0256ec7d6fbef670ae3d57309c4279b8"}, "tags": {"2.0.22--h5ca1c30_1": "sha256:eb0a4cff44d27e98be22951cfb514c31c434956a6c99b5c79a3b29b1ca9c0479", "2.0.22--h5ca1c30_2": "sha256:cf2c61d4cf9f1ebde5becdb494cbcdff0256ec7d6fbef670ae3d57309c4279b8"}, "docker": "quay.io/biocontainers/mmdb2", "aliases": {"x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "pkg-config": "/usr/local/bin/pkg-config", "pkg-config.bin": "/usr/local/bin/pkg-config.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmdb2.
singularity registry hpc automated addition for mmdb2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmdb2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmdb2:2.0.22--h5ca1c30_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmdb2/2.0.22--h5ca1c30_2
$ module help quay.io/biocontainers/mmdb2/2.0.22--h5ca1c30_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmdb2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmdb2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmdb2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmdb2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmdb2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmdb2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config

```bash
$ singularity exec <container> /usr/local/bin/pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config.bin

```bash
$ singularity exec <container> /usr/local/bin/pkg-config.bin
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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