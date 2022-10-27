---
layout: container
name:  "quay.io/biocontainers/decifer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/decifer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/decifer/container.yaml"
updated_at: "2022-10-27 00:37:02.198783"
latest: "2.1.3--py310h243b37b_0"
container_url: "https://biocontainers.pro/tools/decifer"
aliases:
 - "decifer"
 - "dimacs-solver"
 - "dimacs-to-lgf"
 - "fitbeta"
 - "generatestatetrees"
 - "lemon-0.x-to-1.x.sh"
 - "lgf-gen"
 - "mergestatetrees"
versions:
 - "2.1.3--py310h243b37b_0"
description: "shpc-registry automated BioContainers addition for decifer"
config: {"url": "https://biocontainers.pro/tools/decifer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for decifer", "latest": {"2.1.3--py310h243b37b_0": "sha256:37cc1cfb5ec58fba59d16e7ec13c54369aa8999bd808e41cca6d1f249acadd3a"}, "tags": {"2.1.3--py310h243b37b_0": "sha256:37cc1cfb5ec58fba59d16e7ec13c54369aa8999bd808e41cca6d1f249acadd3a"}, "docker": "quay.io/biocontainers/decifer", "aliases": {"decifer": "/usr/local/bin/decifer", "dimacs-solver": "/usr/local/bin/dimacs-solver", "dimacs-to-lgf": "/usr/local/bin/dimacs-to-lgf", "fitbeta": "/usr/local/bin/fitbeta", "generatestatetrees": "/usr/local/bin/generatestatetrees", "lemon-0.x-to-1.x.sh": "/usr/local/bin/lemon-0.x-to-1.x.sh", "lgf-gen": "/usr/local/bin/lgf-gen", "mergestatetrees": "/usr/local/bin/mergestatetrees"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/decifer.
shpc-registry automated BioContainers addition for decifer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/decifer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/decifer:2.1.3--py310h243b37b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/decifer/2.1.3--py310h243b37b_0
$ module help quay.io/biocontainers/decifer/2.1.3--py310h243b37b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### decifer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### decifer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### decifer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### decifer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### decifer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### decifer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### decifer

```bash
$ singularity exec <container> /usr/local/bin/decifer
$ podman run --it --rm --entrypoint /usr/local/bin/decifer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/decifer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dimacs-solver

```bash
$ singularity exec <container> /usr/local/bin/dimacs-solver
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dimacs-to-lgf

```bash
$ singularity exec <container> /usr/local/bin/dimacs-to-lgf
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitbeta

```bash
$ singularity exec <container> /usr/local/bin/fitbeta
$ podman run --it --rm --entrypoint /usr/local/bin/fitbeta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitbeta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generatestatetrees

```bash
$ singularity exec <container> /usr/local/bin/generatestatetrees
$ podman run --it --rm --entrypoint /usr/local/bin/generatestatetrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generatestatetrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lemon-0.x-to-1.x.sh

```bash
$ singularity exec <container> /usr/local/bin/lemon-0.x-to-1.x.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lgf-gen

```bash
$ singularity exec <container> /usr/local/bin/lgf-gen
$ podman run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergestatetrees

```bash
$ singularity exec <container> /usr/local/bin/mergestatetrees
$ podman run --it --rm --entrypoint /usr/local/bin/mergestatetrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergestatetrees   -v ${PWD} -w ${PWD} <container> -c " $@"
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