---
layout: container
name:  "quay.io/biocontainers/pplacer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pplacer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pplacer/container.yaml"
updated_at: "2024-11-14 04:22:18.929123"
latest: "1.1.alpha19--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/pplacer"
aliases:
 - "pplacer"
 - "rppr"
 - "guppy"
versions:
 - "1.1.alpha19--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for pplacer"
config: {"url": "https://biocontainers.pro/tools/pplacer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pplacer", "latest": {"1.1.alpha19--h9ee0642_2": "sha256:5ff394bb7863b160346f7ecc528ffe3b932250000d3f364d7a8caae1a724ae04"}, "tags": {"1.1.alpha19--h9ee0642_2": "sha256:5ff394bb7863b160346f7ecc528ffe3b932250000d3f364d7a8caae1a724ae04"}, "docker": "quay.io/biocontainers/pplacer", "aliases": {"pplacer": "/usr/local/bin/pplacer", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pplacer.
shpc-registry automated BioContainers addition for pplacer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pplacer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pplacer:1.1.alpha19--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pplacer/1.1.alpha19--h9ee0642_2
$ module help quay.io/biocontainers/pplacer/1.1.alpha19--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pplacer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pplacer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pplacer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pplacer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pplacer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pplacer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
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