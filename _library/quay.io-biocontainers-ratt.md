---
layout: container
name:  "quay.io/biocontainers/ratt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ratt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ratt/container.yaml"
updated_at: "2023-07-21 03:05:08.680638"
latest: "1.0.3--0"
container_url: "https://biocontainers.pro/tools/ratt"
aliases:
 - "ratt"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
versions:
 - "1.0.3--0"
description: "shpc-registry automated BioContainers addition for ratt"
config: {"url": "https://biocontainers.pro/tools/ratt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ratt", "latest": {"1.0.3--0": "sha256:35d16252b76add0043d5ed139a8fe49cc666bf662bb34d10333f793f6cc38381"}, "tags": {"1.0.3--0": "sha256:35d16252b76add0043d5ed139a8fe49cc666bf662bb34d10333f793f6cc38381"}, "docker": "quay.io/biocontainers/ratt", "aliases": {"ratt": "/usr/local/bin/ratt", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ratt.
shpc-registry automated BioContainers addition for ratt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ratt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ratt:1.0.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ratt/1.0.3--0
$ module help quay.io/biocontainers/ratt/1.0.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ratt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ratt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ratt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ratt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ratt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ratt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ratt

```bash
$ singularity exec <container> /usr/local/bin/ratt
$ podman run --it --rm --entrypoint /usr/local/bin/ratt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ratt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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