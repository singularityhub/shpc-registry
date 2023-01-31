---
layout: container
name:  "quay.io/biocontainers/spoa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spoa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spoa/container.yaml"
updated_at: "2023-01-31 03:03:41.827022"
latest: "4.0.7--hd03093a_3"
container_url: "https://biocontainers.pro/tools/spoa"
aliases:
 - "spoa"
versions:
 - "4.0.7--hd03093a_3"
description: "shpc-registry automated BioContainers addition for spoa"
config: {"url": "https://biocontainers.pro/tools/spoa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spoa", "latest": {"4.0.7--hd03093a_3": "sha256:5a2fd9bee52f97f543cc2036767268e67d73ce21be6bfdc1863ea0f04bc0341c"}, "tags": {"4.0.7--hd03093a_3": "sha256:5a2fd9bee52f97f543cc2036767268e67d73ce21be6bfdc1863ea0f04bc0341c"}, "docker": "quay.io/biocontainers/spoa", "aliases": {"spoa": "/usr/local/bin/spoa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spoa.
shpc-registry automated BioContainers addition for spoa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spoa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spoa:4.0.7--hd03093a_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spoa/4.0.7--hd03093a_3
$ module help quay.io/biocontainers/spoa/4.0.7--hd03093a_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spoa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spoa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spoa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spoa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spoa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spoa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spoa

```bash
$ singularity exec <container> /usr/local/bin/spoa
$ podman run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
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