---
layout: container
name:  "quay.io/biocontainers/textinput"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/textinput/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/textinput/container.yaml"
updated_at: "2025-04-14 03:27:56.528329"
latest: "0.2--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/textinput"
aliases:
 - "filter"
 - "hidehead"
 - "innerjoin"
 - "intersect"
 - "mean"
 - "nohead"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.2--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for textinput"
config: {"url": "https://biocontainers.pro/tools/textinput", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for textinput", "latest": {"0.2--pyh864c0ab_1": "sha256:6f2ab57f904258cc7f311616f0fd5b76b4cf69a0d7645b5b5f5d05a232c39c1a"}, "tags": {"0.2--pyh864c0ab_1": "sha256:6f2ab57f904258cc7f311616f0fd5b76b4cf69a0d7645b5b5f5d05a232c39c1a"}, "docker": "quay.io/biocontainers/textinput", "aliases": {"filter": "/usr/local/bin/filter", "hidehead": "/usr/local/bin/hidehead", "innerjoin": "/usr/local/bin/innerjoin", "intersect": "/usr/local/bin/intersect", "mean": "/usr/local/bin/mean", "nohead": "/usr/local/bin/nohead", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/textinput.
shpc-registry automated BioContainers addition for textinput
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/textinput
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/textinput:0.2--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/textinput/0.2--pyh864c0ab_1
$ module help quay.io/biocontainers/textinput/0.2--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### textinput-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### textinput-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### textinput-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### textinput-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### textinput-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### textinput-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### filter

```bash
$ singularity exec <container> /usr/local/bin/filter
$ podman run --it --rm --entrypoint /usr/local/bin/filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hidehead

```bash
$ singularity exec <container> /usr/local/bin/hidehead
$ podman run --it --rm --entrypoint /usr/local/bin/hidehead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hidehead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### innerjoin

```bash
$ singularity exec <container> /usr/local/bin/innerjoin
$ podman run --it --rm --entrypoint /usr/local/bin/innerjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/innerjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersect

```bash
$ singularity exec <container> /usr/local/bin/intersect
$ podman run --it --rm --entrypoint /usr/local/bin/intersect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mean

```bash
$ singularity exec <container> /usr/local/bin/mean
$ podman run --it --rm --entrypoint /usr/local/bin/mean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nohead

```bash
$ singularity exec <container> /usr/local/bin/nohead
$ podman run --it --rm --entrypoint /usr/local/bin/nohead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nohead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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