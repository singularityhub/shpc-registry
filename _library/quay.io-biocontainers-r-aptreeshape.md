---
layout: container
name:  "quay.io/biocontainers/r-aptreeshape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-aptreeshape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-aptreeshape/container.yaml"
updated_at: "2024-12-02 03:33:40.656601"
latest: "1.5_0--r351h6115d3f_3"
container_url: "https://biocontainers.pro/tools/r-aptreeshape"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.5_0--r351h6115d3f_3"
description: "shpc-registry automated BioContainers addition for r-aptreeshape"
config: {"url": "https://biocontainers.pro/tools/r-aptreeshape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-aptreeshape", "latest": {"1.5_0--r351h6115d3f_3": "sha256:a274e7dc7ef2cad27989cb02556120c77be97bab1b61a1faf957b6e3aaba006b"}, "tags": {"1.5_0--r351h6115d3f_3": "sha256:a274e7dc7ef2cad27989cb02556120c77be97bab1b61a1faf957b6e3aaba006b"}, "docker": "quay.io/biocontainers/r-aptreeshape", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-aptreeshape.
shpc-registry automated BioContainers addition for r-aptreeshape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-aptreeshape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-aptreeshape:1.5_0--r351h6115d3f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-aptreeshape/1.5_0--r351h6115d3f_3
$ module help quay.io/biocontainers/r-aptreeshape/1.5_0--r351h6115d3f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-aptreeshape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-aptreeshape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-aptreeshape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-aptreeshape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-aptreeshape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-aptreeshape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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