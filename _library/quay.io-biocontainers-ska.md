---
layout: container
name:  "quay.io/biocontainers/ska"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ska/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ska/container.yaml"
updated_at: "2025-01-11 03:30:48.982157"
latest: "1.0--h077b44d_6"
container_url: "https://biocontainers.pro/tools/ska"
aliases:
 - "ska"
versions:
 - "1.0--hd03093a_3"
 - "1.0--hdcf5f25_5"
 - "1.0--h077b44d_6"
description: "shpc-registry automated BioContainers addition for ska"
config: {"url": "https://biocontainers.pro/tools/ska", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ska", "latest": {"1.0--h077b44d_6": "sha256:bd2ca3392c030ef1589daa5bc925f4c90e20a78cdf455c2e3a8d6946b73b7b80"}, "tags": {"1.0--hd03093a_3": "sha256:0a7ab433c00bbd91a0ad97a4af61b7cd404e7da98e39bb7f4a3275120c251e01", "1.0--hdcf5f25_5": "sha256:5dc32788db1ff30c0545e6ff9671c879230bba8044b663370e65834c688a1efb", "1.0--h077b44d_6": "sha256:bd2ca3392c030ef1589daa5bc925f4c90e20a78cdf455c2e3a8d6946b73b7b80"}, "docker": "quay.io/biocontainers/ska", "aliases": {"ska": "/usr/local/bin/ska"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ska.
shpc-registry automated BioContainers addition for ska
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ska
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ska:1.0--h077b44d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ska/1.0--h077b44d_6
$ module help quay.io/biocontainers/ska/1.0--h077b44d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ska-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ska-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ska-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ska-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ska-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ska-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ska

```bash
$ singularity exec <container> /usr/local/bin/ska
$ podman run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
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