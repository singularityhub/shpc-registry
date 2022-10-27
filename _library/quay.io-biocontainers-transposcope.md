---
layout: container
name:  "quay.io/biocontainers/transposcope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transposcope/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/transposcope/container.yaml"
updated_at: "2022-10-27 00:47:12.063732"
latest: "2.0.1--py_0"
container_url: "https://biocontainers.pro/tools/transposcope"
aliases:
 - "transposcope"
versions:
 - "2.0.1--py_0"
description: "shpc-registry automated BioContainers addition for transposcope"
config: {"url": "https://biocontainers.pro/tools/transposcope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transposcope", "latest": {"2.0.1--py_0": "sha256:f3de42cc97feb93bff6ca66be208ecee91e3751ab9006423247f9af3528dad00"}, "tags": {"2.0.1--py_0": "sha256:f3de42cc97feb93bff6ca66be208ecee91e3751ab9006423247f9af3528dad00"}, "docker": "quay.io/biocontainers/transposcope", "aliases": {"transposcope": "/usr/local/bin/transposcope"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transposcope.
shpc-registry automated BioContainers addition for transposcope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transposcope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transposcope:2.0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transposcope/2.0.1--py_0
$ module help quay.io/biocontainers/transposcope/2.0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transposcope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transposcope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transposcope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transposcope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transposcope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transposcope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### transposcope

```bash
$ singularity exec <container> /usr/local/bin/transposcope
$ podman run --it --rm --entrypoint /usr/local/bin/transposcope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transposcope   -v ${PWD} -w ${PWD} <container> -c " $@"
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