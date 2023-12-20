---
layout: container
name:  "quay.io/biocontainers/fqtrim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fqtrim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fqtrim/container.yaml"
updated_at: "2023-12-20 02:43:24.416682"
latest: "0.9.7--hdcf5f25_6"
container_url: "https://biocontainers.pro/tools/fqtrim"
aliases:
 - "fqtrim"
 - "gtest"
 - "threads"
versions:
 - "0.9.7--hd03093a_4"
 - "0.9.7--hdcf5f25_6"
description: "shpc-registry automated BioContainers addition for fqtrim"
config: {"url": "https://biocontainers.pro/tools/fqtrim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fqtrim", "latest": {"0.9.7--hdcf5f25_6": "sha256:31acbb0d0e2542b2e853b480a641a31f2b4f94f66bb08b6f0149f461c205cfa6"}, "tags": {"0.9.7--hd03093a_4": "sha256:f53b6dbd2e9c794473fa891f72ca03f7d50c3f1fb5ef556bd4eda1b6c6a53fa7", "0.9.7--hdcf5f25_6": "sha256:31acbb0d0e2542b2e853b480a641a31f2b4f94f66bb08b6f0149f461c205cfa6"}, "docker": "quay.io/biocontainers/fqtrim", "aliases": {"fqtrim": "/usr/local/bin/fqtrim", "gtest": "/usr/local/bin/gtest", "threads": "/usr/local/bin/threads"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fqtrim.
shpc-registry automated BioContainers addition for fqtrim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fqtrim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fqtrim:0.9.7--hdcf5f25_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fqtrim/0.9.7--hdcf5f25_6
$ module help quay.io/biocontainers/fqtrim/0.9.7--hdcf5f25_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fqtrim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fqtrim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fqtrim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fqtrim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fqtrim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fqtrim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqtrim

```bash
$ singularity exec <container> /usr/local/bin/fqtrim
$ podman run --it --rm --entrypoint /usr/local/bin/fqtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtest

```bash
$ singularity exec <container> /usr/local/bin/gtest
$ podman run --it --rm --entrypoint /usr/local/bin/gtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### threads

```bash
$ singularity exec <container> /usr/local/bin/threads
$ podman run --it --rm --entrypoint /usr/local/bin/threads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/threads   -v ${PWD} -w ${PWD} <container> -c " $@"
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