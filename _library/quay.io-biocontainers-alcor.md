---
layout: container
name:  "quay.io/biocontainers/alcor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alcor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alcor/container.yaml"
updated_at: "2023-05-26 03:18:29.998266"
latest: "1.9--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/alcor"
aliases:
 - "AlcoR"
versions:
 - "1.9--hd03093a_0"
 - "1.9--hdcf5f25_2"
description: "singularity registry hpc automated addition for alcor"
config: {"url": "https://biocontainers.pro/tools/alcor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for alcor", "latest": {"1.9--hdcf5f25_2": "sha256:1d1712e4957d5adedd972fbbfbae6df0917dfd134a5e164f1cf498c8f667cb42"}, "tags": {"1.9--hd03093a_0": "sha256:9020e36402d77479be5c2b04bed89420d63777c9f9c7adff0ee0f4d5269efe9a", "1.9--hdcf5f25_2": "sha256:1d1712e4957d5adedd972fbbfbae6df0917dfd134a5e164f1cf498c8f667cb42"}, "docker": "quay.io/biocontainers/alcor", "aliases": {"AlcoR": "/usr/local/bin/AlcoR"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alcor.
singularity registry hpc automated addition for alcor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alcor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alcor:1.9--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alcor/1.9--hdcf5f25_2
$ module help quay.io/biocontainers/alcor/1.9--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alcor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alcor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alcor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alcor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alcor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alcor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AlcoR

```bash
$ singularity exec <container> /usr/local/bin/AlcoR
$ podman run --it --rm --entrypoint /usr/local/bin/AlcoR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlcoR   -v ${PWD} -w ${PWD} <container> -c " $@"
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