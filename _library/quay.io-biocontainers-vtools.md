---
layout: container
name:  "quay.io/biocontainers/vtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vtools/container.yaml"
updated_at: "2022-10-27 00:21:37.915320"
latest: "1.1.0--py38h17adfb0_4"
container_url: "https://biocontainers.pro/tools/vtools"
aliases:
 - "vtools-evaluate"
 - "vtools-filter"
 - "vtools-gcoverage"
 - "vtools-stats"
versions:
 - "1.1.0--py38h17adfb0_4"
description: "shpc-registry automated BioContainers addition for vtools"
config: {"url": "https://biocontainers.pro/tools/vtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vtools", "latest": {"1.1.0--py38h17adfb0_4": "sha256:99e3cf0a7d21ab2583f9685f161e384a222561b7d5d97fc630d103dc0c8102da"}, "tags": {"1.1.0--py38h17adfb0_4": "sha256:99e3cf0a7d21ab2583f9685f161e384a222561b7d5d97fc630d103dc0c8102da"}, "docker": "quay.io/biocontainers/vtools", "aliases": {"vtools-evaluate": "/usr/local/bin/vtools-evaluate", "vtools-filter": "/usr/local/bin/vtools-filter", "vtools-gcoverage": "/usr/local/bin/vtools-gcoverage", "vtools-stats": "/usr/local/bin/vtools-stats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vtools.
shpc-registry automated BioContainers addition for vtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vtools:1.1.0--py38h17adfb0_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vtools/1.1.0--py38h17adfb0_4
$ module help quay.io/biocontainers/vtools/1.1.0--py38h17adfb0_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vtools-evaluate

```bash
$ singularity exec <container> /usr/local/bin/vtools-evaluate
$ podman run --it --rm --entrypoint /usr/local/bin/vtools-evaluate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtools-evaluate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtools-filter

```bash
$ singularity exec <container> /usr/local/bin/vtools-filter
$ podman run --it --rm --entrypoint /usr/local/bin/vtools-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtools-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtools-gcoverage

```bash
$ singularity exec <container> /usr/local/bin/vtools-gcoverage
$ podman run --it --rm --entrypoint /usr/local/bin/vtools-gcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtools-gcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtools-stats

```bash
$ singularity exec <container> /usr/local/bin/vtools-stats
$ podman run --it --rm --entrypoint /usr/local/bin/vtools-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtools-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
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