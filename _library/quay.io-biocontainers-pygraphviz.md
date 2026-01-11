---
layout: container
name:  "quay.io/biocontainers/pygraphviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pygraphviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pygraphviz/container.yaml"
updated_at: "2026-01-11 03:57:22.552470"
latest: "1.3.1--py36_0"
container_url: "https://biocontainers.pro/tools/pygraphviz"
aliases:
 - "dotty"
 - "lneato"
 - "easy_install-3.6"
 - "acyclic"
 - "bcomps"
 - "ccomps"
 - "circo"
 - "dijkstra"
 - "dot"
 - "dot2gxl"
 - "dot_builtins"
 - "edgepaint"
versions:
 - "1.3.1--py36_0"
description: "shpc-registry automated BioContainers addition for pygraphviz"
config: {"url": "https://biocontainers.pro/tools/pygraphviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pygraphviz", "latest": {"1.3.1--py36_0": "sha256:5fac17d32f7ad12ea6ca32189ef754f6c6b1c10a48cf5a4721ef30398d8fee8c"}, "tags": {"1.3.1--py36_0": "sha256:5fac17d32f7ad12ea6ca32189ef754f6c6b1c10a48cf5a4721ef30398d8fee8c"}, "docker": "quay.io/biocontainers/pygraphviz", "aliases": {"dotty": "/usr/local/bin/dotty", "lneato": "/usr/local/bin/lneato", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "acyclic": "/usr/local/bin/acyclic", "bcomps": "/usr/local/bin/bcomps", "ccomps": "/usr/local/bin/ccomps", "circo": "/usr/local/bin/circo", "dijkstra": "/usr/local/bin/dijkstra", "dot": "/usr/local/bin/dot", "dot2gxl": "/usr/local/bin/dot2gxl", "dot_builtins": "/usr/local/bin/dot_builtins", "edgepaint": "/usr/local/bin/edgepaint"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pygraphviz.
shpc-registry automated BioContainers addition for pygraphviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pygraphviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pygraphviz:1.3.1--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pygraphviz/1.3.1--py36_0
$ module help quay.io/biocontainers/pygraphviz/1.3.1--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pygraphviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pygraphviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pygraphviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pygraphviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pygraphviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pygraphviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dotty

```bash
$ singularity exec <container> /usr/local/bin/dotty
$ podman run --it --rm --entrypoint /usr/local/bin/dotty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lneato

```bash
$ singularity exec <container> /usr/local/bin/lneato
$ podman run --it --rm --entrypoint /usr/local/bin/lneato   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lneato   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### edgepaint

```bash
$ singularity exec <container> /usr/local/bin/edgepaint
$ podman run --it --rm --entrypoint /usr/local/bin/edgepaint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edgepaint   -v ${PWD} -w ${PWD} <container> -c " $@"
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