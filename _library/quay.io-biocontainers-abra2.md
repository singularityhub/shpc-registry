---
layout: container
name:  "quay.io/biocontainers/abra2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abra2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abra2/container.yaml"
updated_at: "2022-10-26 02:46:46.989280"
latest: "2.24--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/2pg_cartesian"
aliases:
 - "abra2"
 - "aserver"
 - "autopoint"
 - "hb-ot-shape-closure"
 - "hb-shape"
 - "hb-subset"
 - "hb-view"
versions:
 - "2.24--h9f5acd7_1"
description: "shpc-registry automated BioContainers addition for 2pg_cartesian"
config: {"url": "https://biocontainers.pro/tools/2pg_cartesian", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for 2pg_cartesian", "latest": {"2.24--h9f5acd7_1": "sha256:20c656ed1353e22a0fcc611f7a0b845f1340a01e7aabf1781731e8a0485857d2"}, "tags": {"2.24--h9f5acd7_1": "sha256:20c656ed1353e22a0fcc611f7a0b845f1340a01e7aabf1781731e8a0485857d2"}, "docker": "quay.io/biocontainers/abra2", "aliases": {"abra2": "/usr/local/bin/abra2", "aserver": "/usr/local/bin/aserver", "autopoint": "/usr/local/bin/autopoint", "hb-ot-shape-closure": "/usr/local/bin/hb-ot-shape-closure", "hb-shape": "/usr/local/bin/hb-shape", "hb-subset": "/usr/local/bin/hb-subset", "hb-view": "/usr/local/bin/hb-view"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abra2.
shpc-registry automated BioContainers addition for 2pg_cartesian
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abra2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abra2:2.24--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abra2/2.24--h9f5acd7_1
$ module help quay.io/biocontainers/abra2/2.24--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abra2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abra2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abra2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abra2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abra2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abra2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abra2

```bash
$ singularity exec <container> /usr/local/bin/abra2
$ podman run --it --rm --entrypoint /usr/local/bin/abra2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abra2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autopoint

```bash
$ singularity exec <container> /usr/local/bin/autopoint
$ podman run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-ot-shape-closure

```bash
$ singularity exec <container> /usr/local/bin/hb-ot-shape-closure
$ podman run --it --rm --entrypoint /usr/local/bin/hb-ot-shape-closure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-ot-shape-closure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-shape

```bash
$ singularity exec <container> /usr/local/bin/hb-shape
$ podman run --it --rm --entrypoint /usr/local/bin/hb-shape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-shape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-subset

```bash
$ singularity exec <container> /usr/local/bin/hb-subset
$ podman run --it --rm --entrypoint /usr/local/bin/hb-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-view

```bash
$ singularity exec <container> /usr/local/bin/hb-view
$ podman run --it --rm --entrypoint /usr/local/bin/hb-view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-view   -v ${PWD} -w ${PWD} <container> -c " $@"
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