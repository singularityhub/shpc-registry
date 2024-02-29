---
layout: container
name:  "quay.io/biocontainers/fpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fpa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fpa/container.yaml"
updated_at: "2024-02-29 02:51:17.306393"
latest: "0.5--hbcae180_2"
container_url: "https://biocontainers.pro/tools/fpa"
aliases:
 - "fpa"
versions:
 - "0.5--hbcae180_2"
description: "shpc-registry automated BioContainers addition for fpa"
config: {"url": "https://biocontainers.pro/tools/fpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fpa", "latest": {"0.5--hbcae180_2": "sha256:b216fc65991a5553c9b9ad100ef66d9fa0f75ec038bad01f5f3010b318aedc43"}, "tags": {"0.5--hbcae180_2": "sha256:b216fc65991a5553c9b9ad100ef66d9fa0f75ec038bad01f5f3010b318aedc43"}, "docker": "quay.io/biocontainers/fpa", "aliases": {"fpa": "/usr/local/bin/fpa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fpa.
shpc-registry automated BioContainers addition for fpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fpa:0.5--hbcae180_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fpa/0.5--hbcae180_2
$ module help quay.io/biocontainers/fpa/0.5--hbcae180_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fpa

```bash
$ singularity exec <container> /usr/local/bin/fpa
$ podman run --it --rm --entrypoint /usr/local/bin/fpa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpa   -v ${PWD} -w ${PWD} <container> -c " $@"
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