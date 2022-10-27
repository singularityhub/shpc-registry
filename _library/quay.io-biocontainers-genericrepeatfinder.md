---
layout: container
name:  "quay.io/biocontainers/genericrepeatfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genericrepeatfinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/genericrepeatfinder/container.yaml"
updated_at: "2022-10-27 01:06:50.661447"
latest: "1.0--h9f5acd7_2"
container_url: "https://biocontainers.pro/tools/genericrepeatfinder"
aliases:
 - "grf-alignment"
 - "grf-alignment2"
 - "grf-dbn"
 - "grf-filter"
 - "grf-intersperse"
 - "grf-main"
 - "grf-mite-cluster"
 - "grf-nest"
versions:
 - "1.0--h9f5acd7_2"
description: "shpc-registry automated BioContainers addition for genericrepeatfinder"
config: {"url": "https://biocontainers.pro/tools/genericrepeatfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genericrepeatfinder", "latest": {"1.0--h9f5acd7_2": "sha256:d71ebb1867d9f6d3a7b6e80f39888a3276066e76ee816bf6ef9ef2a74b888226"}, "tags": {"1.0--h9f5acd7_2": "sha256:d71ebb1867d9f6d3a7b6e80f39888a3276066e76ee816bf6ef9ef2a74b888226"}, "docker": "quay.io/biocontainers/genericrepeatfinder", "aliases": {"grf-alignment": "/usr/local/bin/grf-alignment", "grf-alignment2": "/usr/local/bin/grf-alignment2", "grf-dbn": "/usr/local/bin/grf-dbn", "grf-filter": "/usr/local/bin/grf-filter", "grf-intersperse": "/usr/local/bin/grf-intersperse", "grf-main": "/usr/local/bin/grf-main", "grf-mite-cluster": "/usr/local/bin/grf-mite-cluster", "grf-nest": "/usr/local/bin/grf-nest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genericrepeatfinder.
shpc-registry automated BioContainers addition for genericrepeatfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genericrepeatfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genericrepeatfinder:1.0--h9f5acd7_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genericrepeatfinder/1.0--h9f5acd7_2
$ module help quay.io/biocontainers/genericrepeatfinder/1.0--h9f5acd7_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genericrepeatfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genericrepeatfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genericrepeatfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genericrepeatfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genericrepeatfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genericrepeatfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grf-alignment

```bash
$ singularity exec <container> /usr/local/bin/grf-alignment
$ podman run --it --rm --entrypoint /usr/local/bin/grf-alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-alignment2

```bash
$ singularity exec <container> /usr/local/bin/grf-alignment2
$ podman run --it --rm --entrypoint /usr/local/bin/grf-alignment2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-alignment2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-dbn

```bash
$ singularity exec <container> /usr/local/bin/grf-dbn
$ podman run --it --rm --entrypoint /usr/local/bin/grf-dbn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-dbn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-filter

```bash
$ singularity exec <container> /usr/local/bin/grf-filter
$ podman run --it --rm --entrypoint /usr/local/bin/grf-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-intersperse

```bash
$ singularity exec <container> /usr/local/bin/grf-intersperse
$ podman run --it --rm --entrypoint /usr/local/bin/grf-intersperse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-intersperse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-main

```bash
$ singularity exec <container> /usr/local/bin/grf-main
$ podman run --it --rm --entrypoint /usr/local/bin/grf-main   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-main   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-mite-cluster

```bash
$ singularity exec <container> /usr/local/bin/grf-mite-cluster
$ podman run --it --rm --entrypoint /usr/local/bin/grf-mite-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-mite-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-nest

```bash
$ singularity exec <container> /usr/local/bin/grf-nest
$ podman run --it --rm --entrypoint /usr/local/bin/grf-nest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-nest   -v ${PWD} -w ${PWD} <container> -c " $@"
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