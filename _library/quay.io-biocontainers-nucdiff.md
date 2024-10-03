---
layout: container
name:  "quay.io/biocontainers/nucdiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nucdiff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nucdiff/container.yaml"
updated_at: "2024-10-03 03:00:05.145004"
latest: "2.0.3--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/nucdiff"
aliases:
 - "nucdiff"
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
 - "2.0.3--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for nucdiff"
config: {"url": "https://biocontainers.pro/tools/nucdiff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nucdiff", "latest": {"2.0.3--pyh864c0ab_1": "sha256:a90cfb5c6434af71c774551258ec381f2c3a40bc28d038ce3ddadd142932e378"}, "tags": {"2.0.3--pyh864c0ab_1": "sha256:a90cfb5c6434af71c774551258ec381f2c3a40bc28d038ce3ddadd142932e378"}, "docker": "quay.io/biocontainers/nucdiff", "aliases": {"nucdiff": "/usr/local/bin/nucdiff", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nucdiff.
shpc-registry automated BioContainers addition for nucdiff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nucdiff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nucdiff:2.0.3--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nucdiff/2.0.3--pyh864c0ab_1
$ module help quay.io/biocontainers/nucdiff/2.0.3--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nucdiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nucdiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nucdiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nucdiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nucdiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nucdiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nucdiff

```bash
$ singularity exec <container> /usr/local/bin/nucdiff
$ podman run --it --rm --entrypoint /usr/local/bin/nucdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
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