---
layout: container
name:  "quay.io/biocontainers/bwise"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwise/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwise/container.yaml"
updated_at: "2024-12-16 03:50:11.254754"
latest: "1.0.0--h43eeafb_3"
container_url: "https://biocontainers.pro/tools/bwise"
aliases:
 - "bcalm"
 - "bgreat"
 - "btrim"
 - "bwise"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "h5cc"
versions:
 - "1.0.0--h5b5514e_2"
 - "1.0.0--h43eeafb_3"
description: "shpc-registry automated BioContainers addition for bwise"
config: {"url": "https://biocontainers.pro/tools/bwise", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bwise", "latest": {"1.0.0--h43eeafb_3": "sha256:e74d7abf5c686cba53c018e3157fb897a00f66f6ca2a41fb1908a15fac005f8c"}, "tags": {"1.0.0--h5b5514e_2": "sha256:473530ec687bd650d518f8330e94e0885e896ef3730e9284817fdb028e2a0311", "1.0.0--h43eeafb_3": "sha256:e74d7abf5c686cba53c018e3157fb897a00f66f6ca2a41fb1908a15fac005f8c"}, "docker": "quay.io/biocontainers/bwise", "aliases": {"bcalm": "/usr/local/bin/bcalm", "bgreat": "/usr/local/bin/bgreat", "btrim": "/usr/local/bin/btrim", "bwise": "/usr/local/bin/bwise", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "h5cc": "/usr/local/bin/h5cc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwise.
shpc-registry automated BioContainers addition for bwise
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwise
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwise:1.0.0--h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwise/1.0.0--h43eeafb_3
$ module help quay.io/biocontainers/bwise/1.0.0--h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwise-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwise-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwise-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwise-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwise-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwise-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcalm

```bash
$ singularity exec <container> /usr/local/bin/bcalm
$ podman run --it --rm --entrypoint /usr/local/bin/bcalm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcalm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgreat

```bash
$ singularity exec <container> /usr/local/bin/bgreat
$ podman run --it --rm --entrypoint /usr/local/bin/bgreat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgreat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### btrim

```bash
$ singularity exec <container> /usr/local/bin/btrim
$ podman run --it --rm --entrypoint /usr/local/bin/btrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/btrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwise

```bash
$ singularity exec <container> /usr/local/bin/bwise
$ podman run --it --rm --entrypoint /usr/local/bin/bwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
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