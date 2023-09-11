---
layout: container
name:  "quay.io/biocontainers/mp3treesim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mp3treesim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mp3treesim/container.yaml"
updated_at: "2023-09-11 03:31:31.675995"
latest: "1.0.6--py_0"
container_url: "https://biocontainers.pro/tools/mp3treesim"
aliases:
 - "mp3treesim"
 - "cxpm"
 - "sxpm"
 - "acyclic"
 - "bcomps"
 - "ccomps"
 - "circo"
 - "dijkstra"
 - "dot"
 - "dot2gxl"
 - "dot_builtins"
versions:
 - "1.0.6--py_0"
description: "shpc-registry automated BioContainers addition for mp3treesim"
config: {"url": "https://biocontainers.pro/tools/mp3treesim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mp3treesim", "latest": {"1.0.6--py_0": "sha256:34d94e5828677f51ee17ec89ac3d6e40787881519e894f50ae891c67ee05c53b"}, "tags": {"1.0.6--py_0": "sha256:34d94e5828677f51ee17ec89ac3d6e40787881519e894f50ae891c67ee05c53b"}, "docker": "quay.io/biocontainers/mp3treesim", "aliases": {"mp3treesim": "/usr/local/bin/mp3treesim", "cxpm": "/usr/local/bin/cxpm", "sxpm": "/usr/local/bin/sxpm", "acyclic": "/usr/local/bin/acyclic", "bcomps": "/usr/local/bin/bcomps", "ccomps": "/usr/local/bin/ccomps", "circo": "/usr/local/bin/circo", "dijkstra": "/usr/local/bin/dijkstra", "dot": "/usr/local/bin/dot", "dot2gxl": "/usr/local/bin/dot2gxl", "dot_builtins": "/usr/local/bin/dot_builtins"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mp3treesim.
shpc-registry automated BioContainers addition for mp3treesim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mp3treesim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mp3treesim:1.0.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mp3treesim/1.0.6--py_0
$ module help quay.io/biocontainers/mp3treesim/1.0.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mp3treesim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mp3treesim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mp3treesim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mp3treesim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mp3treesim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mp3treesim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mp3treesim

```bash
$ singularity exec <container> /usr/local/bin/mp3treesim
$ podman run --it --rm --entrypoint /usr/local/bin/mp3treesim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mp3treesim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxpm

```bash
$ singularity exec <container> /usr/local/bin/cxpm
$ podman run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sxpm

```bash
$ singularity exec <container> /usr/local/bin/sxpm
$ podman run --it --rm --entrypoint /usr/local/bin/sxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dot2gxl

```bash
$ singularity exec <container> /usr/local/bin/dot2gxl
$ podman run --it --rm --entrypoint /usr/local/bin/dot2gxl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot2gxl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dot_builtins

```bash
$ singularity exec <container> /usr/local/bin/dot_builtins
$ podman run --it --rm --entrypoint /usr/local/bin/dot_builtins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot_builtins   -v ${PWD} -w ${PWD} <container> -c " $@"
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