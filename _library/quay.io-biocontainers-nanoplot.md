---
layout: container
name:  "quay.io/biocontainers/nanoplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanoplot/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanoplot/container.yaml"
updated_at: "2022-10-27 00:33:35.829480"
latest: "1.8.1--py36_0"
container_url: "https://biocontainers.pro/tools/nanoplot"
aliases:
 - "NanoPlot"
 - "pauvre"
versions:
 - "1.8.1--py36_0"
description: "shpc-registry automated BioContainers addition for nanoplot"
config: {"url": "https://biocontainers.pro/tools/nanoplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanoplot", "latest": {"1.8.1--py36_0": "sha256:4ceaff31ac1534bf1ccdea215a6ca6e248dd3c5ac039994ee2e06979224171b7"}, "tags": {"1.8.1--py36_0": "sha256:4ceaff31ac1534bf1ccdea215a6ca6e248dd3c5ac039994ee2e06979224171b7"}, "docker": "quay.io/biocontainers/nanoplot", "aliases": {"NanoPlot": "/usr/local/bin/NanoPlot", "pauvre": "/usr/local/bin/pauvre"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanoplot.
shpc-registry automated BioContainers addition for nanoplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanoplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanoplot:1.8.1--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanoplot/1.8.1--py36_0
$ module help quay.io/biocontainers/nanoplot/1.8.1--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanoplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanoplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanoplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanoplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanoplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanoplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoPlot

```bash
$ singularity exec <container> /usr/local/bin/NanoPlot
$ podman run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
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