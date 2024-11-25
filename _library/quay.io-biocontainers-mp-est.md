---
layout: container
name:  "quay.io/biocontainers/mp-est"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mp-est/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mp-est/container.yaml"
updated_at: "2024-11-25 03:07:40.002846"
latest: "3.0.0--h031d066_1"
container_url: "https://biocontainers.pro/tools/mp-est"
aliases:
 - "mpest"
versions:
 - "3.0.0--hec16e2b_0"
 - "3.0.0--h031d066_1"
description: "singularity registry hpc automated addition for mp-est"
config: {"url": "https://biocontainers.pro/tools/mp-est", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mp-est", "latest": {"3.0.0--h031d066_1": "sha256:27d3c57bd36cee6b57bcf885c217d4560c2ee50d79b4571f7ed58424f432c59a"}, "tags": {"3.0.0--hec16e2b_0": "sha256:4ef7a6819f4fc28f2bbe10eda327f53f9249f1bc1747a773572854b05d8cc043", "3.0.0--h031d066_1": "sha256:27d3c57bd36cee6b57bcf885c217d4560c2ee50d79b4571f7ed58424f432c59a"}, "docker": "quay.io/biocontainers/mp-est", "aliases": {"mpest": "/usr/local/bin/mpest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mp-est.
singularity registry hpc automated addition for mp-est
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mp-est
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mp-est:3.0.0--h031d066_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mp-est/3.0.0--h031d066_1
$ module help quay.io/biocontainers/mp-est/3.0.0--h031d066_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mp-est-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mp-est-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mp-est-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mp-est-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mp-est-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mp-est-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpest

```bash
$ singularity exec <container> /usr/local/bin/mpest
$ podman run --it --rm --entrypoint /usr/local/bin/mpest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpest   -v ${PWD} -w ${PWD} <container> -c " $@"
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