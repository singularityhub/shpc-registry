---
layout: container
name:  "quay.io/biocontainers/rp2paths"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rp2paths/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rp2paths/container.yaml"
updated_at: "2022-10-29 05:51:19.628057"
latest: "1.5.0"
container_url: "https://biocontainers.pro/tools/rp2paths"
aliases:
 - "2to3-3.7"
 - "acyclic"
 - "aserver"
 - "bcomps"
 - "ccomps"
 - "circo"
 - "cluster"
 - "cxpm"
 - "dijkstra"
 - "dot"
versions:
 - "1.5.0"
description: "shpc-registry automated BioContainers addition for rp2paths"
config: {"url": "https://biocontainers.pro/tools/rp2paths", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rp2paths", "latest": {"1.5.0": "sha256:bfd41807000936370ad5f77004aef24e9746887844dfb096d15856f026a892e7"}, "tags": {"1.5.0": "sha256:bfd41807000936370ad5f77004aef24e9746887844dfb096d15856f026a892e7"}, "docker": "quay.io/biocontainers/rp2paths", "aliases": {"2to3-3.7": "/usr/local/bin/2to3-3.7", "acyclic": "/usr/local/bin/acyclic", "aserver": "/usr/local/bin/aserver", "bcomps": "/usr/local/bin/bcomps", "ccomps": "/usr/local/bin/ccomps", "circo": "/usr/local/bin/circo", "cluster": "/usr/local/bin/cluster", "cxpm": "/usr/local/bin/cxpm", "dijkstra": "/usr/local/bin/dijkstra", "dot": "/usr/local/bin/dot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rp2paths.
shpc-registry automated BioContainers addition for rp2paths
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rp2paths
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rp2paths:1.5.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rp2paths/1.5.0
$ module help quay.io/biocontainers/rp2paths/1.5.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rp2paths-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rp2paths-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rp2paths-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rp2paths-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rp2paths-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rp2paths-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccomps

```bash
$ singularity exec <container> /usr/local/bin/ccomps
$ podman run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circo

```bash
$ singularity exec <container> /usr/local/bin/circo
$ podman run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxpm

```bash
$ singularity exec <container> /usr/local/bin/cxpm
$ podman run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dijkstra

```bash
$ singularity exec <container> /usr/local/bin/dijkstra
$ podman run --it --rm --entrypoint /usr/local/bin/dijkstra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dijkstra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dot

```bash
$ singularity exec <container> /usr/local/bin/dot
$ podman run --it --rm --entrypoint /usr/local/bin/dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot   -v ${PWD} -w ${PWD} <container> -c " $@"
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