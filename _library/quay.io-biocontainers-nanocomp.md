---
layout: container
name:  "quay.io/biocontainers/nanocomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanocomp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanocomp/container.yaml"
updated_at: "2022-10-27 00:52:59.593018"
latest: "1.9.2--py_1"
container_url: "https://biocontainers.pro/tools/nanocomp"
aliases:
 - "NanoComp"
 - "NanoPlot"
 - "orca-server"
 - "pauvre"
versions:
 - "1.9.2--py_1"
description: "shpc-registry automated BioContainers addition for nanocomp"
config: {"url": "https://biocontainers.pro/tools/nanocomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanocomp", "latest": {"1.9.2--py_1": "sha256:a89340a72ef720c08a6360d00eda2b59f2a2e59c5f8e701fe3fa81077a8124f5"}, "tags": {"1.9.2--py_1": "sha256:a89340a72ef720c08a6360d00eda2b59f2a2e59c5f8e701fe3fa81077a8124f5"}, "docker": "quay.io/biocontainers/nanocomp", "aliases": {"NanoComp": "/usr/local/bin/NanoComp", "NanoPlot": "/usr/local/bin/NanoPlot", "orca-server": "/usr/local/bin/orca-server", "pauvre": "/usr/local/bin/pauvre"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanocomp.
shpc-registry automated BioContainers addition for nanocomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanocomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanocomp:1.9.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanocomp/1.9.2--py_1
$ module help quay.io/biocontainers/nanocomp/1.9.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanocomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanocomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanocomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanocomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanocomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanocomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoComp

```bash
$ singularity exec <container> /usr/local/bin/NanoComp
$ podman run --it --rm --entrypoint /usr/local/bin/NanoComp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoComp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NanoPlot

```bash
$ singularity exec <container> /usr/local/bin/NanoPlot
$ podman run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orca-server

```bash
$ singularity exec <container> /usr/local/bin/orca-server
$ podman run --it --rm --entrypoint /usr/local/bin/orca-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orca-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pauvre

```bash
$ singularity exec <container> /usr/local/bin/pauvre
$ podman run --it --rm --entrypoint /usr/local/bin/pauvre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pauvre   -v ${PWD} -w ${PWD} <container> -c " $@"
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