---
layout: container
name:  "quay.io/biocontainers/manc_cojo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/manc_cojo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/manc_cojo/container.yaml"
updated_at: "2026-06-24 06:57:20.233181"
latest: "1.1.0--hd63eeec_0"
container_url: "https://biocontainers.pro/tools/manc_cojo"
aliases:
 - "manc_cojo"
versions:
 - "1.1.0--hd63eeec_0"
description: "singularity registry hpc automated addition for manc_cojo"
config: {"url": "https://biocontainers.pro/tools/manc_cojo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for manc_cojo", "latest": {"1.1.0--hd63eeec_0": "sha256:49c67b6e8bd7e906ce6d0f2b2ef0290375b6688d5cdc78f6c143bbdccff2906d"}, "tags": {"1.1.0--hd63eeec_0": "sha256:49c67b6e8bd7e906ce6d0f2b2ef0290375b6688d5cdc78f6c143bbdccff2906d"}, "docker": "quay.io/biocontainers/manc_cojo", "aliases": {"manc_cojo": "/usr/local/bin/manc_cojo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/manc_cojo.
singularity registry hpc automated addition for manc_cojo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/manc_cojo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/manc_cojo:1.1.0--hd63eeec_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/manc_cojo/1.1.0--hd63eeec_0
$ module help quay.io/biocontainers/manc_cojo/1.1.0--hd63eeec_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### manc_cojo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### manc_cojo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### manc_cojo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### manc_cojo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### manc_cojo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### manc_cojo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### manc_cojo

```bash
$ singularity exec <container> /usr/local/bin/manc_cojo
$ podman run --it --rm --entrypoint /usr/local/bin/manc_cojo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/manc_cojo   -v ${PWD} -w ${PWD} <container> -c " $@"
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